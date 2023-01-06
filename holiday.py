def hotel_cost(num_nights):
    cost_per_night = 85
    return num_nights * cost_per_night

def plane_cost(city):
    if city == "london":
        return 100
    elif city == "madrid":
        return 250
    elif city == "paris":
        return 200
    elif city == "new york":
        return 550
    elif city == "sydney":
        return 900
    else:
        return 0

def car_rental(num_days):
    cost_per_day = 50
    return num_days * cost_per_day

def holiday_cost(num_nights, city, num_days):
    return hotel_cost(num_nights) + plane_cost(city) + car_rental(num_days)

# get user input
num_nights = int(input("How many nights are you staying:\t"))
city = input("What city are you travelling to (London, Madrid, Paris, New York or Sydney):\t").lower()
num_days = int(input("How many days do you need a car:\t"))


# print results
print("Holiday Costs\n")
print(f"Hotel Cost: £{hotel_cost(num_nights)}")
print(f"Plane Cost: £{plane_cost(city)}")
print(f"Rental Cost: £{car_rental(num_days)}")
print(f"\nTotal cost: £{holiday_cost(num_nights, city, num_days)}")
