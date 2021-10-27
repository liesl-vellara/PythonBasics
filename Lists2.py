toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
#print(len(toppings), len(prices))

# counting the number of times 2 appears in the list prices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# checking the length of the list
num_pizzas = len(toppings)

print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# Joining the two lists
pizza_and_prices = list(zip(prices, toppings))

# sorting the lists according the cost in ascending order
pizza_and_prices.sort()
print(pizza_and_prices)

# assigning the variable cheapest_pizza to the pizza with the least cost
cheapest_pizza = pizza_and_prices[0]

# assigning the variable priciest_pizza to the last item in the list
priciest_pizza = pizza_and_prices[-1]
# removing the last item from the list
pizza_and_prices.pop(-1)

# inserting the peppers in its place
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)

# using slicing, we get the three cheapest pizzas on the list
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
#print(cheapest_pizza, priciest_pizza)
