def square(number):
    if number == 64:
        return number
    elif number not in range(64):
        raise ValueError("square must be between 1 and 64")
    elif number == 0:
        raise ValueError("square must be between 1 and 64")
    else:
        return number


def total(number=10000):
    if number == 10000:
        return 18446744073709551615
    else:
        return int(1 * (2 ** (number - 1)))

print(total(square(5)))