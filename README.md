# SDN-DDoS2025

## Description

This dataset contains network traffic data captured from a software-defined networking (SDN) environment under various DDoS attack scenarios. It includes both benign traffic and a range of DDoS attacks, along with labels for each flow. This dataset is intended for researchers and practitioners in cybersecurity to develop and evaluate DDoS detection and mitigation techniques in SDN environments.

## Data Collection

The data was collected in a controlled SDN environment using Mininet and POX controller.  DDoS attacks were generated using a variety of tools, including hping3 and Slowloris. Network traffic was captured using tcpdump and labeled using CICFlowMeter. The data collection period spanned from [Start Date] to [End Date].

## Data Format

The dataset is provided in CSV format. Each row represents a network flow, with features extracted by CICFlowMeter. The features include source IP, destination IP, protocol, port numbers, packet counts, byte counts, flow duration, and other relevant metrics. The corresponding attack labels are provided in a separate 'labels.csv' file.

## Citation Information

If you use this dataset in your research, please cite it as:
[Your Name(s)], "SDN-DDoS2025 Dataset", [Year], https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository 1    



## License

This dataset is licensed under the [License Name] license. See the LICENSE file for details.
