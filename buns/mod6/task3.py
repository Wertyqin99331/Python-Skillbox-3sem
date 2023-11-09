def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num


def armstrong_generator():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1
