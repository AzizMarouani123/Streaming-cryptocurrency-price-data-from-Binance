# Streaming-cryptocurrency-price-data-from-Binance

# Project Overview

This project is designed to stream cryptocurrency price data from Binance via an API, process the data using **Apache Kafka** and **PyFlink**, and visualize the processed results using Python libraries like **Matplotlib** and **Seaborn**.

The flow is as follows:

1. **Kafka Producer**: Collects real-time data from the Binance API and sends it to a Kafka topic.
2. **Kafka Consumer with PyFlink**: Consumes the data from the Kafka topic, processes it with PyFlink, and stores the results in a CSV file.
3. **Data Visualization**: Loads the processed data from the CSV file and creates visualizations (histograms, bar plots, time-series trends, etc.).

This system requires a few prerequisites and setup steps for **Kafka**, **PyFlink**, and other dependencies.

---

## Requirements

To run this project, ensure you have the following Python version and libraries installed:

- **Python** 3.9 or 3.10 (due to compatibility with libraries like PyFlink)
- **Apache Kafka** (for the messaging system)
- **PyFlink** (for stream processing)
- **Other Python Libraries**:
  - `requests`
  - `json`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `time`
  - `csv`
  - `os`

You can install the required Python libraries using the following command:

```bash
pip install -r requirements.txt

