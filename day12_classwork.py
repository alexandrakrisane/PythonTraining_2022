# 12. 04.04.2022

import string

# 1a
'''write the function file_line_len(fpath), which returns the number of lines in the file
check file_line_len ("veidenbaums.txt") -> should be 971 or 972'''


def file_line_len(fpath):
    with open(fpath, 'rb') as f:  # 'rb' translates to read binary
        return len(f.readlines())


print(file_line_len("veidenbaums.txt"))

def file_line_len_2(fpath):
    f = open(fpath, "rb")
    count = 0
    for line in f:
        count += 1
    f.close()
    return count


print(file_line_len_2("veidenbaums.txt"))

# 1b
'''write the function get_poem_lines (fpath), which returns a list with only those lines that contain poetry.
So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
PS preferably use encoding = "utf-8"  '''


def get_poem_lines(fpath):
    poetry_lines = []
    with open(fpath, encoding="UTF-8") as f:
        for line in f:
            if line.strip() and not line.__contains__("***"):
                poetry_lines.append(line)
    return poetry_lines


print(len(get_poem_lines("veidenbaums.txt")))

# 1c
''' write the function save_lines (destpath, lines)
This function will store all lines into destpath file '''


def save_lines(destpath, lines):
    with open(destpath, mode="w", encoding="UTF-8") as f:
        for line in lines:
            f.write(line)
        return f.closed


# 1d
'''call save_lines with destpath being "veid_poems.txt" 
and lines being the poem lines we cleaned from 1b'''

save_lines("veid_poems.txt", get_poem_lines("veidenbaums.txt"))

# 1e
''' write the function clean_punkts (srcpath, destpath)
function will open the srcpath file, clear it from  https://docs.python.org/3/library/string.html#string.punctuation
then function will save the cleaned text into destpath
'''


def clean_punkts(srcpath, destpath):
    with open(srcpath, mode="r", encoding="UTF-8") as src_file, \
            open(destpath, mode="w", encoding="UTF-8") as dest_file:
        new_text = src_file.read()
        for p in string.punctuation:
            new_text = new_text.replace(p, "")
        dest_file.write(new_text)
        return dest_file.closed and src_file.closed

clean_punkts("veidenbaums.txt", "veidenbaums_no_punctuation.txt")


# 1f
'''  write the function get_word_usage (srcpath, destpath)
The function opens the file and finds the most frequently used wordsrecommendation to use Counter module!
assume that the words are separated by either whitespace or newline (the good old split will come in handy)
the saved list of words and frequency should be saved in destpath in the following form:
vards skaits
un 3423
es 3242
PS to test, for srcpath use the file that is poetry only and has no punctuation and also the words are all in lowercase'''