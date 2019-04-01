'''
ps4 vs xboxone vs WiiU
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as pyp
import seaborn as sns

vg = pd.read_csv('VGS.csv')  # reading the csv file
vg = vg.replace('tbd', np.nan)  # there are some value with tdb changing them to NA
vg.User_Score = vg.User_Score.astype(float)  # since the user score is in object covert to float
vg = vg[vg.Year_of_Release >= 1970]  # some years are less then 1970 gaming was not there then
vg = vg.dropna(axis=0)  # dropping NA Values

'''
Only having the 7th generation consoles.
'''
vg8 = vg[(vg['Platform'] == 'WiiU') | (vg['Platform'] == 'PS4') | (vg['Platform'] == 'XOne')]
vgxone = vg[(vg['Platform'] == 'XOne')]
vgps4 = vg[(vg['Platform'] == 'PS4')]
vgwiiu = vg[(vg['Platform'] == 'WiiU')]


def sales():
    '''
    Total sales by year for the three platforms
    '''
    s = vg8.groupby(['Year_of_Release', 'Platform']).Global_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='spectral', grid=False)
    pyp.title('Global Sales of 8th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()


def nasales():
    '''
    North America Sales of three platforms
    '''
    s = vg8.groupby(['Year_of_Release', 'Platform']).NA_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='spectral', grid=False)
    pyp.title('North America Sales of 8th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()


def eusales():
    '''
    Europe Sales for three platforms
    '''
    s = vg8.groupby(['Year_of_Release', 'Platform']).EU_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='spectral', grid=False)
    pyp.title('Europe Sales of 8th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()


def jpsales():
    '''
    Japan Sales for three platforms
    '''
    s = vg8.groupby(['Year_of_Release', 'Platform']).JP_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='spectral', grid=False)
    pyp.title('Japan Sales of 8th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()


def otsales():
    s = vg8.groupby(['Year_of_Release', 'Platform']).Other_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='nipy_spectral', grid=False)
    pyp.title('Rest of the World Sales of 8th Generation Consoles')
    pyp.ylabel('Sales in millions')
    pyp.show()


def genresales():
    '''
    Sales for the three platforms in every genre they sold
    '''
    x = vg8.groupby(['Genre', 'Platform']).Global_Sales.sum()
    x.unstack().plot(kind='bar', figsize=(16, 9))
    pyp.title('8th Generation Sales per Genre')
    pyp.ylabel('Sales in millions')
    pyp.show()


def releasengenrexone():
    '''
       Total number of releases per Genre
       '''
    pyp.figure(figsize=(13, 4))
    x = vgxone.Genre.value_counts().index
    sns.countplot(vgxone.Genre.dropna(), order=x)
    pyp.title('Number of Games Released in every Genre for Xbox One')
    pyp.show()


def releasengenreps4():
    '''
       Total number of releases per Genre
       '''
    pyp.figure(figsize=(13, 4))
    x = vgps4.Genre.value_counts().index
    sns.countplot(vgps4.Genre.dropna(), order=x)
    pyp.title('Number of Games Released in every Genre for PS4')
    pyp.show()


def releasengenrewiiu():
    '''
       Total number of releases per Genre
       '''
    pyp.figure(figsize=(13, 4))
    x = vgwiiu.Genre.value_counts().index
    sns.countplot(vgwiiu.Genre.dropna(), order=x)
    pyp.title('Number of Games Released in every Genre for Wii U')
    pyp.show()


def ps4():
    '''
    Pie chart for genre
    :return:
    '''
    pyp.title("PS4 Genre Distribution")
    c = vg8.loc[vg["Platform"] == "PS4"].Genre.unique()
    z = pyp.pie(vg8.loc[vg8["Platform"] == "PS4"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=False)

    pyp.show()


def xone():
    '''
    Pie chart for genre
    :return:
    '''
    pyp.title("Xbox One Genre Distribution")
    c = vg8.loc[vg["Platform"] == "XOne"].Genre.unique()
    z = pyp.pie(vg8.loc[vg8["Platform"] == "XOne"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=False)

    pyp.show()


def wiiu():
    '''
    pie chart for genre
    :return:
    '''
    pyp.title("Wii U Genre Distribution")
    c = vg8.loc[vg["Platform"] == "WiiU"].Genre.unique()
    z = pyp.pie(vg8.loc[vg8["Platform"] == "WiiU"].Genre.value_counts(), labels=c, autopct='%1.1f%%', shadow=False)

    pyp.show()


def xonesales():
    '''
    xone sales
    '''
    s = vgxone.groupby(['Year_of_Release', 'Platform']).Global_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='Dark2', grid=False)
    pyp.title('Xbox One Sales')
    pyp.ylabel('Sales in millions')
    pyp.show()


def ps4sales():
    '''
    Ps3 sales
    '''
    s = vgps4.groupby(['Year_of_Release', 'Platform']).Global_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='Dark2', grid=False)
    pyp.title('PS4 Sales')
    pyp.ylabel('Sales in millions')
    pyp.show()


def wiiusales():
    '''
    Wii Sales
    '''
    s = vgwiiu.groupby(['Year_of_Release', 'Platform']).Global_Sales.sum()
    s.unstack().plot(kind='bar', stacked=False, colormap='Dark2', grid=False)
    pyp.title('Wii U Sales')
    pyp.ylabel('Sales in millions')
    pyp.show()

def usage():
    pyp.pie(vg8.groupby('Platform').User_Count.sum(),labels=vg8.groupby('Platform').User_Count.sum().index,startangle=90,autopct='%.1f%%')
    pyp.title('User Base')
    pyp.show()

def main():
    sales()
    nasales()
    eusales()
    jpsales()
    otsales()
    genresales()
    releasengenrexone()
    releasengenrewiiu()
    releasengenreps4()
    ps4()
    xone()
    wiiu()
    xonesales()
    ps4sales()
    wiiusales()



if __name__ == '__main__':
    main()