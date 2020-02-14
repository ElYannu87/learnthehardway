def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"Your have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crakcers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

def cookies_and_milk(cookie_count, milk_count):
    print(f"You have {cookie_count} cookies!")
    print(f"To go with this you also have {milk_count} ml of milk!")
    print("That means 'Netflix & Chill' for the whole week-end")




print("We can just give the funktion numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


cookies_and_milk(25, 1000)

cookies_and_milk("not enough", "no")

cookie_amount = input()
milk_amount = input()

cookies_and_milk(int(cookie_amount), int(milk_amount)
