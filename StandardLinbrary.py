# import shutil
import glob
import math
import os
import random
import re
import statistics
from datetime import date

# from urllib.request import urlopen

print(os.getcwd())
# os.chdir() # change current directory
# os.system() # exec shell

# dir(os)
# help(os)

# shutil.copyfile("data.db", "archive.db")
# shutil.move("/build/executables", "installdir")

print(glob.glob("*.py"))

print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
print(re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat"))
print("tea for too".replace("too", "two"))


print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print(random.choice(["apple", "pear", "banana"]))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))


# with urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl")as response:
#     for line in response:
#         line = line.decode("utf-8")
#         if "EST" in line or "EDT" in line:
#             print(line)

now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
