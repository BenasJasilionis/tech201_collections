starters = ("prawn cocktail", "beef tartare", "sweet and sour dumplings")
mains = ("beef wellington", "butter chicken", "mac'n cheese")
desserts = ("chocolate mousse", "lava cake", "lemon meringue pie")
drinks = ("water", "wine", "diet soda", "vodka", "brandy", "champagne")

meal_plan = []

print(f"Hello, please select a starter from the list : {starters}")
starter = input()
meal_plan.append(starter)
print(f"So far you have ordered : {meal_plan},")
print(f"Please order a main from the list : {mains}")
main = input()
meal_plan.append(main)
print(f"So far you have ordered : {meal_plan}")
print(f"Please select a dessert from the list: {desserts}")
dessert = input()
meal_plan.append(dessert)
print(f"So far you have ordered : {meal_plan}")
print(f"Please select a drink from the list : {drinks}")
drink = input()
meal_plan.append(drink)
print(f"Your starter is a {meal_plan[0]}. For the main course, you have opted for {meal_plan[1]} with a {meal_plan[2]}. Your choice of beverage is {meal_plan[-1]}.")
print("Enjoy your meal!")


