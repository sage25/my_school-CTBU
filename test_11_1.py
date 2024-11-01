print("Mary had a little lamb.")
print("Its fllece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("."*10) #what'd that do

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 ="B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#waht taht comma at end. try removing it do see that happens
print(end1 + end2 +end3 +end4 +end5 +end6, end =' ')
print(end7 +end8 +end9 + end10 +end11 +end12)


formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# Here's some new strange stuff, remenber type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6
""")


tabby = "\tI'm tabbed in."
persian_cat = "I'm split\nona line."
backslansh_cat = "I'm \\a \\a cat."

fat_cat = """"
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby)
print(persian_cat)
print(backslansh_cat)
print(fat_cat)


print("How old are you:",end=' ')
age = input()
print("How tall are you:",end=' ')
height= input()
print("How much do you weight:",end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} hevay.")


age1 = input("How old are you? ")
height1 = input("How tall are you? ")
weight1 = input("How much do you weight? ")

print(f"So,you're {age1} old, {height1} tall and {weight1} heavy.")