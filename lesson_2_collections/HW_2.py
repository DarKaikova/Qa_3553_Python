'''def print_list_reverse(lst):
    if lst is None or lst == [] or type(lst) != list:
        return 'Wrong list'
    return lst[::-1]


print(print_list_reverse([1, 2, 3, 4, 5]))
print(print_list_reverse([]))
print(print_list_reverse(223))

def is_valid_point(point):
    if point is None or point == ():
        return None
    elif type(point) != tuple or len(point) != 2 or not(all(isinstance(x, (int, float)) for x in point)):
        return False
    return True

print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))

def print_sublist_reverse(lst, start, finish):
    new = []
    if lst is None or lst == [] or type(lst) != list:
        return 'Wrong args'
    elif (type(start) != int or type(finish) != int) or start < 0 or finish >= len(lst) or start >= finish:
        return 'Wrong args'
    for i in range(finish, start - 1, -1):
        new.append(lst[i])
    return lst[:start] + new + lst[finish + 1:]


print(print_sublist_reverse([10, 20, 30, 40, 50, 60],1, 3))
print(print_sublist_reverse([1, 2, 3], "0", 2))'''




def get_students_by_grade(students):
    if students is None or students == {} or type(students) != dict:
        return {}
    new_dict = {}
    for key, val in students.items():
        new_dict.setdefault(val, []).append(key)

    return new_dict



st1 = {"Alice": 90,
      "Bob": 85,
      "Diana": 90,
      "Charlie": 85}

st2 = None
st3 = {}
print(get_students_by_grade(st1))
print(get_students_by_grade(st2))
print(get_students_by_grade(st3))








