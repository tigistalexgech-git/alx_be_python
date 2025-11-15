#Simple Calculator with Match Case

#Prompt user for numbers
try:
    number1 = int(input("Enter the first number : "))
    number2 = int(input("Enter the second number:"))
except ValueError:
        print("Invalid input. Please enter numbers.")
        exit()

operation = input("Choose the operation (+, -, *, /):")

# Initialize result
result = None

# Match Case to perform calculation
match operation:
   case "+":
        result = number1 + number2
   case "-":
        result = number1 - number2
   case "*":
          result = number1 * number2
   case "/":
          if number2 != 0:
                result = number1 / number2
          else:
                print("Error:Devision by zero is not allowed.")
   case _:
            print("Invalid operation.")
        
if result != 0:
      print(f"Result: {result}")
   