# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    result = []
    for word in sentence.split():
        if len(word) > 4:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

print(spin_words("Hey fellow warriors"))

# https://www.codewars.com/kata/5a4ff3c5fd56cbaf9800003e/train/python
def without_last(lst):
    lst.pop()
     # removes the last element
    return lst

print(without_last([45, 74, 53, 98, 16, 19, 14, 50, 49]))

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
def find_outlier(integers):
    x = []
    y = []
    for i in integers:
        if  i % 2 != 0:
            x.append(i)

        else:

            y.append(i)
    return x[0] if len(x) == 1 else y[0]

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    tag = 'aAeEUuIiOo'
    x = []
    for i in string_:
        if i in tag.lower():
         string_.append(i)

        else:
            string_

    return (''.join(x))

print(disemvowel('dfewf32edc'))



def disemvowel(string_):
    tag = 'aAeEUuIiOo'
    for i in tag:
      string_ = string_.replace(i, '') # replace содержит два аргумента что заменить и на что заменить
    return string_

print(disemvowel('dfewf32edc'))




