from random import sample

def get_random_password(lenght=8) -> str:
    letters_upper = [chr(i) for i in range(65, 92)]
    letters_lower = [chr(i) for i in range(97, 123)]
    nums = [str(i) for i in range(0, 10)]
    symbols = letters_upper + letters_lower + nums
    password = ''.join(sample(symbols, lenght))
    return password

print(get_random_password())
