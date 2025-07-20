# 📊 Real-Time Data Pipeline with Kafka, PostgreSQL, and dbt

هذا المشروع يمثل خط معالجة بيانات متكامل (End-to-End Data Pipeline) مبني بأدوات مفتوحة المصدر.  
يهدف إلى قراءة بيانات من ملف CSV، إرسالها إلى Kafka، استهلاكها وتخزينها في قاعدة بيانات PostgreSQL، ثم تحليلها وتنظيفها باستخدام dbt.

---

## 🔧 مكونات المشروع

1. **Kafka**: وسيط الرسائل لنقل البيانات من المنتج (Producer) إلى المستهلك (Consumer).
2. **Python Producer**: يقرأ من ملف البيانات ويكتب إلى Kafka Topic.
3. **Python Consumer**: يستهلك الرسائل من Kafka ويخزنها في قاعدة البيانات.
4. **PostgreSQL**: قاعدة البيانات الوسيطة لتخزين البيانات الخام.
5. **Deepnote / dbviz**: لمعاينة البيانات والتحقق منها (اختياري).
6. **dbt**: لتنظيف وتحويل البيانات الخام إلى بيانات منظمة جاهزة للتحليل.

---

## 🔁 مسار البيانات (Pipeline Flow)

CSV File
↓
Producer (Python)
↓
Kafka Topic
↓
Consumer (Python)
↓
Raw Table in PostgreSQL
↓
dbt Transformations
↓
Cleaned Table

yaml
نسخ
تحرير

---

## 📁 هيكل المشروع

project_root/
│
├── data/ # ملفات CSV الخام
│ └── source_data.csv
│
├── kafka/ # ملفات Docker لتشغيل Kafka
│ └── docker-compose.yaml
│
├── data_ingest/ # بروديوسر و كنسيومر
│ ├── produce.py
│ └── consumer.py
│
├── dbt_project/ # مشروع dbt
│ ├── dbt_project.yml
│ ├── models/
│ │ └── cleaned_data.sql
│ └── sources.yml
