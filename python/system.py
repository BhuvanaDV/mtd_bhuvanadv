## 1 st program to calculate the sum of digits of a number 
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits =", sum_digits)


## 2 nd program to calculate the sum of digits of a number using pythonic way

num = input("Enter a number: ")

sum_digits = sum(int(digit) for digit in num)

print("Sum of digits =", sum_digits)

## 2 Find Smallest and Biggest Digit in a Number
num = int(input("Enter a number: "))

smallest = 9
biggest = 0

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    if digit > biggest:
        biggest = digit

    num //= 10

print("Smallest digit =", smallest)
print("Biggest digit =", biggest)


## 3  Check if a Number is Prime

num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")

## 4 Print Prime Numbers in Decreasing Order Between M and N (M < N)

m = int(input("Enter M: "))
n = int(input("Enter N: "))

for num in range(n, m - 1, -1):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)

## 5 Print Prime Digits in a Number
num = int(input("Enter a number: "))

print("Prime digits are:")

while num > 0:
    digit = num % 10

    if digit in [2, 3, 5, 7]:
        print(digit)

    num //= 10

## or

num = int(input("Enter a number: "))

print("Prime digits are:")

while num > 0:
    digit = num % 10

    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        print(digit)

    num = num // 10


## 6 Print Distinct Composite Digits in a Number
num = int(input("Enter a number: "))

printed = set()

while num > 0:
    digit = num % 10

    if digit in [4, 6, 8, 9] and digit not in printed:
        print(digit)
        printed.add(digit)

    num //= 10

## or

num = int(input("Enter a number: "))

a = b = c = d = 0

while num > 0:

    digit = num % 10

    if digit == 4 and a == 0:
        print(4)
        a = 1

    elif digit == 6 and b == 0:
        print(6)
        b = 1

    elif digit == 8 and c == 0:
        print(8)
        c = 1

    elif digit == 9 and d == 0:
        print(9)
        d = 1

    num = num // 10

## 7 Find Sum of Odd Digits in a Number
num = int(input("Enter a number: "))

sum_odd = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        sum_odd += digit

    num //= 10

print("Sum of odd digits =", sum_odd)



## 7b Find Sum of even Digits in a Number
num = int(input("Enter a number: "))

sum_even = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        sum_even += digit

    num //= 10

print("Sum of even digits =", sum_even)

## 8 Find Sum of Even Placed Digits in a Number

num = int(input("Enter a number: "))

position = 1
sum_even_place = 0

while num > 0:
    digit = num % 10

    if position % 2 == 0:
        sum_even_place += digit

    position += 1
    num //= 10

print("Sum of even placed digits =", sum_even_place)

## 9a Find Odd Placed Even Digits in a Number

num = int(input("Enter a number: "))

position = 1

print("Odd placed even digits:")

while num > 0:
    digit = num % 10

    if position % 2 == 1 and digit % 2 == 0:
        print(digit)

    position += 1
## 9b Odd Placed Odd Digits
num = int(input("Enter a number: "))

position = 1

print("Odd placed odd digits are:")

while num > 0:
    digit = num % 10

    if position % 2 != 0:
        if digit % 2 != 0:
            print(digit)

    position = position + 1
    num = num // 10

## 9c Even Placed Even Digits

num = int(input("Enter a number: "))

position = 1

print("Even placed even digits are:")

while num > 0:
    digit = num % 10

    if position % 2 == 0:
        if digit % 2 == 0:
            print(digit)

    position = position + 1
    num = num // 10

## 9d Even Placed Odd Digits
num = int(input("Enter a number: "))

position = 1

print("Even placed odd digits are:")

while num > 0:
    digit = num % 10

    if position % 2 == 0:
        if digit % 2 != 0:
            print(digit)

    position = position + 1
    num = num // 10
