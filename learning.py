# this is an octhorpe--it makes a comment (line ignored by the computer)
# print("hello world")
#It makes it say howdy yall at the bottom
print("howdy y'all")
# makes it say I like typing this at the bottom
print("I like typing this.")
#it makes it say this is fun at the bottom
print("This is fun.")

# math skills demo
#This sets up all the math
print("I will not count my chickens", 2)
print("Hens: ", 25+30/6)
print("Roosters: ", 100-25*3 % 4)
print("Now I will count the eggs", 7)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(25 * 4 / 5)
#Floating points are numbers that contain floating decimal points.
print(25.00 * 4.00 / 5.00)


# Variables and some of their powers
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=space_in_a_car*cars_driven
average_passengers_per_car=passengers/cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available today.")
print("There will be",cars_not_driven,"empty cars today.")
print("we can transport",carpool_capacity,"people today.")
print("we have",passengers)

# More variables and playing with output
myname="patrick"
myage=15
myheight=67 # inches
myeyes='black'
myhair='black'
mygender="male"

print("lets talk about %s." % myname)
print("hes's %d inches tall." % myheight)
print("he's got %s eyes and %s hair."% (myeyes, myhair))
print("if i add %d and %d,i get %d."%(myage, myheight, myage+myheight))
print("he's a %s." % mygender)


