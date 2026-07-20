import csv
import json

def save_shopping_list(items):
    with open('shopping.txt', 'w', encoding='utf-8') as file:
        for item in items:
            file.write(item + '\n')


items = [
    'Milk',
    'Bread',
    'Apples',
    'Coffee'
]
save_shopping_list(items)



with open("students.csv", "w", encoding="utf-8",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(['name', 'age'])
    writer.writerow(['Anna', '21'])
    writer.writerow(['Tom', '19'])
    writer.writerow(['Kate', '22'])


def read_students(filename):
    with open('students.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'Student: {row['name']} ({row['age']})')


read_students('students.csv')




def save_profile(name, age, city):

    prof_data = {'Name': name, 'Age': age, 'City': city}

    with open("profile.json", "w", encoding="utf-8") as file:
        json.dump(prof_data, file, indent=2, ensure_ascii=False)

    with open("profile.json", "r", encoding="utf-8") as file:
        loaded_config = json.load(file)


save_profile('Maria', 30, 'Haifa')
