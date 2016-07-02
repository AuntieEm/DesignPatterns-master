#start 3:23am july 2
#pause 5:11am july 2
#restart 7:15am july 2
#pause
#restart
#end

print "Welcome to Mad Libs with Emily!"
print "Please follow the instructions below."

#array
holiday = ["Kawanza", "Groundhog Day"]

#collect numbers from user
number_one = float(input("Enter a number between 1-20:  "))
#conditional statements
if number_one > 20:
    print("You must choose a number lower than 20.")
    number_one = float(input("Enter a number between 1-20:  "))
else:
    print("Good choice.")

number_two = float(input("Enter your favorite number:  "))
number_three = float(input("Enter a number between 2-15 and greater than 2:  "))

#conditional statements
if number_three > 15:
    print("You must choose a number less than 15 and greater than 2.")
    number_three = float(input("Enter your new number here:  "))
elif number_three < 2:
    print("You must choose a number greater than 2 and less than 15.")
    number_three = float(input("Enter your new number here:  "))
else:
    print("Good choice.")

#dictionary
animals = dict()
animals = {"one":"pheasant", "two":"fox", "three":"antelope"}

#mathmatical operators
number_four = number_one + number_two
number_five = number_three * number_one

person_one = raw_input("Enter a person's name:  ")
person_two = raw_input("Enter another person's name:  ")
person_three = raw_input("Enter another person's name:  ")

#function that returns a value and has at least 2 paramaters
def happyHoliday(person):
    print("Happy Thanks Giving " + person + "!")
def run():
    happyHoliday(person_one)
    happyHoliday(person_two)
    happyHoliday(person_three)
run()


#one loop
family = ["Grandma", "Grandpa", "Aunt", "Uncle"]
for f in family:
    print "I love my " + f



#collect info from user
verb_past_one = raw_input("Enter a past tense verb:  ")
adjective_one = raw_input("Enter an adjective:  ")
transport = raw_input("Choose a mode of transportation:  ")
plural_noun_one = raw_input("Enter a plural noun:  ")
plural_noun_two = raw_input("Enter a plural noun that's nature related:  ")
family_one = raw_input("Enter a family relation:  ")
adjective_two = raw_input("Enter another adjective:  ")
greeting_one = raw_input("Enter a kind of greeting:  ")
adjective_three = raw_input("Enter another adjective:  ")
object_one = raw_input("Enter an object that can be found in your home:  ")
plural_noun_three = raw_input("Enter anothe plural noun:  ")
plural_noun_four = raw_input("Enter another plural noun:  ")
family_two = raw_input("Enter another type of family member:  ")
sport_one = raw_input("Enter your favorite sport:  ")
exclamation_one = raw_input("What do you shout when you're upset at an event:  ")
noun_one = raw_input("Enter a noun:  ")
food_one = raw_input("What is your favorite food:  ")
noun_two = raw_input("Enter another noun:  ")
noun_three = raw_input("Enter another noun:  ")
adjective_four = raw_input("Enter another adjective:  ")
family_three = raw_input("Enter another family relation:  ")
trick = raw_input("Whats a crazy trick you can do:  ")



madlib = '''
THANKSGIVING MAD LIBS

Today we are celebrating ''' + holiday [0] + ''' dinner with the whole family
at {person_one}'s House. Earlier today we all {verb_past_one}
into the {adjective_one} {transport} and drove over the {number_one}
{plural_noun_one} and through the {plural_noun_two} to get here. Once we arrived,
my {family_one} greeted us with a big {adjective_two}
{greeting_one}. {person_two} is also here and really made sure
things were looking {adjective_three}. They had decorated the {object_one}
with {number_two} {plural_noun_three}. It was all so very festive! Now we are just
waiting for the ''' + animals["one"] + ''' to come out of the oven. I always eat my
''' + animals["two"] + ''' with a side of mashed {plural_noun_four}.
My {family_two} is watching {sport_one} on TV. They
always shout {exclamation_one} when their team scores a {noun_one}.
Horray! Only {number_three} more minutes until the {food_one} will be
ready to eat. Don't forget to save room for dessert. My grandma makes the best
{noun_two} pies. They smell like {noun_three}. I'm so full now I
feel like an {adjective_four} ''' + animals["three"] + '''! Happy ''' + holiday [1] + '''!
I hope I get to come back here for the next ''' + str(number_four) + ''' years.
I wish I could have been here ''' + str(number_five) + ''' years ago when {family_three} {person_three}
did that crazy {trick}.


'''


madlib = madlib.format(**locals())
print madlib


