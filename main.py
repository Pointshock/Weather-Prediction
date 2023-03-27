# Use pandas to read an excel file
# and then import sklearn to do some machine learning

# Import our libraries
from math import e
import pandas as pd
from sklearn import tree
import openpyxl
# To supress a warning
import warnings
warnings.filterwarnings("ignore")

# Set the file path for the Excel file we will import
csv_data_file = r"Weather Data.csv"

# Read the Excel file into a pandas dataframe
df = pd.read_csv(csv_data_file)
# If this was a csv file, we would use the following line
# df = pd.read_csv(csv_data_file)

print("\n\t*** Find out what the weather is! ***\n")
# Select the columns we want to use for our features training
# We will use the following columns:
features = df[['Temp_C', 'Dew_Point_Temp_C', 'Rel_Hum_%', 'Wind_Speed_km/h', 'Visibility_km', 'Press_kPa']]

# Select the column we want to use for our label training
# We will use the following column:
labels = df[['Weather']]

# Create a decisition tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier using the features and labels
# Remember that fit means fitness which is where it trains
clf = clf.fit(features, labels)

# Time to hard code some test data to use on model after training
print("The following test weather should print out Mainly Clear")
print("Our feature data is: 14.8 Temp_C, 8.8 Dew Point Temp_C, 67 Rel Hum_%, 17 Wind Speed_km/h, 48.3 Visibility_km, 100.65 Press_kPa")
# The prediction happens here
prediction_result = clf.predict([[ 14.8, 8.8, 67, 17, 48.3, 100.65 ]])
# Display the prediction result
print(prediction_result)

print("The following test weather should print out Fog")
print("Our feature data is: -1.8 Temp_C, -3.9 Dew Point Temp_C, 86 Rel Hum_%, 4 Wind Speed_km/h, 8 Visibility_km, 101.24 Press_kPa")
# The prediction happens here
prediction_result = clf.predict([[ -1.8, -3.9, 86, 4, 8, 101.24]])
# Display the prediction result
print(prediction_result)


# Print out the training data for reference
# Print line
print("_" * 50)
print("\n\t*** Training Data ***\n\n", df)
print("_" * 50)

# Now let's begin the fun part by getting user input
# Collect user temp
Temp = float(input("What is the temperature in C?: "))
# Collect user dew point temp
Dew_Point = float(input("What is the dew point temperature in C?: "))
# Collect user relative humidity
Rel_Hum = float(input("What is the relative humidity %?: "))
# Collect user wind speed
Wind_Speed = float(input("What is the wind speed in km/h?: "))
# Collect user visibility
Visibility = float(input("What is the your visibility in km?: "))
# Collect user pressure
Pressure = float(input("What is the pressure in kPa?: "))


# Make prediction using user input
user_prediction_result = clf.predict([[Temp, Dew_Point, Rel_Hum, Wind_Speed, Visibility, Pressure]])
# Display prediction to user
print("I predict that the weather is: ")
print(user_prediction_result)


# End of program
print("_" * 50)
print("\n\t*** End of Program ***")