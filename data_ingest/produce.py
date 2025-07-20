from kafka import KafkaProducer
import json

# إعداد المنتج (Producer)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# اقرأ البيانات من ملف JSON
with open('e:/big_data_pipline/student.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

# لو الملف عبارة عن قاموس كبير فيه عدة طلاب
for  student in data:
    producer.send('customer-topic', student)

producer.flush()
