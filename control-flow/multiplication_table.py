#Multiplication Table Generator

# Ask the user to input a number for which they want to see the multiplication table:

#ask the user input 
number = int(input("Enter a number to see its multiplication table "))


# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    result = i * number
    print(f"{number} * {i} = {result}")
