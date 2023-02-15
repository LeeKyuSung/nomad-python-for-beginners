def make_juice(fruit):
    return f"{fruit}+🥤"


def add_ice(juice):
    return f"{juice}+🧊"


def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)
print(perfect_juice)

winner = 15
if winner > 10:
    print("winner is greater tan 10")
elif winner < 10:
    print("winner is less than 10")
else:
    print("winner is 10")
