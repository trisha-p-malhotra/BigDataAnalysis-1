import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import sklearn as scikit_learn
from statsmodels.nonparametric.smoothers_lowess import lowess
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

"""
__author__ : Group 6 - Introduction to Big data - Fall 2017 
This program reads the VideoGameSales.csv dataset,
and applies Polynomial Regression to predict Europe Sales 
by training on North America sales.
Results are as plotted and,
R2 score: 0.409171424691
Mean absolute error: 0.184974586314
"""
# Reading csv file
VG_sales = pd.read_csv('VGS_project.csv', encoding ='latin1')

# Considering only NonEmpty rows of
sales = VG_sales.NA_Sales.notnull()
sales = VG_sales.EU_Sales.notnull()

# Positive integer values for NA and EU sales columns
sales = VG_sales[((VG_sales.NA_Sales > 0) & (VG_sales.EU_Sales > 0))]
sales = sales.sample(500, random_state=0)
sales = sales.loc[sales.NA_Sales.rank().sort_values().index]
NA_sales_ranks = sales.NA_Sales.rank()
EU_Sales = sales.EU_Sales
sbn.jointplot(NA_sales_ranks, EU_Sales)

# converting NA Sales into ranks in the ascending order and adding to newaxis
NA_ranks = sales.NA_Sales.rank().values[:, np.newaxis]

EU_sales = sales.EU_Sales.values[:, np.newaxis]

plt.style.use('seaborn-darkgrid')

def PolyR_predict(degree):

    # Generate Polynomial features as per equation of the given degree
    poly_features = PolynomialFeatures(degree=degree)
    # Fit to data size of NA Sales ranks and transform the matrix to fit.
    NA_ranks_polyfit = poly_features.fit_transform(NA_ranks)
    # Creating a Linear regression object
    lr = LinearRegression()
    # Fit EU Sales to NA ranks(with polynomial features)
    lr.fit(NA_ranks_polyfit, EU_sales)
    # Predict EU sales as per NA_sales_ranks(with polynomial features)

    EU_predictions = lr.predict(NA_ranks_polyfit)
    result = np.dstack((EU_sales.flatten(), EU_predictions.flatten())).reshape((500, 2))

    """
    Uncomment for Residual plot
    """
    #plt.figure()
    #sbn.residplot(NA_sales_ranks, EU_predictions , color="g", label='Residual plot')

    from sklearn.metrics import mean_absolute_error
    from sklearn.metrics import r2_score

    r2_score = (r2_score(EU_sales, EU_predictions))
    print("R2 score: " + str(r2_score))

    mae = (mean_absolute_error(EU_sales, EU_predictions))
    print("Mean absolute error: " + str(mae))
    return result

def main():


    degree = 3
    prediction_res = PolyR_predict(degree)
    plt.figure()
    plt.plot(range(len(prediction_res[:, 1])), prediction_res[:, 1])
    plt.scatter(range(len(prediction_res[:, 0])), prediction_res[:, 0], color='black')
    plt.ylabel("Europe Sales (in millions)")
    plt.xlabel("Prediction for random 500 records")
    plt.gca().set_title("Polynomial Regression with Degree 3")

if __name__ == '__main__':
    main()