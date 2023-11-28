# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel("RDI-12.xlsx")
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=["Standardised"])
print(data)
# take the data in a an array
data = data.values
#remove the nan values
data = data[~pd.isnull(data)]
data = data[:85]
# print("The array is:\n", data)

near_28 = data[:28]
middle_28 = data[28:56]
far_29 = data[56:]
print("The first 28 years are:\n", len(near_28))
print("The second 28 years are:\n", len(middle_28))
print("The last 28 years are:\n", len(far_29))

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

for i in range(len(near_28)):
    if near_28[i] < 0:
        if near_28[i] > -0.99:
            near_normal_near += 1
        elif near_28[i] > -1.49:
            moderate_near += 1
        elif near_28[i] > -1.99:
            severe_near += 1
        else:
            extreme_near += 1

for i in range(len(middle_28)):
    if middle_28[i] < 0:
        if middle_28[i] > -0.99:
            near_normal_middle += 1
        elif middle_28[i] > -1.49:
            moderate_middle += 1
        elif middle_28[i] > -1.99:
            severe_middle += 1
        else:
            extreme_middle += 1

for i in range(len(far_29)):
    if far_29[i] < 0:
        if far_29[i] > -0.99:
            near_normal_far += 1
        elif far_29[i] > -1.49:
            moderate_far += 1
        elif far_29[i] > -1.99:
            severe_far += 1
        else:
            extreme_far += 1

print("The number of near normal near is: ", near_normal_near)
print("The number of moderate near is: ", moderate_near)
print("The number of severe near is: ", severe_near)
print("The number of extreme near is: ", extreme_near)

print("The number of near normal middle is: ", near_normal_middle)
print("The number of moderate middle is: ", moderate_middle)
print("The number of severe middle is: ", severe_middle)
print("The number of extreme middle is: ", extreme_middle)

print("The number of near normal far is: ", near_normal_far)
print("The number of moderate far is: ", moderate_far)
print("The number of severe far is: ", severe_far)
print("The number of extreme far is: ", extreme_far)


     