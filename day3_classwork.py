# 28.02.2022
print("\n___________Exercise 1 ________________\n")
body_temp = float(input("What is your temperature in \u2103? "))

if body_temp < 35:
    print("not too cold\n")
elif body_temp <= 37:
    print("all right\n")
else: print("possible fever")