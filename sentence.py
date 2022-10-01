from sys import prefix


print('spam eggs')
print('dosen\'t') # escape
print("dosen't")
print('"Yes," he said')
print('"Isn\'t," he said')
s = "First line. \nSecond line."
print(s) # break line
print(r'C:\some\name') # row string
print("""\
    Usage: thingy [OPTIONS]
        -h              Display this usage message
        -H              Hostname to connect to
""") # multi line
print(3 * "um" + "ium") # repeat
print("Py" "thon") # enumeration
print("カッコの中にながいながいながい文字列を"
      "入れておいて繋げてやろう")
prefix = "Py"
# print(prefix "thon") can't join variable and string
print(prefix + "thon")
# character
word = "Python"
print(word[0])
print(word[-1])
print(word[0:2]) # slice
print(word[:2] + word[2:])
print(word[4:42]) # allow range out
# word[0] = "J" immutable
print(len(word))