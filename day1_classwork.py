# Write the following code in Python:
#
# print your name 5 times
# print Bananananana using "Ba" once and "na" 5 times
# print the number of seconds in a year calculated from months, days, minutes, seconds
# how much a googol is that is 10 to the power of the 100th
# how much will your 1000 Euro investment be worth after 12 years of 6% yearly interest?

# print your name 5 times
print('Aleksandra\n' * 5)

# print Bananananana using "Ba" once and "na" 5 times
print('Ba' + 'na' * 5)

# print the number of seconds in a year calculated from months, days, minutes, seconds (this year = 365 days)
print('number of seconds in a year calculated from months, days, minutes, seconds:')
print(60*60*24*365)

# how much a googol is that is 10 to the power of the 100th
print(10**100)

# how much will your 1000 Euro investment be worth after 12 years of 6% yearly interest?
precision = 2
print(round(1000 * 1.06**12, precision))
