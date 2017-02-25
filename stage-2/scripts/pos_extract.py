import csv
import re


str = '<test>some text here</test> <other> more text </other> <test> even more text</test>'

m2=re.compile('<test>(.*?)</test>', re.DOTALL).finditer(str)

# creating a list of lists
lists = []
for l in lists:
    lists.append([l.start(),l.end(),l.group(1)])

# Writing output to csv
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(l)
