# import math module
import math

# create an empty list to hold floats
list_nums = []

test_list = [1.2,3.3,19.9,2.5,9.8,8.8,2.2,5.4,8.2,10.6]

# loop to get floats from the user
# for i in range(10):
#     list_nums.append(float(input("Please enter a float:\t")))

# find sum of all values
print(f"The total of all the values you entered is {math.fsum(test_list)}.")

# find index of max and print the value
max = test_list[0]
index = 0
for i in range(1,len(test_list)):
    if test_list[i] > max:
        max = test_list[i]
        index = i
print(f"The index of the maximum value is {index}. The value is {test_list[index]}.")

# find index of min and print the value
min = test_list[0]
index = 0
for i in range(1,len(test_list)):
    if test_list[i] < min:
        min = test_list[i]
        index = i
print(f"The index of the minimum value is {index}. The value is {test_list[index]}.")

# import statistic module to calculate averages
import statistics
mean = statistics.mean(test_list)
print(f"The mean average is {round(mean,2)}.")
median = statistics.median(test_list)
print(f"The median average is {round(median,2)}.")
