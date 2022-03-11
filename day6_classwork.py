# 6. 09.03.2022

print("\n___________Exercise 1 (a,b,c) ________________\n")
list_of_float_numbers = []
user_input = ""
avg = 0

"""  
test set:
1.1 2;3,   4,
-1,3;   0004.2  -0
"""

while user_input.lower() != "q":
    user_input = input("\nEnter few numbers, separated by space, comma or semicolon. Press 'q' to quit: ")
    list_of_numbers = user_input.replace(";", " ").replace(",", " ").split(" ")   # for input like: 1.1 2;3,   4,
    #print(list_of_numbers)
    list_of_numbers = [x.strip(",") for x in list_of_numbers if (x != "" and x != ",")]# removes extra spaces and comas if they were entered
    #print(list_of_numbers)
    if "q" not in user_input.lower():
        for item in list_of_numbers:
            list_of_float_numbers.append(float(item))
    else:
        print("Let's stop here")
        break

    avg = sum(list_of_float_numbers) / float(len(list_of_float_numbers))
    list_of_float_numbers_top3 = sorted(list_of_float_numbers, key=float)[:3]
    list_of_float_numbers_last3 = sorted(list_of_float_numbers, key=float)[len(list_of_float_numbers) - 3:]

    print(f"\nList of {len(list_of_float_numbers)} entered numbers:\n{list_of_float_numbers}")
    print(f"Average value of all {len(list_of_float_numbers)} entered numbers is:\n{avg:.3f}")
    print(f"TOP 3: {list_of_float_numbers_top3}")
    print(f"BOTTOM 3: {list_of_float_numbers_last3}")




print("\n___________Exercise 2 ________________\n")

user_input_first = int(input("Enter first number (integer): "))
user_input_last = int(input("Enter last number (integer): "))
list_of_cubes = []

if user_input_first < user_input_last:
    for i in range(user_input_first, user_input_last+1):
        cubed = i ** 3
        list_of_cubes.append(cubed)
        print(f"number {i} cubed: {cubed}")
    print(f"All cubes:{list_of_cubes}")
else:
    print("wrong range entered")




print("\n___________Exercise 3 ________________\n")

user_input_text = input("enter some text: ")

list_of_words = user_input_text.split()
list_of_reversed_words = [word[::-1] for word in list_of_words]
reversed_text = ' '.join(list_of_reversed_words).capitalize()
print(reversed_text)




print("\n___________Exercise 4 ________________\n")
# Find and output the first 20 (even better option to chose how many first primes we want) prime numbers in the
# form of the list i.e. [2,3,5,7,11...]

user_input = input("enter the number of primes you want to get: ")
list_of_primes = []
number_of_primes = int(user_input)
n = 1

while len(list_of_primes) < number_of_primes:
    n += 1
    for i in range(2, n):
        if (n % i) == 0:               #print(n, "is not a prime number")
            break
    else:
        list_of_primes.append(n)     #print(n, "is a prime number")

print(f"List of prime numbers: {list_of_primes}")