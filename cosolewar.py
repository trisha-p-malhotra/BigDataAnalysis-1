'''
ps3 vs xbox360 vs Wii
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp
import seaborn as sns


vg = pd.read_csv('VGS.csv')  # reading the csv file
vg = vg.replace('tbd', np.nan) # there are some value with tdb changing them to NA
vg.User_Score = vg.User_Score.astype(float) # since the user score is in object covert to float
vg = vg[vg.Year_of_Release >= 1970] # some years are less then 1970 gaming was not there then
vg=vg.dropna(axis=0) # dropping NA Values

'''
Only having the 7th generation consoles.
'''
vg7=vg[(vg['Platform']=='Wii')|(vg['Platform']=='PS3')|(vg['Platform']=='X360')]


def sales():
    '''
    Total sales by year for the three platforms
    '''
    s=vg7.groupby(['Year_of_Release','Platform']).Global_Sales.sum()
    s.unstack().plot(kind='bar',stacked=False,colormap='spectral',grid=False)
    pyp.title('Global Sales of 7th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()

def genresales():
    '''
    Sales for the three platforms in every genre they sold
    '''
    x = vg7.groupby(['Genre', 'Platform']).Global_Sales.sum()
    x.unstack().plot(kind='bar', figsize=(16, 9))
    pyp.title('7th Generation Sales per Genre')
    pyp.ylabel('Sales in millions')
    pyp.show()

def ps3():
    '''
    Pie chart for genre
    :return:
    '''
    z = pyp.title("PS3")
    c = vg7.loc[vg["Platform"] == "PS3"].Genre.unique()
    z = pyp.pie(vg7.loc[vg7["Platform"] == "PS3"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=True)

    pyp.show()

def x360():
    '''
    Pie chart for genre
    :return:
    '''
    z = pyp.title("X360")
    c = vg7.loc[vg["Platform"] == "X360"].Genre.unique()
    z = pyp.pie(vg7.loc[vg7["Platform"] == "X360"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=True)

    pyp.show()

def wii():
    '''
    pie chart for genre
    :return:
    '''
    z = pyp.title("Wii")
    c = vg7.loc[vg["Platform"] == "Wii"].Genre.unique()
    z = pyp.pie(vg7.loc[vg7["Platform"] == "Wii"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=True)

    pyp.show()


def main():
    sales()
    genresales()
    ps3()
    x360()
    wii()

if __name__ == '__main__':
    main()
