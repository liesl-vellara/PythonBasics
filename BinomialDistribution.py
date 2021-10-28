import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# finding the total number of respnses equal to 'Ceballos
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])

# calculating the percentage
percentage_ceballos = 100*total_ceballos / len(survey_responses)

# In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. 
# Your supervisors are concerned because this is a very different outcome than what the poll predicted. 
# They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.
#Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters.
P = 0.54
# actual population of the town
town_size = 10000

# analysis using Binomial distribution
possible_surveys = np.random.binomial(len(survey_responses), 0.47, size = town_size)
print(total_ceballos, percentage_ceballos)

# plotting the histogram of the possible surveys to see the distribution
plt.hist(possible_surveys, bins = 20)
plt.show()
# recalculate the percentage of surveys that would have an outcome of Ceballos losing 
ceballos_loss_surveys = np.mean(possible_surveys < 16)
print(ceballos_loss_surveys)
