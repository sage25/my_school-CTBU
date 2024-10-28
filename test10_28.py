print("Hello Worlcd!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd must rather you 'not'.")
print('I "said. do not touch this.')


#A comment ,this is so you can read your program later.
#Anything after this # is ignored by python.

print("I could have code like this .")# and the coment after is ignored

#You can also use a comment to "disable" or comment out code:
#print("This won't run.")

print("This will run.")


print("I will now count my chickens:")

print("Hens", 25 + 30 /6)
print("Roosters", 100 - 25 * 3 %4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)


cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacityc = cars_driven * space_in_car
aversge_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available.")
print("There are only",drivers , "drivers available.")
print("There will be",cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacityc ,"peopole today.")
print("We have", passengers ,"to carpool today.")
print("We need to put about", aversge_passengers_per_car, "in each car.")


my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy,")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usaually {my_teeth} depending on the coffee.")


#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} I get {total}.")


types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said:'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?{}!"
print(joke_evaluation.format(hilarious))

w = "This is the left said of..."
e = "a string with right said."

print(w + e)