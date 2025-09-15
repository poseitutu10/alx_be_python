income = int(input("Enter your monthly income: "));
expense = int(input("Enter your total monthly expenses: "));
savings = income - expense;

#Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
projected_savings = savings * 12 + (savings * 12 * 0.05);

print(f"Enter your monthly income: {income}");
print(f"Enter your total monthly expenses: {expense}");
print(f"Your monthly savings are ${savings}.");
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")