🛠️ Data Pipeline Project with Kafka, Debezium & DBT
📌 Overview
This project implements a real-time data pipeline using the following technologies:

Kafka: To stream data from a source file into a Kafka topic.

Kafka Consumer: To ingest the data from the topic into a database.

Debezium: To monitor changes in the database and stream them to Kafka.

DBT (Data Build Tool): To transform and clean the data into a production-ready table.

⚙️ Technologies Used
Apache Kafka

Kafka Connect + Debezium (CDC)

PostgreSQL (or your DB)

DBT (Data Build Tool)

Python (for the producer & consumer scripts)

🔄 Pipeline Flow
File to Kafka Producer
A Python script reads data from a source file (CSV, JSON, etc.) and sends each record to a Kafka topic (raw-data-topic).

Kafka Consumer to Database
A Kafka consumer script listens to the topic and inserts the incoming records into a raw table in the database (raw_data table).

Debezium + Kafka Connect
Debezium monitors changes in the raw_data table and publishes Change Data Capture (CDC) events to a new Kafka topic (db-server.raw_data).

Kafka Connect Sink Connector (optional)
You can use Kafka Connect Sink to write CDC data to another table or a storage layer.

DBT Transformations
DBT models are used to clean and transform the raw CDC data into a clean, analytics-ready table (clean_data).
