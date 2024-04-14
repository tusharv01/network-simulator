# Network Simulation

This Python script simulates a network with end devices, hubs, and switches. Demonstrates CSMA/CD, Go-Back-N, Selective Repeat, and Stop-and-Wait ARQ.

---

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/network-simulator.git

# Navigate to the Directory
cd network-simulator

# Run the Script
python network_simulator.py


## Test Cases

1. **Dedicated Connection**
   Establishes a dedicated connection between two end devices.
   - **Input:** Message from Device 1 to Device 2.

2. **Star Topology**
   Simulates a star topology with five end devices connected to a hub.
   - **Input:** Message from a randomly selected device.

3. **Switch Network**
   Demonstrates a switch network with CSMA/CD, Go-Back-N, and Selective Repeat ARQ.
   - **Input:** Sender, receiver, message, and protocol choice.

4. **Interconnected Star Topologies**
   Simulates two star topologies connected by a switch.
   - **Input:** Message between randomly selected devices.

---

## Additional Features
- **CSMA/CD:** Detects collisions in shared media.
- **Go-Back-N ARQ:** Retransmits a window of frames.
- **Selective Repeat ARQ:** Retransmits only lost frames.
- **Stop-and-Wait ARQ:** Waits for acknowledgment before sending next frame.

---

### Author: Tushar Verma
