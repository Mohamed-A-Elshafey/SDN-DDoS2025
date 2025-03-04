import requests
import pandas as pd
import time

# Ryu REST API endpoints
RYU_REST_API = 'http://localhost:8080'
FLOW_STATS_URL = f'{RYU_REST_API}/stats/flow'
PORT_STATS_URL = f'{RYU_REST_API}/stats/port'
DESC_STATS_URL = f'{RYU_REST_API}/stats/desc'

# Function to get flow statistics
def get_flow_stats():
    response = requests.get(FLOW_STATS_URL)
    flow_stats = response.json()
    data = {'n_packets': [], 'n_bytes': []}
    for dpid, flows in flow_stats.items():
        for flow in flows:
            if 'n_packets' in flow and 'n_bytes' in flow:
                data['n_packets'].append(flow['n_packets'])
                data['n_bytes'].append(flow['n_bytes'])
    return pd.DataFrame(data)

# Function to get port statistics
def get_port_stats():
    response = requests.get(PORT_STATS_URL)
    port_stats = response.json()
    data = {'port': [], 'rx_packets': [], 'tx_packets': []}
    for dpid, ports in port_stats.items():
        for port in ports:
            data['port'].append(port['port_no'])
            data['rx_packets'].append(port['rx_packets'])
            data['tx_packets'].append(port['tx_packets'])
    return pd.DataFrame(data)

# Function to get switch description statistics
def get_desc_stats():
    response = requests.get(DESC_STATS_URL)
    desc_stats = response.json()
    data = {'dpid': [], 'mfr_desc': [], 'hw_desc': [], 'sw_desc': [], 'serial_num': [], 'dp_desc': []}
    for dpid, desc in desc_stats.items():
        data['dpid'].append(dpid)
        data['mfr_desc'].append(desc['mfr_desc'])
        data['hw_desc'].append(desc['hw_desc'])
        data['sw_desc'].append(desc['sw_desc'])
        data['serial_num'].append(desc['serial_num'])
        data['dp_desc'].append(desc['dp_desc'])
    return pd.DataFrame(data)

# Capture and process statistics
flow_df = get_flow_stats()
port_df = get_port_stats()
desc_df = get_desc_stats()

# Extract features from flow statistics
flow_features = {
    'total_packets': flow_df['n_packets'].sum(),
    'total_bytes': flow_df['n_bytes'].sum(),
    'average_packets_per_flow': flow_df['n_packets'].mean(),
    'average_bytes_per_flow': flow_df['n_bytes'].mean(),
}

# Extract features from port statistics
port_features = {
    'total_rx_packets': port_df['rx_packets'].sum(),
    'total_tx_packets': port_df['tx_packets'].sum(),
    'average_rx_packets_per_port': port_df['rx_packets'].mean(),
    'average_tx_packets_per_port': port_df['tx_packets'].mean(),
}

# Extract features from switch description statistics
switch_features = {
    'total_switches': len(desc_df),
}

# Combine all features
all_features = {**flow_features, **port_features, **switch_features}

# Convert to DataFrame and save to CSV
features_df = pd.DataFrame([all_features])
features_df.to_csv('sdn_features.csv', index=False)

print("Features extracted and saved to sdn_features.csv")




