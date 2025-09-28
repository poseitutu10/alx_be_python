from datetime import datetime
from datetime import timedelta

def display_current_datetime():
  current_date = datetime.now()
  print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')
  number_of_days = int(input('Enter the number of days to add to the current date: '));
  new_date = current_date + timedelta(days=number_of_days) 
  print(f'Future date: {new_date.strftime("%Y-%m-%d %H:%M:%S")}')


if __name__ == "__main__":
  display_current_datetime()