

def perform_operation(num1 ,num2 , operation):
  match operation:
    case "add":
      sum = float(num1) + float(num2)
      return sum
    case "subtract":
      subtract = float(num1) - float(num2);
      return subtract
    case "multiply":
      multiply = float(num1) * float(num2);
      return multiply
    case "divide":
      try:
        divide = float(num1) / float(num2);
        return divide
      except:
        print("Can't divide by zero")
    case _:
      print('Invalid operation')

print(__name__)