def reverse(n: str):
    if n is None or n == '' or n.isspace() == 1:
        return "Wrong string"

    return n[::-1]


print(reverse('Shalom'))
print(reverse('   '))



def is_isr_phone_number(p: str):
    if p is None or p == '' or p.isspace() == 1:
        return None
    if p.isdigit() == True and p[0] == '0' and len(p) == 10:
        return True
    return False


print(is_isr_phone_number("0521234567"))
print(is_isr_phone_number("521234567"))
print(is_isr_phone_number("05212345a7"))
print(is_isr_phone_number(""))


def print_substring_reverse(s: str, start: int, finish: int):
    if s is None or s == '' or s.isspace() == 1 or start < 0 or finish >= len(s) or start == finish or start > finish:
        return "Wrong args"
    return s.replace(s[start:finish + 1], s[start:finish + 1][::-1])

print(print_substring_reverse('forever', 2, 4))



def get_words_reverse(s: str):
    if s is None or s == '' or s.isspace() == 1:
        return "Wrong string"
    return ' '.join(s.split(' ')[::-1])

print(get_words_reverse('Hello my nice world'))


def print_words_reverse_in_column(s: str):
    if s is None or s == '' or s.isspace() == 1:
        return "Wrong string"
    for i in s.split(' '):
        print(reverse(i))
    return None


print_words_reverse_in_column('Hello my nice world')


