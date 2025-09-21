# Receive input for two number
num1 = int(input("Enter the first number: "));
num2 = int(input("Enter second number: "));
operation = input("Choose the operation (+, -, *, /):");

match operation:
  case "+":
    sum = num1 + num2;
    print(f"The result is {sum}")
  case "-":
    diff = num1 - num2;
    print(f"The result is {diff}")
  case "/":
    if not num2 == 0:
      divide = num1 / num2;
      print(f"The result is {divide}")
    else:
      print("EXception")
  case "*":
    mult = num1 * num2;
    print(f"The result is {mult}")
  case _:
    print("Invaid operation")