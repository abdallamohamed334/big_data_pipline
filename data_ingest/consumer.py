from kafka import KafkaConsumer
import psycopg2
import json

# إعدادات Kafka
KAFKA_TOPIC = "customer-topic"
KAFKA_BROKER = "localhost:9092"

# إعدادات PostgreSQL
POSTGRES_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'mydb',
    'user': 'myuser',
    'password': 'password'
}

# الاتصال بـ PostgreSQL
def get_postgres_connection():
    return psycopg2.connect(**POSTGRES_CONFIG)

# إدخال البيانات في جدول
def insert_data_to_postgres(conn, data):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO customers ( name , address , city_name ,phone,card_number)
            VALUES ( %s,%s, %s,%s, %s)
            """,
            ( data['name'],data['address'], data['city_name'],data['phone'], data['card_number'])
        )
        conn.commit()

# إنشاء الكنسيومر
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True
)

print("Listening for Kafka messages...")

postgres_conn = get_postgres_connection()

try:
    for message in consumer:
        data = message.value
        print("Received:", data)
        insert_data_to_postgres(postgres_conn, data)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    consumer.close()
    postgres_conn.close()
