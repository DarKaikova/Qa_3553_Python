def create_profile(name, age=18, city = 'Unknown'):
    return {
        'name': name,
        'age': age,
        'city': city
    }


print(create_profile('Anna'))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Maria"))


def sum_even_numbers(*numbers):
    if numbers == ():
        return 0

    summ = 0
    for num in numbers:
        if num % 2 == 0:
            summ += num

    return summ



print(sum_even_numbers(1, 2, 3, 4, 5, 6))
print(sum_even_numbers(7, 9))
print(sum_even_numbers())
print()


def print_pet_info(name, **info):
    print(f"name: {name}")

    if not info:
        print("No additional information")
    else:
        for key, val in info.items():
            print(f"{key}: {val}")


print_pet_info("Lucky", age=4, color="White", breed="Spitz")
print()
print_pet_info("Lucky")


def merge_lists(*lists):
    new = []
    for list in lists:
        for i in list:
            new.append(i)

    return new


print(merge_lists([1, 2], [3], [4, 5], []))
print(merge_lists())
print(merge_lists([]))
print(merge_lists([1]))

def build_message(*words, separator=" "):
    return separator.join(words)



print(build_message('world', 'eat', 'meat', separator=' * '))
print(build_message("Hello", "world"))
print(build_message("2026", "07", "15", separator="-"))