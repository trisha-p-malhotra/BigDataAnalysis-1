from sklearn import linear_model

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp

# Import data

vg = pd.read_csv('VGS.csv')
vg = vg.replace('tbd', np.nan)
vg = vg.dropna(axis=0)
vg = vg[vg.Year_of_Release.notnull()]
vg = vg[vg.Global_Sales.notnull()]

def genrereg():
    # Finding the median sales value by genre and year
    data = vg.loc[vg.Year_of_Release > 1999]
    mediansale = pd.pivot_table(data, index=['Year_of_Release'],
                                             columns=['Genre'], values=['Global_Sales'], aggfunc=np.median)
    Data=mediansale
    mediansale.columns = mediansale.columns.get_level_values(1)
    coeff = []
    reg_msd = []
    fig, axes = pyp.subplots(nrows=3, ncols=4)
    x = np.transpose(np.matrix(Data.index))

    count = 0
    for genre in Data.columns:
        axs = axes[count // 4, count % 4]
        y = Data[genre].to_frame()
        # Linear regression
        regr = linear_model.LinearRegression()
        #print(x)
        #print(y)
        regr.fit(x, y)
        # Mean Squared Deviation
        MSD = np.mean((regr.predict(x) - y) ** 2)
        coeff.append(regr.coef_[0][0])
        reg_msd.append(MSD[0])
        Data[genre].plot(ax=axs)
        axs.plot(x, regr.predict(x), color='black')
        ylim = axs.get_ylim()
        txt = 'Coeff: %.3f \nMSD: %.3f' % (regr.coef_, MSD)
        y_loc = 0.75 * (ylim[1] - ylim[0]) + ylim[0]
        axs.text(2008, y_loc, txt)
        axs.set_title(genre)
        axs.set_xlabel('Year')
        axs.set_ylabel('Median Value')
        count += 1
    fig.tight_layout()
    pyp.show()


def main():
    genrereg()

if __name__ == '__main__':
    main()