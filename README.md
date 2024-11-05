# Fragmentation Visualizer

[@anjalichaturvedi](https://www.github.com/anjalichaturvedi) & [@vibhuchaudhary](https://www.github.com/vibhuchaudhary)

This project simulates packet fragmentation and reassembly, mimicking the handling of large data packets in network protocols. The program divides a large data packet into smaller fragments based on a specified maximum segment size (MSS), adds a header to each fragment, and visualizes the fragmentation and reassembly processes.


## Features

- Fragmentation: Divides data into fragments based on the specified MSS.
- Fragment Header: Each fragment contains a header with the following fields:
    - `packet_id`: Original packet identifier.
    - `fragment_id`: Identifier for each fragment.
    - `offset`: Position of the fragment within the original data.
    - `is_last`: Indicates if the fragment is the last one in the packet.
    - `checksum`: Simple checksum of ASCII values of the fragment data.
- Visualization
    - Complete Packet: Visualizes the entire packet as a single block before fragmentation.
    - Fragmentation Process: Displays each fragment with its header and data.
    - Reassembly Process: Shows real-time reassembly of the fragments to verify data integrity.


## Requirements
- Python 3.x
- `matplotlib` for visualization

Install `matplotlib` with:
``` bash
pip install matplotlib
```

## Usage
![image](https://github.com/user-attachments/assets/9c22e09c-64ea-42bd-a980-aacb6029596c)

