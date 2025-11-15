#Simple Calculator with Match Case

#Prompt user for numbers
try:
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number:"))
except ValueError:
        print("Invalid input. Please enter numbers.")
        exit()

operation = input("Choose the operation (+, -, *, /):")

# Initialize result
result = None

# Match Case to perform calculation
match operation:
   case "+":
        result = first_number + second_number
   case "-":
        result = first_number - second_number
   case "*":
          result = first_number * second_number
   case "/":
          if second_number != 0:
                result = first_number / second_number
          else:
                print("Error:Devision by zero is not allowed.")
   case _:
            print("Invalid operation.")
        
if result != 0:
      print(f"Result: {result}")
   