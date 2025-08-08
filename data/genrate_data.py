from faker import Faker
import json
from random import choice, randint, uniform

fake = Faker()

def generate_data(x):
    student_data = []

    for _ in range(x):
     student = {
    'customer_id': f"VF{randint(100000, 999999)}",
    'full_name': fake.name(),
    'gender': choice(['Male', 'Female']),
    'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=70).strftime('%Y-%m-%d'),
    'national_id': fake.ssn(),
    'phone_number': fake.phone_number(),
    'email': fake.email(),
    'address': fake.address(),
    'city': fake.city(),
    'country': fake.country(),
    'plan_type': choice(['Prepaid', 'Postpaid']),
    'subscription_date': fake.date_between(start_date='-10y', end_date='-1d').strftime('%Y-%m-%d'),
    'is_active': choice([True, False]),
    'balance': round(uniform(0, 1000), 2),
    'data_usage_gb': round(uniform(0.1, 100.0), 2),
    'call_minutes': randint(0, 5000),
    'last_recharge_date': fake.date_between(start_date='-30d', end_date='today').strftime('%Y-%m-%d'),
    'preferred_language': choice(['Arabic', 'English']),
    'device_model': fake.phone_number()
}
     student_data.append(student)

    # print to console
    print(json.dumps(student_data, indent=4))

    # write to file
    with open('student.json', 'w') as fp:
        json.dump(student_data, fp, indent=4)

def main():
    number_student = 5
    generate_data(number_student)

main()
