def is_narcissistic_number(num):
    sum_of_powers = 0
    temp_num = num
    num_digits = 0

    # Count the number of digits in the number
    while temp_num != 0:
        num_digits += 1
        temp_num //= 10

    # Calculate the sum of each digit raised to the power of the number of digits
    temp_num = num
    while temp_num != 0:
        last_digit = temp_num % 10
        sum_of_powers += last_digit ** num_digits
        temp_num //= 10

    # Check if the number is narcissistic
    if sum_of_powers == num:
        return True
    else:
        return False


def find_narcissistic_numbers():
    num = 0
    while True:
        if is_narcissistic_number(num):
            print(num, " is a narcissistic number.")
        num += 1


if __name__ == "__main__":
    find_narcissistic_numbers()
