# 8. 21.03.2022
from collections import Counter


# Ex. 1
def get_char_count_1a(text):
    char_count_dict = {}
    for i in text:
        if i in char_count_dict:
            char_count_dict[i] += 1
        else:
            char_count_dict[i] = 1
    return char_count_dict


def get_char_count_1b(text):
    count = Counter(text)
    return count  # result will be sorted


# Ex. 2
# OOT OF PLACE dictionary comprehension
def replace_dict_value(d, bad_val, good_val):
    return {k: (v if v != bad_val else good_val) for k, v in d.items()}


# Ex. 3a
# OOT OF PLACE dictionary comprehension
def clean_dict_value_3a(d, bad_val):
    return {k: v for k, v in d.items() if v != bad_val}


# Ex. 3b
# OOT OF PLACE dictionary comprehension
def clean_dict_values_3b(d, bad_list):
    return {k: v for k, v in d.items() if v not in bad_list}


# IN PLACE (3a & 3b)
def clean_dict_values_3a_inplace(d, bad_val):
    new_dic = d.copy()
    for k, v in dict(new_dic).items():
        if v == bad_val:
            del new_dic[k]
    return new_dic


def clean_dict_values_3b_inplace(d, bad_list):
    for k, v in d.copy().items():
        if v in bad_list:
            del d[k]
    return d


print("\n___________Exercise 1  ________________\n")
print(get_char_count_1a("hubba bubba"))
print(get_char_count_1a("Hubba Bubba".lower()))
print(get_char_count_1a([1, 2, 3, 3, 3, 3, 4, 4, 55, 55, 55, 6, 5, 55, 5, 55]))

print(get_char_count_1b("hubba bubba"))
print(dict(get_char_count_1b("hubba Bubba".lower())))  # without counter printed

print("\n___________Exercise 2  ________________\n")
print(replace_dict_value({'a': 5, 'b': 6, 'c': 5}, 5, 10))

print("\n___________Exercise 3  ________________\n")
print(clean_dict_value_3a({'a': 5, 'b': 6, 'c': 5}, 5))
print(clean_dict_values_3b({'a': 5, 'b': 6, 'c': 5, 'd': 3}, [3, 4, 5]))
print(clean_dict_values_3a_inplace({'a': 5, 'b': 6, 'c': 5}, 5))
print(clean_dict_values_3b_inplace({'a': 5, 'b': 6, 'c': 5, 'd': 3}, [3, 4, 5]))
