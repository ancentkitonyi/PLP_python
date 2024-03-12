
### CHALLENGE 1 ####
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

integers = int(input("Enter total numbers items you'll add to a list: "))
list_int = []
print(integers)

# Get user input for each integer and add it to the list
for i in range(integers):
    element = int(input(f"Enter an integer {i + 1}: "))
    list_int.append(element)
print(f"List of integers: {list_int}")

#Compute the sum of all integers in the list
sum_of_integers = sum(list_int)
print(f"Sum of the integers: {sum_of_integers}\n")


##### CHALLENGE 2 #####
# Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.

my_tuple=("Learn Python", "Forex Guide", "My Money", "From the Grass", "Journey")
print("My favorite books: ")
for i in my_tuple:
    print(i)
print("\n")


##### CHALLENGE 3 #####
# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

user_info= {}
user_info['Name'] = input("Enter your name: ")
user_info['Age'] = input("Enter your age: ")
user_info['Favorite Color'] = input("Enter your favorite color: ")
print("\n Person's Information:")
for key, value in user_info.items():
    print(f"{key}: {value}")