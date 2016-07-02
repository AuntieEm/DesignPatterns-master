#one lined comments
'''
multi line comments
doc strings
'''

first_name = "Kermit"
last_name = "De Frog"
#print first_name

#collect info from the user

#response = raw_input("Enter your name:  ")
#print response
#print "Hello there," ,response

birth_year = 1993
current_year = 2016
age = current_year - birth_year
#print age

#assignment operators don't exist in python (no ++)
# + - / * % =  += *= /= -=

#age = age + 3
#age = +=3

#print "You are " + str(age) + " years old."
#convert strings into numbers
#int(var)

#conditional statements
budget = 90
if budget > 100:
    brand = "nike"
    #print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 50:
    #print "We can at least get some generic sneakers."
    pass
else:
    #print "No cool shoes for me."
    pass


#arrays
characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters
#print characters [0]

#dictionary
movies = dict() #create dictionary object
#star wars is the "key" darth vader is the "value" that the key points to
movies = {"Star Wars":"Darth Vader", "Slience of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]


#loops
#while loop
i = 0
while i<9:
    #print "The count is", i
    i = i+1

#for loop
for i in range(0,10):
    #print "The count is", i
    i = i+1

#for each loop
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    #print r
    #print "One of the best rappers is " + r
    pass



#functions - Def=definition

def calcArea(h, w):
    area = h * w
    #print area
    return area
#call the function (or invoke it aka invokaiton)
a = calcArea(20, 40);
#print a
#print "My area is " + str(a) + "sqft."

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message = message.format(**locals())
print message