# Movie ticket price:Input the following data: 
# my age, and which week it is day rules:
# The ticket costs 10GEL 60% discount on Monday and Friday; 
# If I am under 12 or over 65 I get 50% sale.

age = int(input('your age: '))

weekDay = input('week day: ')

cost = 10

if weekDay.lower() == 'monday' or weekDay.lower() == 'friday':
  cost=10-(10*6/10);
  if age<12 or age>65:
    cost*=0.5

print(cost)