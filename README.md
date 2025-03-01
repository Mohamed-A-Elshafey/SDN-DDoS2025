# SDN-DDoS2025

## Description

SDN-DDoD2025 dataset was collected from an established SDN environment with OpenFlow-based additional features from ICDDoS2019. SDN-DDoD2025 contains port statistics and flow statistics. The captured port statistics, e.g., the number of packets and bytes transmitted and received, and error statistics. Also, the flow statistics, e.g., packet and byte counts, flow duration, and actions associated with the flow. This data provides a comprehensive view of the traffic and performance characteristics of the established SDN network.

## Data Collection

The SDN-CSV files were generated through the following steps:

1. **Establish SDN Virtual Environment:**
    * Installed Ubuntu 22.04.3 LTS as the base operating system for the virtual environment.

2. **Install Mininet and Ryu Controller:**
    * Installed Mininet, a network emulator, to create a virtual network on the Ubuntu machine, enabling simulation of the SDN environment. Mininet allows for creating virtual hosts, switches, controllers, and links, facilitating testing of network configurations and protocols without physical hardware [36].
    * Installed Ryu, an open-source SDN controller framework written in Python. Ryu provides a platform for developing SDN applications and managing network flows and policies. It supports OpenFlow and other southbound protocols, enabling communication with network devices to configure the network [37].

3. **Build SDN Network:**
    * Implemented an SDN network topology similar to the CIC-DDoS2019 dataset network (see Figure 4).
    * Designed two separate networks:
        * **Victim-Network:** Consists of devices connected to a Ryu controller via a switch, simulating benign behaviors.
        * **Attack-Network:** A separate infrastructure used to execute various DDoS attacks.
    * Utilized the OpenFlow 1.3 protocol for compatibility with the Ryu controller and to enable connectivity between hosts.

4. **Ingest CIC-DDoS2019 PCAP Files:**
    * Ingested the CIC-DDoS2019 dataset PCAP files into the SDN network through one of the interfaces.
    * Used Wireshark, a network protocol analyzer, to capture and inspect the ingested CIC-DDoS2019 traffic (see Figure 5) [38].

5. **Capture OpenFlow Statistics:**
    * Developed a Python script to capture statistics from the Ryu controller's REST API.
    * Utilized the Ryu REST API to gather flow, port, and switch description statistics [39].
    * Processed and saved the collected data for further analysis.

6. **Parse Captured Traffic Statistics:**
    * Parsed the captured traffic statistics, which include time series data for each switch, port, and flow.
    * Extracted high-level metrics such as packet counts, byte counts, flow durations, entropy, and CPU usage.

7. **Save Extracted Features in CSV Files:**
    * Saved the parsed features in CSV file format (`networkstats.csv`) for subsequent analysis and use in deep learning models for DDoS detection.
The data was collected in a controlled SDN environment using Mininet and POX controller.  DDoS attacks were generated using a variety of tools, including hping3 and Slowloris. Network traffic was captured using tcpdump and labeled using CICFlowMeter. The data collection period spanned from [Start Date] to [End Date].

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


## License

This dataset is licensed under the [Mohamed-A-Elshafey] license. See the LICENSE file for details.
