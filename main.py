from packet import Packet

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
