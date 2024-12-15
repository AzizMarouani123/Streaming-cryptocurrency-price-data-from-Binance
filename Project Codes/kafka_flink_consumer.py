# Import necessary libraries from PyFlink and standard Python modules
from pyflink.datastream import StreamExecutionEnvironment  # For managing the Flink streaming environment
from pyflink.datastream.connectors import FlinkKafkaConsumer  # For consuming data from Kafka
from pyflink.common.serialization import SimpleStringSchema  # For deserializing Kafka messages as strings
from pyflink.common.windowing import Time  # For defining time-based windows in the stream
from pyflink.datastream.functions import ProcessAllWindowFunction  # For processing elements in a window
from pyflink.datastream.state import ValueStateDescriptor  # For managing state in Flink
from pyflink.common.typeinfo import Types  # For specifying types
from pyflink.datastream.formats import CsvTableSink  # For writing the output in CSV format
import json  # For parsing JSON data
import csv  # For writing data to CSV files
import os  # For file handling

# Define the output CSV file name where the processed data will be saved
OUTPUT_FILE = "financial_data.csv"

# Function to write the processed data into a CSV file
def write_to_csv(file_name, data):
    file_exists = os.path.isfile(file_name)  # Check if the file already exists
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Only add the header if the file is new
        if not file_exists:
            writer.writerow(["symbol", "price", "timestamp"])  # Writing the header row
        writer.writerows(data)  # Writing the data to the CSV

# Define a custom window function to process the data inside each window
class MyWindowFunction(ProcessAllWindowFunction):
    def process(self, context, elements):
        results = []  # List to hold the processed results
        # Iterate over all the elements in the window
        for element in elements:
            # Extract relevant data and append to results list
            results.append([element["symbol"], element["price"], element["timestamp"]])
        # Write the results to the CSV file
        write_to_csv(OUTPUT_FILE, results)

# Main function to process the stream of data
def process_stream():
    # Create the Flink execution environment
    env = StreamExecutionEnvironment.get_execution_environment()

    # Configure the Kafka consumer to listen to the 'binance_prices' topic for real-time data
    kafka_consumer = FlinkKafkaConsumer(
        topics='test',
        value_deserialization_schema=SimpleStringSchema(),  # Deserialization schema to convert Kafka messages into strings
        properties={
            'bootstrap.servers': 'localhost:9092',  # Kafka server address (adjust for your setup)
            'group.id': 'flink_group'  # Kafka consumer group id (adjust for your setup)
        }
    )

    # Add the Kafka consumer as the source of the data stream
    data_stream = env.add_source(kafka_consumer)

    # Function to parse the incoming JSON data
    def parse_json(value):
        return json.loads(value)  # Convert the JSON string into a Python dictionary

    # Apply the parse_json function to each element in the stream to parse the incoming JSON messages
    parsed_stream = data_stream.map(parse_json)

    # Apply a sliding time window to the stream (window size = 10 minutes, slide every 1 minute)
    windowed_stream = parsed_stream.time_window_all(
        Time.minutes(10),  # Define the length of the window (10 minutes in this case)
        Time.minutes(1)    # Define the sliding interval (1 minute)
    )

    # Process the data in each window using the custom window function and write the results to the CSV file
    windowed_stream.process_all(MyWindowFunction())

    # Start the Flink job and begin processing the stream
    env.execute("Flink Kafka Consumer with Sliding Window")

# Main entry point of the script
if __name__ == "__main__":
    # Delete the existing output CSV file before starting to ensure a clean slate
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    # Start the stream processing function that will consume data from Kafka in real time
    process_stream()
