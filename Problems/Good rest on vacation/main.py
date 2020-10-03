# put your python code here
days = int(input())
food_cost_day = int(input())
flight_cost = int(input())
night_cost = int(input())

print(days * food_cost_day + (days - 1) * night_cost + flight_cost * 2)
