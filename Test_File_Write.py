import sys

f = open("TestPyWrite.txt", mode="wt", encoding="utf-8")

f.writelines(
    "This is a test from the pyCharms Editor" '\n'
    "I wonder if this will work, " '\n'
    "or will I just look stupid?" '\n')

f.close()

g = open("TestpyWrite", mode="rt", encoding="utf-8")

g.close()





