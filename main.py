import matplotlib.pyplot as plt
import random
import time

class Packet:
    def __init__(self, packet_id, data, max_segment_size):
        self.packet_id = packet_id
        self.data = data
        self.max_segment_size = max_segment_size
        self.fragments = []

    def fragment(self):
        self.fragments = []
        total_length = len(self.data)
        offset = 0
        fragment_id = 1

        while offset < total_length:
            is_last = offset + self.max_segment_size >= total_length
            
            fragment_data = self.data[offset:offset + self.max_segment_size]
            offset += self.max_segment_size
            
            checksum = sum(ord(char) for char in fragment_data)
            
            fragment = Fragment(self.packet_id, fragment_id, offset - len(fragment_data), fragment_data, is_last, checksum)
            self.fragments.append(fragment)
            fragment_id += 1

    def visualize_entire_packet(self):
        """Visualizes the entire packet as a single block before fragmentation."""
        fig, ax = plt.subplots(figsize=(12, 2))
        
        ax.broken_barh([(0, len(self.data))], (0.5, 0.8), facecolors='tab:blue', edgecolor='black')
        
        ax.text(len(self.data) / 2, 0.9, self.data, ha="center", va="center", color="white", fontsize=10)
        
        ax.set_xlim(0, len(self.data))
        ax.set_ylim(0, 2)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Complete Packet Before Fragmentation")
        plt.show()
        plt.pause(1)  

    def visualize_fragmentation(self):
        """Visualize each fragment with its header and data step-by-step."""
        fig, ax = plt.subplots(figsize=(10, 6))
        y_positions = range(len(self.fragments))
        
        for i, fragment in enumerate(self.fragments):
            color = (random.random(), random.random(), random.random())
            ax.broken_barh([(fragment.offset, len(fragment.data))], (i - 0.4, 0.8), facecolors=color, edgecolor='black')
            
            header_text = (f"ID: {fragment.packet_id}, Frag: {fragment.fragment_id}, Offset: {fragment.offset}, "
                           f"Last: {fragment.is_last}, Checksum: {fragment.checksum}")
            ax.text(-0.1, i, header_text, ha='right', va='center', color='black', fontsize=8)
            
            ax.text(fragment.offset + len(fragment.data) / 2, i, fragment.data, ha='center', va='center', color='white')
        
            ax.set_xlim(-10, len(self.data) + 10)
            ax.set_ylim(-1, len(self.fragments))
            ax.set_yticks([])
            ax.set_xlabel("Offset")
            ax.set_title("Fragmentation Process: Each Fragment with Headers and Data")
            plt.pause(0.5)  
        plt.show()

    def reassemble(self):
        return ''.join(fragment.data for fragment in sorted(self.fragments, key=lambda x: x.offset))

    def visualize_reassembly(self):
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.set_xlim(0, len(self.data))
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Reassembly Process")

        reassembled_data = ""
        for fragment in sorted(self.fragments, key=lambda x: x.offset):
            reassembled_data += fragment.data
            for i, char in enumerate(reassembled_data):
                ax.text(i, 0.5, char, ha="center", va="center", fontsize=12, color="black")
            plt.pause(0.5)  
        plt.show()

class Fragment:
    def __init__(self, packet_id, fragment_id, offset, data, is_last, checksum):
        self.packet_id = packet_id
        self.fragment_id = fragment_id
        self.offset = offset
        self.data = data
        self.is_last = is_last
        self.checksum = checksum

    def __repr__(self):
        return (f"Packet ID: {self.packet_id}, Fragment ID: {self.fragment_id}, Offset: {self.offset}, "
                f"Last: {self.is_last}, Checksum: {self.checksum}, Data: '{self.data}'")

if __name__ == "__main__":
    packet_data = input("Enter the packet data to be fragmented: ")
    max_segment_size = int(input("Enter the maximum segment size (MSS): "))

    packet = Packet(packet_id=1, data=packet_data, max_segment_size=max_segment_size)

    print("Displaying the entire packet:")
    packet.visualize_entire_packet()

    print("Fragmenting and displaying each fragment:")
    packet.fragment()
    packet.visualize_fragmentation()

    print("Reassembling the packet:")
    packet.visualize_reassembly()

    reassembled_data = packet.reassemble()
    if reassembled_data == packet_data:
        print("\nReassembly successful! The data was correctly reassembled.")
    else:
        print("\nReassembly failed. The data was incomplete or incorrect.")
