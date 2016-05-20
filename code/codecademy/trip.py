def hotel_cost(nights):
    return 1400 * nights


def plane_ride_cost(city):
    if city == "charlotte":
        print("183")
        return 183
    elif city == "Tampa":
        print("220")
        return 220
    elif city == "Pittsburgh":
        print("222")
        return 222
    elif city == "Los Angeles":
        print("475")
        return 475


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost = cost-50
    elif days >= 3:
        cost = cost-20
    print(cost)
    return cost


def trip_cost(city, days, spending_money):
    print(plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money)
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money

trip_cost("Los Angeles", 5, 600)
