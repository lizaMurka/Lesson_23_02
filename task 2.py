import random

try:
    list_num = random.sample(range(-10, 11), 10)

    even = []
    odd = []
    negative = []
    positive = []

    for num in list_num:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if num < 0:
            negative.append(num)
        else:
            positive.append(num)

    print("List of even numbers:", even)
    print("List of odd numbers:", odd)
    print("List of negative numbers:", negative)
    print("List of positive numbers:", positive)

except Exception as error:
    print("An error occurred:", error)

