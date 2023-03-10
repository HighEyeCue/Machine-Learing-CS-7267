# Importing libraries
# -------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# ---------------------
dataset = pd.read_csv('Polynomial-Dataset.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
# Missing line-----------------------------------------
lin_reg = LinearRegression()
# Missing line-----------------------------------------
lin_reg.fit(X,y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualising the Linear Regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (Linear Regression 2)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Fitting Polynomial Regression to the dataset with degree=3
poly_reg = PolynomialFeatures(degree=3)
X_poly = poly_reg.fit_transform(X)
# Missing line-----------------------------------------
lin_reg_3 = LinearRegression()
# Missing line-----------------------------------------
lin_reg_3.fit(X_poly, y)

# Visualising the Polynomial Regression results with degree=3
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg_3.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff (Linear Regression 3)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Fitting Polynomial Regression to the dataset with degree=4
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
# Missing line-----------------------------------------
lin_reg_4 = LinearRegression()
# Missing line-----------------------------------------
lin_reg_4.fit(X_poly, y)

# Visualising the Polynomial Regression results with degree=4
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg_4.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Truth or Bluff (Linear Regression 4)')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with Linear Regression
# Missing line-----------------------------------------
print("Linear Regression Prediction of level 6.5: " + str(lin_reg.predict([[6.5]])))

# Predicting a new result with Polynomial Regression
# Missing line-----------------------------------------
print("Polynomial Regression Prediction of level 6.5: " + str(lin_reg_4.predict(poly_reg.fit_transform([[6.5]]))))