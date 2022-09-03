# Some pseudocode copied from Mr. Peppers

# store a constant of the number of scores we will input: 3
NUM_SCORES = 3

# Prompt user for inputs
# store input as last_name
last_name = input('Enter your last name: ')

# store input as first_name
first_name = input('Enter your first name: ')

# store input as age
age = input('Enter your age: ')

# create a list to hold the scores
scores = []
# prompt user for the scores (do it constant times, use a new variable each time)
for x in range(NUM_SCORES):
    scores.append(int(input(f'Please enter score {str(x + 1)}: ')))

# calculate an average (sum each value and divide by the number of values)
# add all values in average variable
average = 0
for x in range(NUM_SCORES):
    average += scores.pop()
# now divide by NUM_SCORES
average = average / NUM_SCORES

# print output; should look like
# Rodriguez, Linda age: 21 average grade: 92.50

print(last_name + ', ' + first_name + ' age: ' + age
      + ' average grade: ' + str(round(average, 2)))
