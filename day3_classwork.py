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


