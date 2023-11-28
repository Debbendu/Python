# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel("RDI-6.xlsx")
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=["Standardised"])
# take the data in a an array
data = data.values
#remove the nan values
data = data[~pd.isnull(data)]
# remove zero values
data = data[data != 0]
print("The array is:\n", data)
near_28 = data[:28*12-2]
middle_28 = data[28*12-2:56*12-2]
far_29 = data[56*12-2:]
print("The first 28 years are:\n", len(near_28))
# print("The second 28 years are:\n", middle_28)
# print("The last 28 years are:\n", far_29)
# find at least three consecutive negative values
near_normal_near=0
moderate_near=0
severe_near=0
extreme_near=0

near_normal_middle=0
moderate_middle=0
severe_middle=0
extreme_middle=0

near_normal_far=0
moderate_far=0
severe_far=0
extreme_far=0
neg_list = []
for i in range(len(near_28)):
    if near_28[i] > 0:
        if len(neg_list) >= 3:
            # print("The list is: ", neg_list)
            # find the lowest negative value in the list
            lowest = min(neg_list)
            if lowest > -0.99:
                near_normal_near += 1
            elif lowest > -1.49:
                moderate_near += 1
            elif lowest > -1.99:
                severe_near += 1
            else:
                extreme_near += 1
        neg_list = []
    else:
        neg_list.append(near_28[i])

if len(neg_list) >= 3:
    # find the lowest negative value in the list
    lowest = min(neg_list)
    if lowest > -0.99:
        near_normal_near += 1
    elif lowest > -1.49:
        moderate_near += 1
    elif lowest > -1.99:
        severe_near += 1
    else:
        extreme_near += 1

print("The number of near normal of near_28 is: ", near_normal_near)
print("The number of moderate of near_28 is: ", moderate_near)
print("The number of severe of near_28 is: ", severe_near)
print("The number of extreme of near_28 is: ", extreme_near)

neg_list = []
for i in range(len(middle_28)):
    if middle_28[i] > 0:
        if len(neg_list) >= 3:
            # print("The list is: ", neg_list)
            # find the lowest negative value in the list
            lowest = min(neg_list)
            if lowest > -0.99:
                near_normal_middle += 1
            elif lowest > -1.49:
                moderate_middle += 1
            elif lowest > -1.99:
                severe_middle += 1
            else:
                extreme_middle += 1
        neg_list = []
    else:
        neg_list.append(middle_28[i])

if len(neg_list) >= 3:
    # find the lowest negative value in the list
    lowest = min(neg_list)
    if lowest > -0.99:
        near_normal_middle += 1
    elif lowest > -1.49:
        moderate_middle += 1
    elif lowest > -1.99:
        severe_middle += 1
    else:
        extreme_middle += 1

print("The number of near normal of middle_28 is: ", near_normal_middle)
print("The number of moderate of middle_28 is: ", moderate_middle)
print("The number of severe of middle_28 is: ", severe_middle)
print("The number of extreme of middle_28 is: ", extreme_middle)


neg_list = []
for i in range(len(far_29)):
    if far_29[i] > 0:
        if len(neg_list) >= 3:
            # print("The list is: ", neg_list)
            # find the lowest negative value in the list
            lowest = min(neg_list)
            if lowest > -0.99:
                near_normal_far += 1
            elif lowest > -1.49:
                moderate_far += 1
            elif lowest > -1.99:
                severe_far += 1
            else:
                extreme_far += 1
        neg_list = []
    else:
        neg_list.append(far_29[i])

if len(neg_list) >= 3:
    # find the lowest negative value in the list
    lowest = min(neg_list)
    if lowest > -0.99:
        near_normal_far += 1
    elif lowest > -1.49:
        moderate_far += 1
    elif lowest > -1.99:
        severe_far += 1
    else:
        extreme_far += 1

print("The number of near normal of far_29 is: ", near_normal_far)
print("The number of moderate of far_29 is: ", moderate_far)
print("The number of severe of far_29 is: ", severe_far)
print("The number of extreme of far_29 is: ", extreme_far)



