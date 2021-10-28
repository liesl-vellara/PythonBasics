import numpy as np

# importing the csv file as an array
calorie_stats = np.genfromtxt('cereal.csv', delimiter = ',')
#print(calorie_stats)

# percentile of competition which has their calories higher than 60
average_calories = np.mean(calorie_stats)
print(average_calories)

# checking if there are any outliers
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# lets see how many calories is the median
median_calories = np.median(calorie_stats)
print(median_calories)
nth_percentile = np.percentile(calorie_stats, [0, 25, 50, 75, 100])
print(nth_percentile)

# finding how many competition is more than 60
more_calories = np.mean(calorie_stats > 60)
print(more_calories)

#lets see the spread of data
calorie_std = np.std(calorie_stats)
print(calorie_std)
print("The average calorie of cereals from our data set is around 100, when we checked for outliers, there were non found. The quartile range suggests that our product lies within the first quartile and a minimum of  96% of the other products in the market are more than 60 calories. The spread of data is norminal and not too large or too small.")
