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

## Step-by-Step Setup and Execution

### 1. Install Apache Kafka
To use Kafka, you need to have it installed on your local machine or use a cloud-based service.

#### On Local Machine (Kafka Setup)
- Download Kafka from the [official Kafka website](https://kafka.apache.org/downloads).
- Extract the files and navigate to the Kafka folder.

Start **Zookeeper** (required for Kafka):
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties

### Start the Kafka Server

To start the Kafka server:


```bash
bin/kafka-server-start.sh config/server.properties

\documentclass[a4paper,11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{listings}
\usepackage{xcolor}

% Define Bash style
\lstdefinestyle{bash}{
    language=bash,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{orange},
    showstringspaces=false,
    numbers=none
}

% Define Python style
\lstdefinestyle{python}{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{orange},
    showstringspaces=false,
    numbers=none
}

\title{Running Kafka with PyFlink and Data Visualization}
\author{}
\date{}

\begin{document}

\maketitle

\section{Run the Kafka Producer}
The Kafka producer script fetches live cryptocurrency data from Binance API and pushes the data to the Kafka topic (\texttt{test}).

\noindent \textbf{Steps to run the Kafka producer:}
\begin{enumerate}
    \item Open a terminal and navigate to your project directory.
    \item Execute the producer script:
\end{enumerate}

\begin{lstlisting}[style=bash]
python kafka_producer.py
\end{lstlisting}

\noindent This will continuously fetch data from the Binance API every 5 seconds and push it to the Kafka \texttt{test} topic.

\section{Run the Kafka Consumer with PyFlink}
The PyFlink consumer script consumes data from the Kafka \texttt{test} topic, processes the data, and writes it to a CSV file.

\noindent \textbf{Steps to execute the consumer:}
\begin{enumerate}
    \item Open a terminal and navigate to your project directory.
    \item Run the PyFlink consumer script:
\end{enumerate}

\begin{lstlisting}[style=bash]
python kafka_flink_consumer.py
\end{lstlisting}

\noindent The data will be processed and saved in \texttt{financial\_data.csv}. The script uses a sliding window (10 minutes with a slide every 1 minute) to process the data.

\section{Data Visualization}
Once the data is written to \texttt{financial\_data.csv}, you can generate visualizations. Run the following Python script to create charts and plots:

\begin{lstlisting}[style=bash]
python visualize_data.py
\end{lstlisting}

\noindent \textbf{The following visualizations will be generated:}
\begin{itemize}
    \item \textbf{Distribution of Prices:} A histogram and KDE plot showing the distribution of cryptocurrency prices.
    \item \textbf{Top 10 Symbols by Price:} A bar plot for the top 10 symbols with the highest prices.
    \item \textbf{Price Trend for a Specific Symbol:} A line plot showing the price trend for a specific symbol over time.
    \item \textbf{Price Distribution by Symbol:} A boxplot to visualize the distribution of prices for each symbol.
    \item \textbf{Time-Series Price Trends for Top Symbols:} A multi-line plot showing price trends for the top 5 symbols.
\end{itemize}

\section{Cleanup}
To remove the generated CSV file after processing, run the following command:

\begin{lstlisting}[style=bash]
rm financial_data.csv
\end{lstlisting}

\section{How the Code Works}

\subsection{Kafka Producer (\texttt{kafka\_producer.py})}
\begin{itemize}
    \item Continuously fetches cryptocurrency prices from the Binance API and sends them to Kafka.
    \item \texttt{KafkaProducer} is configured to connect to \texttt{localhost:9092}.
    \item The producer serializes the data (as JSON) and sends it to the Kafka \texttt{test} topic.
    \item The API requests the price for each trading pair in real-time, and the data is sent to Kafka in 5-second intervals.
\end{itemize}

\subsection{Kafka Consumer with PyFlink (\texttt{kafka\_flink\_consumer.py})}
\begin{itemize}
    \item The consumer listens to the Kafka \texttt{test} topic.
    \item \texttt{FlinkKafkaConsumer} consumes messages from Kafka.
    \item The messages are parsed from JSON into Python dictionaries.
    \item A sliding window of 10 minutes is applied, and every minute the data is processed.
    \item The processed data is saved in the \texttt{financial\_data.csv} file.
\end{itemize}

\subsection{Data Visualization (\texttt{visualize\_data.py})}
This script reads the \texttt{financial\_data.csv} file into a Pandas DataFrame and generates various plots:
\begin{itemize}
    \item \textbf{Histogram and KDE:} Shows the price distribution.
    \item \textbf{Bar Plot:} Displays the top 10 symbols with the highest prices.
    \item \textbf{Line Plot:} Shows price trends for a selected symbol.
    \item \textbf{Boxplot:} Illustrates the price distribution across different symbols.
    \item \textbf{Multi-line Plot:} Displays time-series trends of the top 5 symbols.
\end{itemize}

\section{Troubleshooting}
\textbf{Kafka Connection Issues:}
\begin{itemize}
    \item Ensure Kafka is running locally and that the producer and consumer scripts are pointing to the correct Kafka server (\texttt{localhost:9092}).
\end{itemize}

\textbf{Library Errors:}
\begin{itemize}
    \item Make sure you're using Python 3.9 or 3.10, as certain libraries such as PyFlink may not be compatible with other versions.
\end{itemize}

\section{Conclusion}
This project integrates Kafka, PyFlink, and Python libraries to process and visualize real-time cryptocurrency price data. The steps outlined will allow you to set up Kafka locally, stream data, process it, and generate meaningful insights using visualizations.

\section*{Screenshots of Visualizations}
\begin{itemize}
    \item \textbf{Price Distribution:}
    \item \textbf{Top 10 Symbols by Price:}
    \item \textbf{Price Trend for Symbol:}
    \item \textbf{Price Distribution by Symbol:}
\end{itemize}

\end{document}







