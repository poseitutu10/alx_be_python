def safe_divide(numerator, denominator):
  try: 
    result = float(numerator) / float(denominator);
  except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
  except ValueError as e:
    print("Error: Please enter numeric values only.")
  else: 
   return f"The result of the division is {result}"