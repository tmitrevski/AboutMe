# %%
# Activity 3
# Create a list called 'farm' with the elements "pig", "cow", "chicken", "dog", "horse", "sheep".
farm = ["pig", "cow", "chicken", "dog", "horse", "sheep"]
print(farm)
# Write an if statement that prints the string "RWAR!" if the first element of farm is NOT "Godzilla".
if farm[0] != "Godzilla":
    print("RWAR!")
# Write an else if statement that prints the string "SCREECH!" if the last element of farm is "Mothra".
if farm[5] == "Mothra":
    print("SCREECH!")
# Else, print the string "This animal is neither Godzilla nor Mothra!".
else:
    print("This animal is neither Godzilla nor Mothra!")
# Declare a variable named 'dog' with a string of "Spot".
dog = "Spot" 
# Declare 3 variables `cat`, `city`, `car` without assigning them values.
cat = None
city = None
car = None
# Assign the string "Farley" to `cat`.
cat = "farley" 
# Assign the string "San Francisco" to `city`.
city = "San Francisco"
# Assign the string "Prius" to `car`.
car = "Prius"
# Using string concatenation, print out the sentence "See Spot run!".
print("See " + dog + " run!")
# Using string concatenation, print out the sentence "I drive Farley around San Francisco in my Prius".
print("I drive " + cat + " around " + city + " in my " + car)
# Declare a variable budget and assign it a value of 5000.
budget = 5000
# Declare a variable rent_cost and assign it a value of 1500.
rent_cost = 1500
# Declare a variable utilities_cost and assign it a value of 150.
utilities_cost = 150
# Declare a variable food_cost and assign it a value of 250.
food_cost = 250
# Declare a variable transportation_cost and assign it a value of 350.
transportation_cost = 350
# Declare a variable computer_cost and assign it a value of 2000.
computer_cost = 2000
# Declare a variable called total_cost that takes the sum of all costs above (excluding budget).
total_cost = rent_cost+utilities_cost+food_cost+transportation_cost+computer_cost
# Write an if statement that checks whether the sum of all our costs is within the budget.
if total_cost <= budget:
    print("Your total cost is: " + str(total_cost))
else:
    print("You're over budget by: " + str(budget-total_cost))
# If so, print "You're total cost is " concatentated with the `total_cost` variable.
# Else, print "You're over budget by " concatenated with the difference between `budget` and `total_cost`.
# Write an if statement that checks whether the rent_cost is larger than the sum of the `utilities_cost`, `food_cost`,
if rent_cost > utilities_cost+food_cost+transportation_cost:
    print("The rent is too damn high!")
else:
    print("Ahh just right!")
# and `transportation_cost`. If so, print a string that says "The rent is too damn high!".
# Else, print a string that says "Ahhh just right!"
# %%

######################
# Create Character One
######################

# Make a variable called `c1_name` and have it equal a string of "Mr. Farley".
c1_name = "Mr. Farley"

# Make a variable called `c1_age` and have it equal to an integer of 65.
c1_age = 65

# Make a variable called `c1_profession` and have it equal to "Web Developer".
c1_profession = "Web Developer"

# Make a variable called `c1_salary` and have it equal to 100000.
c1_salary = 100000

# Make a variable called `c1_species` and have it equal to "cat".
c1_species = "cat"

# Make a variable called `c1_location` and have it equal to "San Francisco, CA".
c1_location = "San Francisco, CA"

# Make a variable called `c1_monthly_rent` and have it equal to 2000.
c1_monthly_rent = 2000

# Make a variable called `c1_monthly_expenses` and have it equal to 1500.
c1_monthly_expenses = 1500

# Make a variable called `c1_yearly_rent` and have it equal to `c1_monthly_rent` * 12.
c1_yearly_rent = c1_monthly_rent*12

# Make a variable called `c1_yearly_expenses` and have it equal to 1500.00 * 12
c1_yearly_expenses = 1500.00 * 12

# Make a variable called `c1_savings` and have it equal to `c1_salary` - (`c1_yearly_rent` + `c1_yearly_expenses`)
c1_savings = c1_salary - (c1_yearly_rent + c1_yearly_expenses)


######################
# Create Character Two
######################

# Make a variable called `c2_name` and have it equal a string of "Mr. Snuggles".
c2_name = "Mr. Snuggles"

# Make a variable called `c2_age` and have it equal to an integer of 30.
c2_age = 30

# Make a variable called `c2_species` and have it equal to "mouse".
c2_species = "mouse"

# Make a variable called `c2_profession` and have it equal "Accountant"
c2_profession = "Accountant"

# Make a variable called `c2_salary` and have it equal to 70000.
c2_salary = 70000

# Make a variable called `c2_location` and have it equal to "Oakland, CA".
c2_location = "Oakland, CA"

# Make a variable called `c2_monthly_rent` and have it equal to 4000.
c2_monthly_rent = 4000

# Make a variable called `c2_monthly_expenses` and have it equal to 500.
c2_monthly_expenses = 500

# Make a variable called `c2_yearly_rent` and have it equal to `c2_monthly_rent` * 12.
c2_yearly_rent = c2_monthly_rent * 12

# Make a variable called `c2_yearly_expenses` and have it equal to `c2_monthly_expenses` * 12.
c2_yearly_expenses = c2_monthly_expenses * 12

# Make a variable called `c2_savings` and have it equal to `c2_salary` - (`c2_yearly_rent` + `c2_yearly_expenses`)
c2_savings = c2_salary - (c2_yearly_rent + c2_yearly_expenses)

##############
# Conditionals
##############

# Write an if-else statement to check if `c1_name` is equal to "Mr. Farley". If so, print a string of "Hello Mr. Farley" using the `c1_name` variable. If not, print a string of "Hello stranger".
if c1_name == "Mr. Farley":
    print("Hello " + c1_name)
else:
    print("Hello stranger.")

# Write an if-else statement to check if `c2_age` is greater than `c1_age`. If so, print a string of "Mr. Farley is older than Mr. Snuggles". Else if `c1_age` is greater than `c2_age`, print a string of "Mr. Snuggles is older than Mr. Farley". Else, `c1_age` must have to be equal to `c2_age`, therefore print a string of "Mr. Farley is the same age as Mr. Snuggles".
if c2_age > c1_age:
    print("Mr. Farley is older than Mr. Snuggles")
elif c1_age > c2_age:
    print("Mr. Snuggles is older than Mr. Farley")
else:
    print("Mr. Farley is the same age as Mr. Snuggles")

# Write an if-else statement to check if `c1_location` is equal to "Oakland, CA". If so, print a string of "Mr. Farley comes from the home of the Raiders!". Else if `c1_location` is equal to a string of "San Francisco, CA", print a string of "Mr. Farley comes from the home of the 49ers!". Else both conditions must not apply and therefore print a string "Mr. Farley doesn't hail from a sports town."
if c1_location == "Oakland, CA":
    print("Mr. Farley comes from the home of the Raiders!")
elif c1_location == "San Francisco, CA":
    print("Mr. Farley comes from the home of the 49ers!")
else:
    print("Mr. Farley doesn't hail from a sports town.")
# Write an if-else statement to check if `c1_monthly_rent` is greater than `c2_monthly_rent`. If so, print a string of "Mr. Farley pays more rent than Mr. Snuggles". Else if `c1_monthly_rent` is less than `c2_monthly_rent`, print a string of "Mr. Farley pays less rent than Mr. Snuggles". Else, `c1_monthly_rent` must have to be equal to `c2_monthly_rent`, therefore print a string of "Mr. Farley pays the same rent as Mr. Snuggles".
if c1_monthly_rent > c2_monthly_rent:
    print("Mr. Farley pays more rent than Mr. Snuggles")
elif c2_monthly_rent > c1_monthly_rent:
    print("Mr. Farley pays less rent than Mr. Snuggles")
else:
    print("Mr. Farley pays the same rent as Mr. Snuggles")

# Write an if-else statement to check if `c1_monthly_expenses` is greater than `c2_monthly_expenses`. If so, print a string of `Mr. Farley has more expenses than Mr. Snuggles`. Else if `c1_monthly_expenses` is less than `c2_monthly_expenses`, print a string of "Mr. Farley pays less expenses than Mr. Snuggles". Else, `c1_monthly_expenses` must have to be equal to `c2_monthly_expenses`, therefore print a string of "Mr. Farley pays the same expenses at Mr. Snuggles".
if c1_monthly_expenses > c2_monthly_expenses:
    print("Mr. Farley has more expenses than Mr. Snuggles")
elif c1_monthly_expenses < c2_monthly_expenses:
    print("Mr. Farley has less expenses than Mr. Snuggles")
else:
    print("Mr. Farley pays the same expenses as Mr. Snuggles")
# Write an if-else statement to check if `c1_profession` is equal to "Web Developer" AND `c2_profession` is equal to "Accountant". If so, print a string of "Look a Web Developer and an Accountant", else print a string of "They are professionals."
if c1_profession == "Web Developer" and c2_profession == "Accountant":
    print("Look a Web Developer and an Accountant.")
else:
    print("They are professionals.")

# %%
# Declare a variable `welcome_name` as an input with a string of "Welcome to the sandwich shop, what do I call you? ".
welcome_name = input("Welcome to the sandwich shop, what do I call you? ")

# Then print the string "Hello" concatenated with the variable `welcome_name`.
print("Hello " + welcome_name)

# Declare a variable `question_sandwich` as an input with a string of "Are you here for a sandwich? (Y/N) ".
question_sandwich = input("Are you here for a sandwich? (Y/N) ")

# If `question_sandwich` is equal to "Y" or "y" declare a variable `food_prompt` as an input with a string of "What kind of sandwich would you like?".
if question_sandwich == "Y" or question_sandwich == "y":
    food_prompt = input("What kind of sandwich would you like?")
# Then print a string of "Please wait 10 min for your " concatenated with the variable `food_prompt`.
    print("Please wait 10 min for your " + food_prompt + " sandwich.")
# Else If `question_sandwich` is "N" or "n", print a string of "If you don't want a sandwich what are you here for?!".
elif question_sandwich == "N" or question_sandwich == "n":
    print("If you don't want a sandwich, what are you here for?!")
# Else print a string of "You did not write Y or N!"
else:
    print("You did not write Y or N!")
# %%
# Declare a variable of `name` with an input and a string of "Welcome to the Boba Shop! What is your name?".
name = input("Welcome to the Boba Shop! What is your name? ")

# Check if `name` is not an empty string or equal to `None`.
if name != '':
    # If so, write a print with a string of "Hello" concatenated with the variable `name`.
    print("Hello "+ name)

    # Then, declare a variable of `beverage` with an input and a string of "What kind of boba drink would you like?".
    beverage = input("What kind of boba drink would you like? ")

    # Then, Declare a variable of `sweetness` with an input and a string of "How sweet do you want your drink: 0, 50, 100, or 200?".
    sweetness = input("How sweet do you want your drink: 0, 50, 100, or 200? ")

    # If `sweetness` equals 50 print "half sweetened".
    if sweetness == "50":
        print("half sweetened")
    # Else if `sweetness` 100 print "normal sweet".
    elif sweetness == "100":
        print("normal sweet")
    # Else if `sweetness` 200 print "super sweet".
    elif sweetness == "200":
        print("super sweet")
    # Else print with a string of "non-sweet".
    else:
        print("non-sweet")

    # Then print the string of "Your order of " concatenated with the variable `beverage`, concatenated with " boba with a sweet level of ", concatenated with the variable `sweetness`
    print("Your order of " + beverage + " boba with a sweet level of " + sweetness)
# Else, print the string of "You didn't give us your name! Goodbye"
else:
    print("You didn't give us your name! Goodbye")
# %%
# Create a list, `list_1`,  with `0`, `1`, `2`, `3` as values.
list_1 = [0, 1, 2, 3]

# Create a list, `list_2` with `4`, `5`, `6`, `7` as values.
list_2 = [4, 5, 6, 7]

# Create a list, `list_3` with `8`, `9`, `10`, `11` as values.
list_3 = [8, 9, 10, 11]

# Create a list, `list_4` with `12`, `13`, `14`, `15` as values.
list_4 = [12, 13, 14, 15]

# Print the 3rd index of `list_1`.
print(list_1[2])

# Print the 1st index of `list_2`.
print(list_2[0])

# Print the 2nd index of `list_3`.
print(list_3[1])

# Print the 4th index of `list_4`.
print(list_4[3])
# %%

# san_francisco = {
#     "west_coast": True,
#     "has_multiple_bridges": True,
#     "known_for_pizza": False,
#     "coastal": True,
#     "snows": False,
#     "very_hot": False,
#     "mayor": "London Breed",
#     "state": "California",
#     "country": "USA",
#     "best_food": "burritos",
#     "sports_teams": ["Giants", "Warriors", "Forty-Niners"],
#     "tallest_building": "SalesForce Building",
#     "population": 884363,
#     "city_size": "large",
#     "median_house_price": 1610000,
#     "famous_residents": ["Maya Angelou", "Robert Frost", "Carlos Santana"],
#     "homeless_pop": 1150,
#     "political_leaning": "Democrat",
#     "notable_attractions": ["Alcatraz", "Golden Gate Bridge", "Fisherman's Wharf"],
#     "natural_disasters": ["Earthquakes"],
# }

# Re-create the content of the commented out `san_francisco` dictionary by using bracket notation to manually add each of the key-value pairs (including nested objects).

san_francisco = {}
san_francisco["west_coast"] = True
san_francisco["has_multiple_bridge"] = True
san_francisco["known_for_pizza"] = False
san_francisco["coastal"] = True
san_francisco["snows"] = False
san_francisco["very_hot"] = False
san_francisco["mayor"] = "London Breed"
san_francisco["state"] = "California"
san_francisco["country"] = "USA"
san_francisco["best_food"] = "burritos"
san_francisco["sports_teams"] = ["Giants", "Warriors", "Forty-Niners"]
san_francisco["tallest_building"] = "SalesForce Building"
san_francisco["population"] = 884363
san_francisco["city_size"] = "large"
san_francisco["median_house_price"] = 1610000
san_francisco["famous_residents"] = ["Maya Angelou", "Robert Frost", "Carlos Santana"]
san_francisco["homeless_pop"] = 1150
san_francisco["political_leaning"] = "Democrat"
san_francisco["notable_attractions"] = ["Alcatraz", "Golden Gate Bridge", "Fisherman's Wharf"]
san_francisco["natural_disasters"] = ["Earthquakes"]
# Print the manually modified `san_francisco` dictionary and confirm the contents match the commented out version.
print(san_francisco)
# %%
# Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file
from show_data import shows

# QUESTION 1: Who is the actor that plays Squidward in Spongebob (kids)?
print(shows["genre"]["kids"]["Spongebob"]["cast"][3]["actor"])

# QUESTION 2: Patrick Warburton plays Joe Swanson in Family Guy (comedy). What is the link to his imdb page?
print(shows["genre"]["comedy"]["family_guy"]["cast"][4]["imdb"])

# QUESTION 3: Is the Walking Dead still running?
print(shows["genre"]["drama"]["the_walking_dead"]["still_running"])

# QUESTION 4: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
# HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
print(shows["genre"]["drama"]["dexter"]["cast"][0]["actor"], shows["genre"]["kids"]["dexters_lab"]["cast"][0]["actor"])

# QUESTION 5: Who are the creators of Stranger Things (drama)?
for i in shows["genre"]["drama"]["stranger_things"]["creators"]:
    print(i)

# QUESTION 6: Who hosts the Daily Show (talk)?
print(shows["genre"]["talk"]["the_daily_show"]["host"])

# QUESTION 7: Who are all the hosts of the view (talk)
for i in shows["genre"]["talk"]["the_view"]["host"]:
    print(i)
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually


# QUESTION 8: What are the show names of the Impractical Jokers (comedy)
for i in shows["genre"]["comedy"]["impractical_jokers"]["cast"]:
    print(i["showName"])
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually


# QUESTION 9: Who does Will Arnett play in Arrested Development (comedy)


# QUESTION 10: Who plays Yami Yugi in Yu-Gi-Oh (kids)?


# QUESTION 11: How many seasons did the Office (comedy) run?


# QUESTION 12: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?


# QUESTION 13: List the characters in Teen Titans (kids)


# QUESTION 14: What is the link to the IMDB page for the actor who plays Mr. Krabs (Spongebob, kids)?


# QUESTION 15: Who plays Negan in The Walking Dead?


# QUESTION 16: List the main cast of Dexter (drama) (the actors, not the characters)


# QUESTION 17: Is Game of Thrones(drama) still running?


# QUESTION 18: Who does Peter Dinklage play in Game of Thrones (drama)?


# QUESTION 19: List the American Idol Judges


# QUESTION 20: Who plays Dustin in Stanger Things (drama)?


# %%
# Define a function `calculate` that takes in two numbers and adds, subtracts, multiplies, or divides the two numbers.
def calculate(a, b):
    # Create a variable `result` and set it to 0.
    result = None
    # Prompt the user "What do you want to do: Add, Subtract, Multiply or Divide?" and assign the answer to a variable `choice`.
    choice = input("What do you want to do: Add, Subtract, Multiply or Divide?")
    while result == None:
    # Create an if-else statement to perform the proper calculation with the two parameters based on the user's `choice`.
        if choice == "add" or choice == "Add":
            result = a + b
        elif choice == "subtract" or choice == "Subtract":
            result = a - b
        elif choice == "multiply" or choice == "Multiply":
            result = a * b
        elif choice == "divide" or choice == "Divide":
            if b == 0:
                return "You can't divide by 0!"
            else:
                result = a / b
        elif choice == "":
            return "You didn't choose an option"
        else:
            choice = input("Please enter: Add, Subtract, Multiply or Divide.")

    # Return the calculated `result` variable.
    return result

# Call the `calculate` function and print the results.
print(calculate(6,9))

# %%
