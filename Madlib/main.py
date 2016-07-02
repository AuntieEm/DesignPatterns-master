#collect info from user

adjective_one = raw_input("Enter an adjective:  ")
adjective_two = raw_input("Enter an adjective:  ")
room_one = raw_input("Enter a type of room:  ")
pluralnoun_one = raw_input("Enter a plural noun:  ")
pluralnoun_two = raw_input("Enter a plural noun:  ")
noun_one = raw_input("Enter a noun:  ")
noun_two = raw_input("Enter a noun:  ")
noun_three = raw_input("Enter a noun:  ")
adjective_three = raw_input("Enter an adjective:  ")
noun_four = raw_input("Enter a noun:  ")
number_one = raw_input("Enter a number:  ")
pluralnoun_three = raw_input("Enter a plural noun")
noun_five = raw_input("Enter a noun:  ")
color_one = raw_input("Enter a color:  ")
color_two = raw_input("Enter a color:  ")
living_one = raw_input("Enter something alive:  ")
person_one = raw_input("Enter person in room:  ")
person_two = raw_input("Enter person in room:  ")


madlib = '''
SELECTING A TREE

No Christmas season can be really {adjective_one} unless you have
a/an {adjective_two} tree in your {room_one}. If you live in
 a city, you will see many vacant {pluralnoun_one} filled with hundreds
 of {pluralnoun_two} for sale. If you live in the country, you can get
 your own {noun_one} right out of the forest. Go out with a/an
 {noun_two} and {noun_three}, and when you see a/an {adjective_three}
 tree you like, you can dig it up and plant it in a/an {noun_four}.
 Then you can use it for {number_one} years. To make sure your tree
 is fresh, shake the branches and see if the {pluralnoun_three} fall off onto
 the {noun_five}. And make sure the tree is very {color_one}.
 Nothing looks worse than a/an {color_two} tree. Just follow these
 directions and you can have a perfectly beautiful {living_one} in
 your front room for weeks. Remember, poems and Mad Libs are made
 by fools like {person_one}, but only {person_two} can make a tree.
'''


madlib = madlib.format(**locals())
print madlib