# 14.03.2022


# ex.1
# 1. The Big Result
# the sum of the 2 smallest arguments multiplied by the largest argument value
def add_mult(*numbers):
    prec = 3  # precision
    if len(numbers) >= 3:
        numbers = sorted(list(numbers))
        result = round(sum(numbers[0:2]) * numbers[-1], prec)
        print(f"({numbers[0]} + {numbers[1]}) * {numbers[-1]} = {result}")
        return result
    else:
        print("3 or more numbers needed!")


# ex.2
# 2. Palindrome
def is_palindrome(text: str):
    text = text.replace(' ', '').lower()
    return text == text[::-1]  # returns True or False (boolean)


# ex.3
# 3. City Population
"""The city has a known population p0
A percentage of population perc is added each year
Every year a certain number of delta also arrive (or leave)
We need to know when (if at all) the city will reach a population of p
Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
If p cannot be reached, then we return -1"""

def get_city_year(p0, perc, delta, p):
    years = 0
    percent = perc / 100
    px = float()  # calculated population after each year
    while px < p:
        px = p0 + (p0 * percent) + delta
        #print(px)
        if px <= p0:
            return -1
            break
        p0 = px
        years += 1
    return years




print("\n___________Exercise 1  ________________\n")
print(add_mult(-4, -7, 2, 5))  #
print(add_mult(4, 7, 5, 2, 7,-1.16789369))  #
print(add_mult(4, 7))  #

print("\n___________Exercise 2  ________________\n")
print(is_palindrome("Alus ari i ra sula"))
print(is_palindrome("ABa"))
print(is_palindrome("nava"))

print("\n___________Exercise 3  ________________\n")
print(get_city_year(1000, 2, 50, 1200)) # => 3  # ex.3
print(get_city_year(1000, 2, -50, 5000)) # => -1
print(get_city_year(1500, 5, 100, 5000))# => 15
print(get_city_year(1500000, 2.5, 10000, 2_000_000)) # => 10
print(get_city_year(10, 0.0014, 50.8964, 1200))  #  => 24