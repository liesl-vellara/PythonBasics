import pandas as pd

#creating a data frame
inventory = pd.read_csv('inventory.csv')

#inspecting the first 10 rows
#print(inventory.head())

#place the first 10 rows of the dataframe to a variable
staten_island = inventory.iloc[0:10]

#checking on staten island
#print(staten_island)

#selecting a particular column
product_request = staten_island['product_description']

#checking on the product_request
#print(product_request)

#select all the rows with location == brookly and product type == seeds
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

#checking on the function
#print(seed_request)

#adding columns to inventory
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)

#calling the function
#print(inventory.head(10))

#check the value of their inventory
inventory['total_value'] = inventory.apply(lambda x: x['price'] * x['quantity'], axis=1)

#inspecting the dataframe
#print(inventory.head())

#complete description for their catalog
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory.head())
