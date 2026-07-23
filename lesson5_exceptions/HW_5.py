def get_list_element(items, index):
    try:
        ind = items[index]
        return ind
    except IndexError:
        return 'Index is out of range, sorry :('

print(get_list_element([1, 2, 3, 4, 5], 2))
print(get_list_element([1, 2, 3, 4, 5], 6))

numbers = [10, 20, 30]
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))

print()


def get_user_data(user, key):
    try:
        word = user[key]
        return word
    except KeyError:
        return 'Key was not found, sorry :('


def get_user_data_2(user, key):
    try:
        result = user[key]
        return result
    except Exception as e:
        return f'KeyError, where no key as {e}'


user = {
"name": "Anna",
"age": 30
}


user_2 = {
"name": "Dan",
"age": 22
}

print(get_user_data(user, 'name'))
print(get_user_data(user, 'email'))
print(get_user_data_2(user, 'email'))

print()

def calculate_average(first_value, second_value):
    try:
        res = (float(first_value) + float(second_value)) / 2
        return res
    except ValueError:
        print(f'Value must be a number!')
    except TypeError:
        print('Invalid data type')

calculate_average("10", "20")
calculate_average("hello", "20")
calculate_average(None, 20)

print()

def read_number():
    try:
        number = int(input())
    except Exception:
        print('Invalid number')
    else:
        print('Number was entered successfully!')
    finally:
        print("Program finished")

read_number()

print()

def validate_age(age):

    age_num = int(age)

    if age_num < 0:
        raise ValueError('Age cannot be negative')
    if age_num > 120:
        raise ValueError('Age is not realistic')
    else:
        return 'Very well!'


def please_enter_your_age():
    try:
        age = input('Please, enter your age: ')
        result = validate_age(age)
        print(result)
    except ValueError as e:
        print(e)


please_enter_your_age()
