from faker import Faker
import json
from random import randint

fake = Faker()

def generate_data(x):
    student_data = []

    for _ in range(x):
        student = {
            'id': float(randint(1, 1000)),  
            'name': fake.name(),
            'address': fake.address(),
            'city_name': fake.city(),
            'phone': fake.phone_number(),
            'card_number': fake.credit_card_number()
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
