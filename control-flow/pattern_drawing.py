size = int(input("Enter the size of the pattern: "));
initial_size = 1;

while initial_size <= size:
  for number in range(size):
    print("*", end="")
  print();
  initial_size += 1;