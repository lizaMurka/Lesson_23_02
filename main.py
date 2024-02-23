import random

try:
    numbers = random.sample(range(-10, 11), 10)

    sum_negative = 0
    for number in numbers:
        if number < 0:
            sum_negative += number
    print(f"Sum of negative numbers: {sum_negative}")

    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
    print(f"Sum of even numbers: {sum_even}")

    sum_odd = 0
    for number in numbers:
        if number % 2 != 0:
            sum_odd += number
    print(f"Sum of odd numbers: {sum_odd}")

    product_multiples = 1
    for number in range(len(numbers)):
        if number % 3 == 0:
            product_multiples *= numbers[number]

    print(f"Product of elements with multiple indices 3: {product_multiples}")

    min_value = min(numbers)
    max_value = max(numbers)
    product = 1

    for number in range(len(numbers)):
        if min_value < numbers[number] < max_value:
            product *= numbers[number]

    print(f"Product of elements between minimum and maximum: {product}")

    first_positive_index = -1
    last_positive_index = -1
    for number in range(len(numbers)):
        if numbers[number] > 0:
            if first_positive_index == -1:
                first_positive_index = number
            last_positive_index = number

    sum_between_positive = 0
    if first_positive_index != -1 and last_positive_index != -1:
        for number in range(first_positive_index + 1, last_positive_index):
            sum_between_positive += numbers[number]
    print(f"Sum of the elements between the first and last positive elements: {sum_between_positive}")


except TypeError as error:
    print(f"Not all items in the list are integers: {error}")
except Exception as error:
    print(f"An error occurred: {error}")
