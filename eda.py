import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp
import seaborn as sns


vg = pd.read_csv('VGS.csv')
vg = vg.replace('tbd', np.nan)
vg.User_Score = vg.User_Score.astype(float)
vg = vg[vg.Year_of_Release >= 1970]
vg = vg[vg.Year_of_Release <= 2017]
vg["User_Score"] = vg.User_Score * 10


def correlation():
    '''
    Correlation comparision
    :return:
    '''
    pyp.figure(figsize=(12, 8))
    vgcor = vg.corr()
    sns.heatmap(vgcor,
                xticklabels=vgcor.columns.values,
                yticklabels=vgcor.columns.values,
                annot=True)
    return vgcor


def toppublishersbysales():
    '''
    Will be displayed in the pycharm console output
    Top 10 Publishers by sales
    '''
    s = vg.groupby(['Publisher']).sum().Global_Sales.copy()
    s.sort_values(ascending=False, inplace=True)

    return s.head(10)

def toppubbynoofreleases():
    '''
    Will be displayed in the pycharm console output
    Top 10 publishers by no of releases
    '''
    r = vg.groupby(['Publisher']).count().Name.copy()
    r.sort_values(ascending=False, inplace=True)

    return r.head(10)


def criticvsuser():
    '''
    Comparision between critic and user rating using pearsonr
    '''
    g = sns.jointplot(x='Critic_Score', y='User_Score', data=vg, kind='hex', cmap='hot', size=6)
    sns.regplot(vg.Critic_Score, vg.User_Score, ax=g.ax_joint, scatter=False, color='grey')
    pyp.show()


def releasenplatform():
    '''
    Total number of releases for platform
    '''
    pyp.figure(figsize=(13, 4))
    x = vg.Platform.value_counts().index
    sns.countplot(vg.Platform.dropna(), order=x)
    pyp.show()

def salesnpublish():
    '''
    No of releases by publishers
    '''
    vg.groupby('Publisher').count().sort_values('Name', ascending=False)[:20]['Name'].plot(kind='bar', figsize=(12, 7))
    pyp.ylabel("Count")
    pyp.show()

def sales():
    '''
    Total sales per year in millions
    '''
    vg.groupby('Year_of_Release').sum().plot.bar(x=vg.groupby('Year_of_Release').sum().index, y='Global_Sales',
                                                 figsize=(12, 6))
    pyp.title("Total Sales per Year in Million Units")
    pyp.ylabel('Sales in Millions')
    pyp.show()

def salesnplatform():
    '''
    Total sales for each platform
    '''
    vg.groupby('Platform').sum().reset_index().sort_values(by='Global_Sales')[['Global_Sales', 'Platform']].plot(
        kind='bar', x='Platform', figsize=(12, 6))
    pyp.title("Total Sales in Millions")
    pyp.show()


def salesplatformyears():
    '''
    Total sales for every platform for every year
    '''
    s = vg.groupby(['Year_of_Release', 'Platform']).Global_Sales.sum()
    s.unstack(level=1).plot(kind='line', stacked=False, colormap='spectral', grid=False)
    pyp.title('Global Sales of All Platforms')
    pyp.ylabel('Sales in millions')
    pyp.show()


def main():
    correlation()
    print(toppubbynoofreleases())
    print(toppublishersbysales())
    criticvsuser()
    releasenplatform()
    salesnpublish()
    sales()
    salesnplatform()
    salesplatformyears()


if __name__ == '__main__':
    main()
