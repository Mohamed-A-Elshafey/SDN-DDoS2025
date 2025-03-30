# SDN-DDoS2025
 
## Description

SDN-DDoD2025 dataset was collected from an established SDN environment with OpenFlow-based additional features from ICDDoS2019. SDN-DDoD2025 contains port statistics and flow statistics. The captured port statistics, e.g., the number of packets and bytes transmitted and received, and error statistics. Also, the flow statistics, e.g., packet and byte counts, flow duration, and actions associated with the flow. This data provides a comprehensive view of the traffic and performance characteristics of the established SDN network.

## SDN-CSV File Generation Methodology

This document outlines the steps required to generate SDN-CSV files as depicted in the methodology flowchart.

# 1. Establish SDN Virtual Environment

First, we installed Ubuntu 22.04.3 LTS as the base operating system.
# 2. Install Mininet and Ryu Controller

Mininet is a network emulator that allows users to create virtual networks on a single machine, widely used for SDN simulations. Ryu is an open-source SDN controller written in Python that provides network programmability.

Installation Steps:

   -Update system
   sudo apt update

  -Install Mininet
  sudo apt install mininet -y

  -Set up a Python virtual environment for Ryu
  python3 -m venv ryu-env
  source ryu-env/bin/activate

  -Install Ryu and dependencies
  pip install ryu
  dep pip install eventlet==0.30.2
  pip install psutil

  -Start the Ryu controller
  ryu-manager ryu.app.ofctl_rest
  
# 3. Build SDN Network

 We implemented an SDN network similar to CIC-DDoS2019, consisting of:

 Attack-Network: A dedicated infrastructure for launching DDoS attacks.

 Victim-Network: A separate network connected to the controller via a switch, running normal benign traffic.

 We used OpenFlow 1.3 for compatibility with the Ryu controller.
 
# 4. Ingest PCAP Files from CIC-DDoS2019
 The next step is to inject the CIC-DDoS2019 dataset PCAP files into the network using Wireshark, a widely used network protocol analyzer.

# 5. Capture OpenFlow Statistics using Ryu's REST API
 We developed a Python script to capture network statistics via the Ryu REST API, collecting flow, port, and switch statistics for further analysis.

# 6. Parse and Store Network Statistics
Captured traffic contains network statistics such as:Packet counts , Byte counts,Flow durations,Entropy ,CPU usage

These extracted features are saved in a CSV file (SDN-DDoS2025.csv) for deep learning-based DDoS detection.
# 7. Final Output
The extracted SDN statistics are stored in network-stats.csv, which can be used for machine learning and deep learning models.



## Data Format

The dataset is provided in CSV format. Each row represents a network flow, with 39 features extracted. These features provide a comprehensive view of the network traffic and SDN environment. They include:

* **Basic Flow Information:**  `protocol`, `port numbers`, `packet counts`, `byte counts`, `flow duration`.
* **Switch Statistics:** `timestamp`, `type`, `dpid`, `port-no`, `rx-packets`, `tx-packets`, `rx-bytes`, `tx-bytes`, `rx-dropped`, `tx-dropped`, `rx-errors`, `tx-errors`, `rx-frameerr`, `rx-overerr`, `rx-crc-err`, `collisions`.
* **Flow Entry Details:** `priority`, `idle-timeout`, `hard-timeout`, `byte-count`, `packet-count`, `cookie`, `table-id`, `duration-sec`, `duration-nsec`, `length`, `flags`, `actions`, `match`.
* **Group Entry Information:** `group-id`, `ref-count`, `flow-count`.
* **Performance Metrics:** `packet-in-count`, `aggregate-packet-count`, `aggregate-byte-count`, `aggregate-flow-count`, `cpu-util`, `active-flows`, `entropy`.


## Citation Information

If you use this dataset in your research, please cite it as:
https://github.com/Mohamed-A-Elshafey/SDN-DDoS2025/


