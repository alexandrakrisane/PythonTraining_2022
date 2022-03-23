# 9. 23.03.2022

import string


#  Ex.1a

# def get_min_avg_max(sequence):
#     prec = 2
#     new_tuple = tuple(sequence)
#     min_value = sorted(new_tuple)[0]
#     avg_value = round(sum(new_tuple) / len(new_tuple), prec)
#     max_value = sorted(new_tuple)[-1]
#     return min_value, avg_value, max_value

def get_min_avg_max(sequence):
    # print(type(sequence))
    prec = 2
    avg_value = round(sum(sequence) / len(sequence), prec)
    return min(sequence), avg_value, max(sequence)


#  Ex.1b
def get_min_med_max(sequence):
    new_list = sorted(sequence)           # same as sorted(list(sequence))  -> returns list
    #print(type(new_list))   # -> <class 'list'>
    min_value = min(new_list)
    max_value = max(new_list)
    middle = int(len(sequence) / 2)
    if len(sequence) % 2 == 0:
        for i in range(len(new_list)):
            if type(new_list[i]) == str:  # if string - take both middle values
                median_value = new_list[middle - 1] + new_list[middle]
            else:  # if not string, div by 2
                median_value = (new_list[middle - 1] + new_list[middle]) / 2
        # print(middle)
        # print(my_list)
        result = min_value, median_value, max_value
    # print(result)
    else:
        middle = int((len(sequence) + 1) / 2)
        median_value = new_list[middle - 1]
        result = min_value, median_value, max_value
    return result


#  Ex.2a
def get_common_elements(seq1, seq2, seq3):
    common_str = tuple(set(seq1) & set(seq2) & set(seq3))
    if len(common_str) == 0:
        common_str = "No common elements found"
    return common_str


# Ex. 2b
def get_common_elements_b(*seq):
    if len(seq) == 0:
        return ()
    return tuple(set(seq[0]).intersection(*seq[1:]))


# Ex. 3a
def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    sequence = [x.lower() for x in text if x.isalpha()]
    sequence = ''.join(sequence)
    return set(sequence) >= set(alphabet)


# Ex. 3b
a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
a_en = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram_3b(text, alphabet):
    sequence = [x.lower() for x in text if x.isalpha()]
    sequence = ''.join(sequence)
    return set(sequence) >= set(alphabet)


print("\n___________Exercise 1a  ________________\n")
print(get_min_avg_max([0, 10, 1, 9]))
print(get_min_avg_max([2, 2, 9, 9, 4, 3]))
print(get_min_avg_max((2, 2, 9)))

print("\n___________Exercise 1b  ________________\n")
# get_min_med_max ([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max ([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max ("baaac") -> ('a', 'a', 'c')
# get_min_med_max ("faaacb") -> ('a', 'ab', 'f')
print(get_min_med_max([1, 5, 8, 4, 3]))
print(get_min_med_max([2, 2, 9, 9, 4, 3]))
print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))

print("\n___________Exercise 2a  ________________\n")
print(get_common_elements("abc", ["a", "b"], ('b', 'c')))
print(get_common_elements("abc", ["d", "e"], ('f', 'c')))

print("\n___________Exercise 2b  ________________\n")
print(get_common_elements_b("abc", ["a", "b"], ('b', 'a'), "ab"))
print(get_common_elements_b("abc", ["d", "e"], ('f', 'c')))
print(get_common_elements_b())

print("\n___________Exercise 3  ________________\n")
print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("Is this a pangram?"))

print(is_pangram_3b('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv))
print(is_pangram_3b("The five boxing wizards jump quickly", alphabet=a_en))
