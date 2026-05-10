# 📡 SDN-DDoS2025 Dataset & CNN-LSTM Model for DDoS Detection in SDN

[![Dataset](https://img.shields.io/badge/Dataset-SDN--DDoS2025-blue)](https://github.com/Mohamed-A-Elshafey/SDN-DDoS2025)
[![Paper](https://img.shields.io/badge/Paper-ACI--07--2025--0278.R1-green)](https://doi.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-orange)](https://python.org)

---

## 📋 Table of Contents
- [📖 Overview](#-overview)
- [🎯 Dataset Highlights](#-dataset-highlights)
- [📊 Feature Description](#-feature-description)
- [📈 Exploratory Data Analysis](#-exploratory-data-analysis)
  - [Distribution Analysis](#distribution-analysis)
  - [Constant Features](#constant-features-candidates-for-removal)
  - [Traffic-Based Analysis](#traffic-based-analysis)
  - [Correlation Analysis](#correlation-analysis)
- [🧠 Proposed CNN-LSTM Model](#-proposed-cnn-lstm-model)
- [📊 Experimental Results](#-experimental-results)
  - [Setup](#setup)
  - [Results on CIC-DDoS2019](#results-on-cic-ddos2019)
  - [Results on SDN-DDoS2025](#results-on-sdn-ddos2025)
  - [Comparative Analysis](#comparative-analysis)
  - [References for Benchmark Models](#references-for-benchmark-models)
- [💡 Key Insights](#-key-insights)
- [📚 Citation](#-citation)
- [🤝 Contributing](#-contributing)

---

## 📖 Overview

The **SDN-DDoS2025 dataset** is the **first SDN-specific** DDoS attack dataset derived from the well-known **CIC-DDoS2019** benchmark. It captures realistic network traffic in a **Software-Defined Networking (SDN)** environment.

This repository provides:
- The **SDN-DDoS2025 dataset** (39 features, both port-level and flow-level statistics).
- A comprehensive **Exploratory Data Analysis (EDA)** highlighting key attack indicators.
- A **hybrid CNN-LSTM deep learning model** achieving state‑of‑the‑art DDoS detection accuracy on both traditional and SDN networks.

> 📄 **Related publication:**  
> *"Developing Realistic Distributed Denial-of-Service (DDoS) Attack Dataset for Software-Defined Networking (SDN)"* – Applied Computing and Informatics (Manuscript ID: ACI-07-2025-0278.R1)

---

## 🎯 Dataset Highlights


| Feature               | SDN-DDoS2025                          | CIC-DDoS2019                          |
|-----------------------|----------------------------------------|---------------------------------------|
| **Environment**       | SDN (Mininet + Ryu, OpenFlow 1.3)     | Traditional network                   |
| **Attack types**      | 13 modern DDoS variants                | 13 modern DDoS variants                |
| **Total features**    | 39                                     | 88                                    |
| **Data types**        | Port-level + Flow-level statistics     | PCAP + CSV (bidirectional flows)      |
| **SDN-specific**      | ✅ OpenFlow metrics, flow rules, CPU   | ❌                                    |
| **Time component**    | ✅ Timestamp included                   | ✅ Timestamp included                   |

The dataset includes **benign traffic** and **13 DDoS attack types**: NTP, DNS, LDAP, MSSQL, NetBIOS, SNMP, SSDP, UDP, UDP-Lag, WebDDoS, SYN, TFTP, and PortScan.

---

## 📊 Feature Description

The 39 features in SDN-DDoS2025 are divided into **port statistics** (physical/logical switch health) and **flow statistics** (traffic stream behaviour). Below is the complete feature list:

| # | Feature               | Description                                      |
|---|-----------------------|--------------------------------------------------|
| 1 | `timestamp`           | ⏱️ Time of data capture                          |
| 2 | `type`                | 📋 Data type (port / flow stats)                  |
| 3 | `dpid`                | 🔌 Data path ID of the switch                    |
| 4 | `port-no`             | 🔢 Port number on the switch                     |
| 5 | `rx-packets`          | 📥 Received packets                              |
| 6 | `tx-packets`          | 📤 Transmitted packets                           |
| 7 | `rx-bytes`            | 📥 Received bytes                                |
| 8 | `tx-bytes`            | 📤 Transmitted bytes                             |
| 9 | `rx-dropped`          | ❌ Dropped received packets                      |
|10 | `tx-dropped`          | ❌ Dropped transmitted packets                   |
|11 | `rx-errors`           | ⚠️ Received packet errors                        |
|12 | `tx-errors`           | ⚠️ Transmitted packet errors                     |
|13 | `rx-frame-err`        | 🖼️ Frame errors                                  |
|14 | `rx-over-err`         | 💥 Overrun errors                                |
|15 | `rx-crc-err`          | 🔄 CRC errors                                    |
|16 | `collisions`          | 💢 Network collisions                            |
|17 | `priority`            | ⭐ Flow entry priority                           |
|18 | `idle-timeout`        | ⏳ Idle timeout value                            |
|19 | `hard-timeout`        | ⌛ Hard timeout value                            |
|20 | `byte-count`          | 📦 Bytes in flow                                 |
|21 | `packet-count`        | 📦 Packets in flow                               |
|22 | `cookie`              | 🍪 Opaque flow identifier                        |
|23 | `table-id`            | 📑 Flow table identifier                         |
|24 | `duration-sec`        | ⏱️ Flow duration (seconds)                       |
|25 | `duration-nsec`       | ⏱️ Flow duration (nanoseconds)                   |
|26 | `length`              | 📏 Flow entry length                             |
|27 | `flags`               | 🏷️ Flags associated with the flow entry          |
|28 | `actions`             | ⚡ Actions associated with the flow entry         |
|29 | `match`               | 🎯 Matching criteria for the flow entry          |
|30 | `group-id`            | 👥 Group entry ID                                |
|31 | `ref-count`           | 🔗 Reference count for the group                 |
|32 | `flow-count`          | 📊 Number of flows in the group                  |
|33 | `packet-in-count`     | 📨 Packet-in messages for the flow               |
|34 | `aggregate-packet-count`| 📊 Aggregate packet count for the flow          |
|35 | `aggregate-byte-count`| 📊 Aggregate byte count for the flow             |
|36 | `aggregate-flow-count`| 📊 Aggregate flow count for the flow             |
|37 | `cpu-util`            | 💻 CPU utilization                               |
|38 | `active-flows`        | 🔄 Number of active flows                        |
|39 | `entropy`             | 🎲 Entropy measure of traffic                    |

### 🎯 14 Key DDoS Attack Indicators

Based on EDA, these features show significant variation during attacks:

1. `rx-packets` – sudden flood of incoming packets  
2. `tx-packets` – abnormal outgoing patterns  
3. `rx-bytes` – surge in incoming data  
4. `tx-bytes` – anomalies in outgoing data  
5. `rx-dropped` – packet drops due to overload  
6. `tx-dropped` – congestion indicators  
7. `rx-errors` – errors from traffic surges  
8. `tx-errors` – transmission errors  
9. `collisions` – increase during congestion  
10. `cpu-util` – spikes during attack processing  
11. `entropy` – randomness changes in traffic  
12. `active-flows` – sudden connection increase  
13. `duration-sec` – unusual flow duration patterns  
14. `duration-nsec` – microsecond-level anomalies  

---

## 📈 Exploratory Data Analysis

We performed a thorough EDA using histograms, boxplots, and correlation matrices.

### Distribution Analysis

<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/6129e6bb-8fa9-4271-947b-244907b65416" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/5b6ec268-783f-4eb3-88ad-c52d5e4b0791" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/3f5bb88c-f219-4546-871f-6a9ccdd9cb53" />
<img width="940" height="283" alt="image" src="https://github.com/user-attachments/assets/9dc5fc4d-57dc-47cc-8372-5fbefa6a2a44" />
<img width="940" height="279" alt="image" src="https://github.com/user-attachments/assets/599a59ee-01d5-47f0-9da2-22b8c7f29f8a" />

*Boxplots and histograms of SDN traffic features in the SDN-DDoS2025 dataset. Features like rx‑packets, tx‑packets, rx‑bytes, tx‑bytes show heavily skewed distributions with extreme outliers – clear signs of volumetric DDoS attacks. CPU‑util spikes above 60% indicate resource stress.*

<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/25da091c-3e96-47d0-b159-c3bb409114de" />
<img width="940" height="282" alt="image" src="https://github.com/user-attachments/assets/ddac3ee6-8b23-41bc-873e-31d1a02157b8" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/580b8a56-744b-424c-b862-e175867662b5" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/328e3c6a-24ea-4a01-8089-66ff00688572" />

*Boxplot and histogram analysis of SDN flow duration and traffic anomalies in the SDN-DDoS2025 dataset. Duration‑sec and duration‑nsec follow near‑normal distributions but with long right tails, suggesting some flows persist longer due to attack traffic. Aggregate packet count and entropy show moderate distributions with occasional high outliers.*

### Constant Features (Candidates for Removal)

<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/c20853d7-9062-445f-9ef1-6a54dd437e01" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/c505069b-6aa7-4d7e-8786-4fd147c8666e" />

*Analysis of constant-value features in the SDNDDoS2025 dataset. Features such as priority, idle‑timeout, hard‑timeout, table‑id, and error counters remain nearly constant – they can be removed to reduce dimensionality.*

### Traffic-Based Analysis

<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/49ba5c25-b3b1-43e3-8a0e-03c79f942bc6" />
<img width="940" height="277" alt="image" src="https://github.com/user-attachments/assets/94cf5bbb-be1a-4b08-b245-378ce3b27682" />
<img width="940" height="276" alt="image" src="https://github.com/user-attachments/assets/0ef0419c-edc1-40c8-b3ce-a2783f27cce1" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/f3b1e483-e55d-44f1-896f-23de64e2141a" />
<img width="940" height="280" alt="image" src="https://github.com/user-attachments/assets/43c404f2-9bf5-4fe1-b90c-440190c72e4b" />

*Analysis of traffic-based features in the SDN-DDoS2025 Dataset. Packet count, byte count, aggregate flow count, and packet‑in count are strong signals for various attack types.*

### Correlation Analysis

<img width="940" height="781" alt="image" src="https://github.com/user-attachments/assets/2789aab2-67ce-4f75-b75a-17fd6d49c1a5" />
  
*Heatmap of 15 Features in the SDN-DDoS2025 dataset. Strong positive correlations between packet counts and byte volumes (as expected). Timestamp correlates with aggregate traffic volume, indicating increasing trends during attacks. CPU‑util negatively correlates with traffic volume – the controller becomes overwhelmed and cannot process efficiently.*

- **rx‑packets** ↔ **rx‑bytes** (0.99)  
- **tx‑packets** ↔ **tx‑bytes** (0.99)  
- **duration‑sec** ↔ **duration‑nsec** (0.95)  
- **timestamp** ↔ **aggregate‑packet‑count** (0.85)  
- **cpu‑util** ↔ **aggregate‑packet‑count** (–0.72)

Entropy shows weak correlations, suggesting it provides independent information about traffic randomness.

---

## 🧠 Proposed CNN-LSTM Model

We propose a hybrid deep learning model that combines **1D Convolutional Neural Networks (CNN)** for spatial feature extraction and **Long Short-Term Memory (LSTM)** for temporal dependency modelling.

### Architecture
<img width="1956" height="570" alt="cnn-lstm" src="https://github.com/user-attachments/assets/a43350a0-4535-4557-913c-238276acfbc0" />

*The proposed CNN-LSTM hybrid model. The model consists of initial Conv1D layers, an Inception block for multi‑scale feature extraction, an LSTM layer, and dense layers for classification.*

**Layers:**
- **Input**: features treated as timesteps.
- **Initial Conv1D**: two layers with 32 filters, kernel size 3, BatchNorm, MaxPooling, Dropout 50%.
- **Inception block**: three parallel Conv1D branches (kernel sizes 1, 3, 5), concatenated, MaxPooling, Dropout 30%.
- **LSTM**: 256 units, return_sequences=False, L2 regularization.
- **Dense layers**: two layers with 256 units, BatchNorm, ReLU, Dropout 50% (if needed).
- **Output**: single unit with sigmoid activation for binary classification.

### Hyperparameters

| Parameter                  | Value            |
|----------------------------|------------------|
| Optimizer                  | Adam             |
| Learning rate              | 5e-4             |
| Batch size                 | 64               |
| Epochs                     | 200              |
| Patience (early stopping)  | 20               |
| Loss function              | Binary Crossentropy |
| Conv1D filters             | 32               |
| LSTM units                 | 256              |
| Dense units                | 256              |
| Regularization             | L2 (0.001)       |

> The model is trained with **ReduceLROnPlateau** and **ModelCheckpoint** callbacks.

---

## 📊 Experimental Results

### Setup

- **Hardware**: Intel Core i7, 32 GB RAM, Windows 11.
- **Software**: Python 3.10, TensorFlow, Jupyter Notebook.
- **Datasets**: CIC-DDoS2019 (traditional) and SDN-DDoS2025 (SDN).

### Results on CIC-DDoS2019

The proposed CNN-LSTM model achieves near‑perfect scores on the traditional dataset, outperforming most benchmarks.

| Metrics   | CNN-BRS [1] | Bays-CNN [2] | CNN-WRS [3] | Cybernet [4] | **CNN-LSTM (ours)** |
|-----------|--------------|---------------|--------------|----------------|---------------------|
| Accuracy  | 99.99%       | 99.90%        | 95.76%       | 99.99%         | **99.98%**          |
| Recall    | 99.99%       | 98.90%        | 99.84%       | 99.99%         | **99.98%**          |
| Precision | 99.99%       | 99.70%        | 95.87%       | 99.99%         | **99.98%**          |
| F1-Score  | 99.99%       | 99.29%        | 95.95%       | 99.99%         | **99.98%**          |
| MCC       | 99.93%       | 98.59%        | 29.64%       | 99.98%         | **99.70%**          |

### Results on SDN-DDoS2025

The CNN-LSTM model significantly outperforms all benchmarks on the SDN dataset, achieving **98.02% accuracy** – an improvement of **+6.69% over CNN-BRS** and **+16.69% over CNN-WRS**.

| Metrics   | CNN-BRS [1] | Bays-CNN [2] | CNN-WRS [3] | Cybernet [4] | **CNN-LSTM (ours)** |
|-----------|--------------|---------------|--------------|----------------|---------------------|
| Accuracy  | 91.87%       | 88.26%        | 84.00%       | 93.14%         | **98.02%**          |
| Recall    | 91.86%       | 79.57%        | 93.00%       | 92.80%         | **98.01%**          |
| Precision | 93.96%       | 84.21%        | 87.00%       | 92.50%         | **98.04%**          |
| F1-Score  | 92.25%       | 81.54%        | 90.00%       | 92.60%         | **98.03%**          |
| MCC       | 94.83%       | 63.61%        | 52.11%       | 83.18%         | **94.49%**          |

### Comparative Analysis

#### Accuracy Improvements
<img width="1045" height="661" alt="image" src="https://github.com/user-attachments/assets/2c86e2b1-3e68-427d-ba16-98b4784f2046" />


On SDN-DDoS2025, CNN-LSTM improves accuracy by up to 16.69% over benchmarks.

<img width="1045" height="661" alt="image" src="https://github.com/user-attachments/assets/6cd94764-d008-4bc0-ba38-075bb7ffe5ad" />

Improvements in the detection accuracy of the proposed CNN-LSTM hybrid model relative to benchmarks on CIC-DDos2019 and SDN-DDoS2025 datasets. The proposed CNN-LSTM consistently outperforms all baselines on both datasets.

#### Cross‑Evaluation Robustness
<img width="1045" height="661" alt="image" src="https://github.com/user-attachments/assets/216e13a2-6a20-4832-883e-d6c24c476160" />

The proposed CNN-LSTM shows the smallest accuracy drop (1.96%) when moving from traditional to SDN data, demonstrating superior generalization.

### References for Benchmark Models

The benchmark models compared in the tables above are based on the following publications:

- **[1] CNN-BRS:** Najar AA, Naik SM. Cyber-secure SDN: a CNN-based approach for efficient detection and mitigation of DDoS attacks. Comput Sec. 2024; 139: 103716. [Link](https://dl.acm.org/doi/10.1016/j.cose.2024.103716)

- **[2] Bays-CNN:** AlSaleh I, Al-Samawi A, Nissirat L. Novel machine learning approach for DDoS cloud detection: Bayesian-based CNN and data fusion enhancements. Sensors. 2024; 24(5): 1418. [Link]( https://www.mdpi.com/1424-8220/24/5/1418)

- **[3] CNN-WRS:** Najar A, Naik SM. A robust DDoS intrusion detection system using convolutional neural network. Comput Electr Eng. 2024; 117: 104698. [Link](https://dl.acm.org/doi/10.1016/j.compeleceng.2024.109277)

- **[4] Cybernet:** Azar ASMB. Cybernet model: a new deep learning model for cyber DDoS attacks detection and recognition. Comput Mater Cont. 2024; 78(1): 1275-95. [Link](http://www.techscience.com/cmc/v78n1/55407)

---

## 💡 Key Insights

- **SDN-DDoS2025** is the first SDN‑native dataset derived from realistic DDoS traffic, filling a critical gap in SDN security research.
- **EDA** reveals that volumetric attacks manifest as extreme outliers in packet/byte counts and CPU spikes, while constant features (priority, timeouts) can be removed.
- The **CNN-LSTM hybrid model** excels at capturing both spatial and temporal patterns, achieving **98.02% accuracy** on SDN data.
- **Robustness**: The proposed model suffers the smallest performance drop when transitioning from traditional to SDN environments, indicating strong generalization.

---

## 📚 Citation

If you use the SDN-DDoS2025 dataset or the CNN-LSTM model in your research, please cite:

```bibtex
@article{10.1108/ACI-07-2025-0278,
    author = {Hassan, Mahmoud and Metwally, Khaled and Elshafey, Mohamed},
    title = {Developing realistic distributed denial-of-service (DDoS) attack dataset for software-defined networking (SDN)},
    journal = {Applied Computing and Informatics},
    pages = {1-23},
    year = {2026},
    month = {05},
    issn = {2634-1964},
    doi = {10.1108/ACI-07-2025-0278},
    url = {https://doi.org/10.1108/ACI-07-2025-0278},
    eprint = {https://www.emerald.com/aci/article-pdf/doi/10.1108/ACI-07-2025-0278/11577556/aci-07-2025-0278en.pdf},
}

```

Dataset available at: [https://github.com/Mohamed-A-Elshafey/SDN-DDoS2025](https://github.com/Mohamed-A-Elshafey/SDN-DDoS2025)

---

## 🤝 Contributing

Contributions are welcome! If you find issues or want to improve the dataset or models:
- 🐛 Open an issue
- 🔀 Submit a pull request
- 📧 Contact the authors

---

<div align="center">
⭐ Star this repository if you find it useful! ⭐
</div>
