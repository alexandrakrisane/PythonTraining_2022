# 28.02.2022

print("\n___________Exercise 1 ________________\n")
body_temp = float(input("What is your temperature in \u2103? "))

if body_temp < 35:
    print("not too cold\n")
elif body_temp <= 37:
    print("all right\n")
else:
    print("possible fever")




print("\n___________Exercise 2 ________________\n")

# 15% of monthly salary
# every year for service over 2 years
#
# Example1: 5 years of experience, 1000 Euro salary, the bonus will be 450 Euro.
# Example2: 1.5 years of experience, 1500 Euro salary, no bonus(0).

bonus_percent = 0.15
minimal_work_years = 2
salary = float(input("What is your monthly salary in \u20ac? "))
years_worked = float(input("how many years are you working here? "))

extra_years = years_worked - minimal_work_years

if years_worked > minimal_work_years:
    xmas_bonus = float(salary * bonus_percent * extra_years)
    print(
        f"Your Christmas bonus will be: {xmas_bonus:.2f}\u20ac")  ## without :.2f it will be like 30.0 eur, but I want 30.00 €
else:
    xmas_bonus = 0
    print("No Christmas bonus")



print("\n___________Exercise 3 ________________\n")
# Order output
# 3 numbers in ascending order - use if, elif and else

first = float(input("Input first number: "))  # 5
second = float(input("Input second number: "))  # 4
third = float(input("Input third number: "))  # 3
# set 1 = 5 4 -3 .
# set 2 = 5 2 3 .
# set 3 = 5 4 7 .
# set 4 = 5 7 3 .
# set 5 = 3 7 5 .
# set 6 = 3 4 5 .

# else if
if first < second < third:  # 3 4 5
    print(f"numbers in the ascending order are: {first}, {second}, {third}")
elif first < third < second:  # 3 7 5
    print(f"numbers in the ascending order are: {first}, {third}, {second}")
elif second < first < third:  # 5  4 7
    print(f"numbers in the ascending order are: {second}, {first}, {third} ")
elif second < third < first:  # 5 2 3
    print(f"numbers in the ascending order are: {second}, {third}, {first}")
elif third < first < second:  # 5 7 3
    print(f"numbers in the ascending order are: {third}, {first}, {second}")
elif third < second < first:  # 5 4 -3
    print(f"numbers in the ascending order are: {third}, {second}, {first}")


# # Second option: nested ifs (ugly):
# if first > second:
#     if first > third:
#         if second > third:
#             print(f"numbers in the ascending order are: {third}, {second}, {first}")
#         else:  #second <= third:  5 2 3
#             print(f"numbers in the ascending order are: {second}, {third}, {first}")
#     else:  #first < = third:   5  4  7
#         if second <= third:  # second > third is impossible in this branch
#             print(f"numbers in the ascending order are: {second}, {first}, {third} ")
# else: # first <= second
#     if second > third:  # 5  7  3
#         if first > third:
#             print(f"numbers in the ascending order are: {third}, {first}, {second}")
#         else: #  first <= third: 3 7 5
#             print(f"numbers in the ascending order are: {first}, {third}, {second}")
#     else: # second < = third 3 4 5
#         print(f"numbers in the ascending order are: {first}, {second}, {third}")