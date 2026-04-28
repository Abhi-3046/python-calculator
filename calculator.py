# simple calculator
while True:
  operation = input("Choose (add, sub, mul, div , mode) or exit: ").strip().lower()
  
  if operation == "exit":
    print("see you 🫡")
    break
  
  try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
  except ValueError:
    print("Please enter valid numbers.")
    continue

  if operation == "add":
      print("sum:", number1 + number2)
  
  elif operation == "sub":
      print("sub:", number1 - number2)
  
  elif operation == "mul":
      print("multi:", number1 * number2)
  
  elif operation == "div":
    
      if number2 != 0:
        print("div:", number1 / number2)
    
      else:
        print("Error: Cannot divide by zero.")
  
  elif operation == "mode":
    if number2 != 0:
        print("mod:", number1 % number2)
    else:
        print("Error: Cannot modulo by zero.")
  
  else:
    print("invalid use (add, sub, mul, div , mode)")
