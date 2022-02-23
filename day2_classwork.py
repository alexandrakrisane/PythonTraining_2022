# 23.02.2022
import datetime

print("___________Exercise 1 ________________")
usr = input("Enter your username: ")
print(f"username {usr} is saved ")
age = int(input(f"Enter your age in full years, {usr}: "))
print(f"{usr}'s age is {age} full years")

century = 100
till_hundred = century - age

if till_hundred > 0:
    print(f"{usr} will be 100 years old in {till_hundred} years")
else:
    print(f"{usr} is already at least {century} years old")

this_year = int(2022)
century_old1 = this_year + till_hundred
print(f"{usr} will be 100 years old in the year of {century_old1}")

currentYear = datetime.datetime.now().year
century_old2 = currentYear + till_hundred
print('{} will be 100 years old in the year of {}'.format(usr, century_old2))



print("\n___________Exercise 2 ________________")

width = float(input(f"Enter width of the room in meters: "))
length = float(input(f"Enter length of the room in meters: "))
height = float(input(f"Enter height of the room in meters: "))
# Right Rectangular Prism	V=LWH
room_volume = round((width * length * height),2)
print(f"Room volume is {room_volume}m\u00B3\n")

# or:
room_volume2 = width * length * height
print('Room volume is {:.2f}m\u00B3'.format(room_volume2))



print("\n___________Exercise 3 ________________")
# Celsius to Fahrenheit
prec = 3 # precision
t_celsius = float(input("Enter some temperature in Celsius: "))
t_fahrenheit = 32 + t_celsius * (9 / 5)
print(f"Temperature in Celsius is {t_celsius:.2f}\u2103. \nTemperature in Fahrenheit is {t_fahrenheit:.2f}\u2109.")

print('\nSecond rounding option:')
t_celsius_rounded = round(t_celsius, prec)
t_fahrenheit_rounded = round(t_fahrenheit, prec)
print(f"Temperature {t_celsius_rounded}\u2103 will be {t_fahrenheit_rounded}\u2109 Fahrenheit")
print(f"Temperature in Celsius is {t_celsius_rounded}\u2103.\nTemperature in Fahrenheit is {t_fahrenheit_rounded}\u2109.")
