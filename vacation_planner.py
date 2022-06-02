print("Welcome to my vaction trip planner")
bugted = int(input("What is your total budget: "))

print(" 1. New York, NY ")
print(" 2 California, CA")
print(" 3 Chicago, IL")
print(" 4 Dallas, TX")
city_choice = int(input("Slect your destination: "))
city_prices = [300,275,190,325,200]
airfare_choice = city_prices[city_choice - 1]
print("Airfare: $", airfare_choice)

days = int(input("How many day's wil you be staying: "))
nights = days - 1
hotel_choice = nights * 89
print("Hotel: $", hotel_cost)

rental_car_cost = days * 40
if days >= 4:
    rental_car_cost = rental_car_cost * 0.90
print("Rental Car: $", rental_car_cost)


meal_costs = days * 50
print("Meals: $", meal_cost)

spending_money = int(input("How much money do you need? "))

total_costs = airfare_choice + hotel_cost + rental_car_cost + meal_cost + spending_money
print("Your total vaction trip will cost $", total_costs)


if total_costs <= budget:
    print("Congratulations --- you stayed within your budget!!!")
else:
    print("Sorry ---- you cannot pay for your trip with your budget!!!")