from sklearn import linear_model

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp

# Import data

vg = pd.read_csv('VGS.csv')
vg = vg.replace('tbd', np.nan)
data = vg.loc[vg.Year_of_Release >= 1999]
data = data.dropna(axis=0)
data.User_Score = data.User_Score.astype(float)
data = data[data.Year_of_Release.notnull()]


def genrereg():
    # Finding the median sales value by genre and year
    Med_Sales_by_Gen_and_Yr = pd.pivot_table(data, index=['Year_of_Release'],
                                             columns=['Genre'], values=['Global_Sales'], aggfunc=np.median)
    Data = Med_Sales_by_Gen_and_Yr
    Data.columns = Data.columns.get_level_values(1)
    Regr_Coeff = []
    Regr_MSE = []
    fig, axes = pyp.subplots(nrows=4, ncols=3, figsize=(10, 12))

    x = np.transpose(np.matrix(Data.index))

    count = 0

    for genre in Data.columns:
        axs = axes[count // 3, count % 3]
        y = Data[genre].to_frame()

        # Linear regression
        regr = linear_model.LinearRegression()
        print(x)
        print(y)


def main():
    genrereg()


main()
