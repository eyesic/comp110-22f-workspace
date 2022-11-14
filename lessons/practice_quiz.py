def odd_and_even(oldList: list[int])->list[int]:
    newlist = []
    counter = 0
    for i in oldList:
        if counter % 2 == 0 and i % 2 == 1:
            newlist.append(i)
        counter += 1
    
    return newlist


def vowels_and_threes(oldStr: str)->str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    newStr = ''
    for i in oldStr:
        if counter % 3 == 0 and i not in vowels:
            newStr += i
        if counter % 3 != 0 and i in vowels:
            newStr += i
        counter += 1
    return newStr


def average_grades(oldDic: dict[str, list[int]])->dict[str, float]:
    for key in oldDic:
        oldDic[key] = sum(oldDic[key])/(len(oldDic[key]))

    return oldDic

print(average_grades({"Bill": [75, 94,  97]}))


# 1. Global variables are limited to the scope of the function they are declared in. (T/F)
ans = False
# 2. Variables can have the same name but store different values if they are defined in a different scope. (T/F)
ans = True
# 3. Named constants should be used to store values that may change throughout the program. (T/F)
ans = False
# 4. All pytest test function names must begin with test.
ans = True
# 5. A test will pass if it does not hit a False assertion or some other type of error.
ans = True
# 6. Test functions should be written in a file with a name matching the file that the functions are defined in, followed by _test.
ans = True
# 7. When using a for...in loop, on the first line of the loop you must specify the type of the variable (variable refers to i in for i in nums). (T/F)
ans = False
# 8. In Python dictionaries, each dictionary’s value type must match its key type. (T/F)
ans = False
# 9. Writing a for...in loop on a dict loops through the keys of a dictionary. (T/F)
ans = True
# 10. The values in a dictionary cannot be changed once they are assigned. (T/F)
ans = False
# 11. Explain the similarities and differences between Python’s list and dict.
Both: str = "Can use a for in loop, live in heap, mutable, duplicate values"

Dictionaries: str = "Matched Key-Value pairs, pair with assignment opperator '=' (dict_name[key] = value), control over key type, for in gives keys"

List: str = "Index increasing by integers, add items with .append, ordered, for in loop gives items."