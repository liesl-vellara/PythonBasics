import numpy as np
# Creating an array
cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print(cupcakes)

# importing a csv file as a array using numpy. The delimiter is ','
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print(recipes)

# selecting all the eggs in the eggs column from the recipe array
eggs = recipes[:,2]

# using a boolean to check which recipes uses only one egg
#print(eggs == 1)

# Get the recipe for cookies from the array
cookies = recipes[2, :]
#print(cookies)

# creating a double batch of cupcakes
double_batch = 2 * cupcakes
print(double_batch)

# creating a custom array containing the cookies and double cupcakes
grocery_list = cookies + double_batch
print(grocery_list)
