# Import required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn  # Machine learning algos

# Load the datasets
oecd_bli = pd.read_csv("oecd_bli_2015.csv", delimiter=",", thousands=",", encoding="latin1", na_values="n/a")
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", delimiter=",", thousands=",", encoding="latin1", na_values="n/a",engine="python")
print(oecd_bli.columns)


# Retaining only the needed rows
oecd_bli = oecd_bli[oecd_bli["Indicator"] == "Life satisfaction"]
# Select only these 2 columns
oecd_bli = oecd_bli[["Country", "Value"]]
# Renaming those selected columns
oecd_bli.columns = ["Country", "Life satisfaction"]


# Keep only these 2 cols
gdp_per_capita = gdp_per_capita[["Country", "2015"]]
# Change col names for common match and meaningful names
gdp_per_capita.columns = ["Country", "GDP per capita"]


# Merge using common tag (Country)
country_stats = pd.merge(oecd_bli, gdp_per_capita, on="Country")


#Extracting x and y for ML model
x = country_stats[["GDP per capita"]]
y = country_stats[["Life satisfaction"]]

#Plot to visualiza the relationship
plt.figure(figsize=(9,6))
plt.scatter(x,y, color="Hotpink",alpha=0.8)
plt.title("GDP vs Life Satisfaction")
plt.xlabel("GDP per capita")
plt.ylabel("Life satisfaction")
plt.grid()
plt.show()

#Train the Linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
#finds the best straight line
model.fit(x,y)


#To visualiza the regression plot
# Create points for the regression line
X_line = np.linspace(x["GDP per capita"].min(), x["GDP per capita"].max(), 100).reshape(-1, 1)
y_line = model.predict(X_line)

# Plot scatter + regression line together
plt.figure(figsize=(9,6))
plt.scatter(x, y, color="hotpink", alpha=0.8, label="Data points")
plt.plot(X_line, y_line, color="blue", linewidth=2, label="Best fit line")

plt.title("GDP vs Life Satisfaction (with Regression Line)")
plt.xlabel("GDP per capita")
plt.ylabel("Life satisfaction")
plt.grid()
plt.legend()
plt.show()


#Prediction for unknown data
X_new = pd.DataFrame([[22587]], columns=["GDP per capita"])
prediction = model.predict(X_new)
print("Prediction for Cyprus:", prediction)


