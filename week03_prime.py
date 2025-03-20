is_prime = True

if number >= 2:
    for i in range(2, number):
        i = 2
    while i * i <= number:
        if number % i == 0:
            is_prime = False
        print(i, end=" ")
        i = i + 1
else:
    is_prime = False