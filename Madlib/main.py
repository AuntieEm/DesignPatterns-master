print "Welcome to Mad Libs with Emily!"
print "Please follow the instructions below."

#array
holiday = ["Kawanza", "Groundhog Day"]

#collect numbers from user
number_one = raw_input("Enter a number between 1-20:  ")
number_two = raw_input("Enter your favorite number:  ")
number_three = raw_input("Enter your least favorite number:  ")

#dictionary
animals = dict()
animals = {"one":"pheasant", "two":"fox", "three":"antelope"}

#mathmatical operators
number_four = 57 / 7
number_five = 33 / 11

#collect info from user
person_one = raw_input("Enter a person's name:  ")
verb_past_one = raw_input("Enter a past tense verb:  ")
adjective_one = raw_input("Enter an adjective:  ")
transport = raw_input("Choose a mode of transportation:  ")
plural_noun_one = raw_input("Enter a plural noun:  ")
plural_noun_two = raw_input("Enter a plural noun that's nature related:  ")
family_one = raw_input("Enter a family relation:  ")
adjective_two = raw_input("Enter another adjective:  ")
greeting_one = raw_input("Enter a kind of greeting:  ")
person_two = raw_input("Enter another person's name:  ")
adjective_three = raw_input("Enter another adjective:  ")
object_one = raw_input("Enter an object that can be found in your home:  ")
plural_noun_three = raw_input("Enter anothe plural noun:  ")
plural_noun_four = raw_input("Enter another plural noun:  ")
family_two = raw_input("Enter another type of family member:  ")
sport_one = raw_input("What's your favorite sport:  ")
exclamation_one = raw_input("What do you shout when you're upset at an event:  ")
noun_one = raw_input("Enter a noun:  ")
food_one = raw_input("What is your favorite food:  ")
noun_two = raw_input("Enter another noun:  ")
noun_three = raw_input("Enter another noun:  ")
adjective_four = raw_input("Enter another adjective:  ")
family_three = raw_input("Enter another family relation:  ")
person_three = raw_input("Enter another person's name:  ")
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