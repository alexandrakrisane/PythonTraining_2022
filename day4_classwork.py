# 02.03.2022

print("\n___________Exercise 1 ________________\n")

# if number divided by 5 then Fizz If divided by 7 then Buzz,
# If divided by 5 AND 7 then FizzBuzz otherwise the same number

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz", end=",")
    elif i % 5 == 0:
        print("Fizz", end=",")
    elif i % 7 == 0:
        print("Buzz", end=",")
    else:
        print(i, end=",")
    i += 1


print("\n___________Exercise 2 ________________\n")
# Christmas tree out of stars - enter height
# printout:
#   *
#  ***
# *****
# two nested loops or single loop

height = int(input("enter the height of the tree: "))
x = 1
n = height - 1

for i in range(height):
    print(' ' * n + '*' * x + ' ' * n)
    n -= 1
    x += 2


print("\n___________Exercise 3 ________________\n")
# primes - check if entered positive number is a prime number
# a prime number is the number that divides without remainder only by itself and 1
# negative integers can not be prime
# 1 is not a prime number. The number 1 has only 1 factor.
# For a number to be classified as a prime number, it should have exactly two factors

n = int(input("enter positive number: "))

if n <= 1:  # 1, 0 or negative
    print(n, "is not a prime number")
else:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")