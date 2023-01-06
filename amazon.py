# create my own min function
def min(list_values):
    lowest = list_values[0]
    for num in list_values:
        if num < lowest:
            lowest = num
    return lowest

# create my own max function
def max(list_values):
    highest = list_values[0]
    for num in list_values:
        if num > highest:
            highest = num
    return highest

# create my own average function
def mean_average(list_values):
    total = 0
    for num in list_values:
        total += num
    return round(total / len(list_values), 2)

# create function to calculate result based on operator
def gen_results(operator, list_values):
    if operator == "min":
        return min(list_values)
    elif operator =="max":
        return max(list_values)
    else:
        return mean_average(list_values)

# read the input file - encode to avoid unusual characters on first line
with open("input.txt", encoding='utf-8-sig') as file:
    all_inputs = file.read()

# split into list of lines
lines_list = all_inputs.strip().split("\n")

# for each line in file
for line in lines_list:
    # split into operation and values
    operation_values = line.split(":")

    # split values to get list of numbers as strings
    list_of_strings = operation_values[1].split(",")

    # convert to list of ints
    list_of_ints = [eval(i) for i in list_of_strings]

    # print result of operation on list of ints using gen_results function
    print(f"The {operation_values[0]} of [{operation_values[1]}] is {gen_results(operation_values[0], list_of_ints)}")
