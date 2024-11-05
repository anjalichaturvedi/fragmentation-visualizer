import matplotlib.pyplot as plt
import random

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
            header = {
                "packet_id": self.packet_id,
                "fragment_id": fragment_id,
                "offset": offset - len(fragment_data),
                "is_last": is_last,
                "checksum": checksum
            }
            fragment = Fragment(header, fragment_data)
            self.fragments.append(fragment)
            fragment_id += 1

    def visualize_entire_packet(self):
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
        fig, ax = plt.subplots(figsize=(10, 6))
        y_positions = range(len(self.fragments))
        
        for i, fragment in enumerate(self.fragments):
            color = (random.random(), random.random(), random.random())
            ax.broken_barh([(fragment.header["offset"], len(fragment.data))], (i - 0.4, 0.8), facecolors=color, edgecolor='black')
            header_text = (f"ID: {fragment.header['packet_id']}, Frag: {fragment.header['fragment_id']}, "
                           f"Offset: {fragment.header['offset']}, Last: {fragment.header['is_last']}, "
                           f"Checksum: {fragment.header['checksum']}")
            ax.text(-0.1, i, header_text, ha='right', va='center', color='black', fontsize=8)
            ax.text(fragment.header["offset"] + len(fragment.data) / 2, i, fragment.data, ha='center', va='center', color='white')
            ax.set_xlim(-10, len(self.data) + 10)
            ax.set_ylim(-1, len(self.fragments))
            ax.set_yticks([])
            ax.set_xlabel("Offset")
            ax.set_title("Fragmentation Process: Each Fragment with Headers and Data")
            plt.pause(0.5)
        plt.show()

    def reassemble(self):
        return ''.join(fragment.data for fragment in sorted(self.fragments, key=lambda x: x.header["offset"]))

    def visualize_reassembly(self):
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.set_xlim(0, len(self.data))
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Reassembly Process")
        reassembled_data = ""
        for fragment in sorted(self.fragments, key=lambda x: x.header["offset"]):
            reassembled_data += fragment.data
            for i, char in enumerate(reassembled_data):
                ax.text(i, 0.5, char, ha="center", va="center", fontsize=12, color="black")
            plt.pause(0.5)
        plt.show()

class Fragment:
    def __init__(self, header, data):
        self.header = header
        self.data = data

    def __repr__(self):
        return (f"Packet ID: {self.header['packet_id']}, Fragment ID: {self.header['fragment_id']}, "
                f"Offset: {self.header['offset']}, Last: {self.header['is_last']}, "
                f"Checksum: {self.header['checksum']}, Data: '{self.data}'")
