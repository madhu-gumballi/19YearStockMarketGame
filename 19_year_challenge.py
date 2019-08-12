#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: madhugumballi
"""

def plotCompany(fig, subplot, data, name, max_year=2019) :
    subplot.xaxis.set_major_locator(majorLocator)
    subplot.xaxis.set_major_formatter(majorFormatter)
    company_data = data[data['COMPANY'] == name]
    company_data = company_data[company_data['DATE'] <= max_year]
    company_data = company_data.sort_values(by=['DATE'])
    count = len(company_data['DATE'])
    fig.suptitle('SECTOR: ' + company_data.iloc[0,3], fontsize=15)
    subplot.plot(company_data['DATE'], company_data['CLOSE'], marker='o')
    subplot.set_title(company_data.iloc[count-1,5], loc='left', fontweight='bold')
    textvalue = company_data.iloc[count-1,2]
    textvalue = round(textvalue)
    subplot.text(company_data.iloc[count-1,1], 
                 company_data.iloc[count-1,2], 
                 "%d"%textvalue, 
                 fontproperties = bold_font,
                 fontsize=15,
                 bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    subplot.spines['right'].set_visible(False)
    subplot.spines['top'].set_visible(False)
    for x in range(count) :
        news = company_data.iloc[x,4]
        if news != 'None':
            subplot.annotate(news,
                             xy=(company_data.iloc[x,1], 
                                 company_data.iloc[x,2]),
                             xycoords='data',
                             xytext=(-200, 40),
                             textcoords='offset points',
                             size=11,
                             va='center',
                             bbox=dict(boxstyle="round", fc=(1.0,0.7,0.7), ec="none", alpha=0.5),
                             arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                             fc=(1.0,0.7,0.7),
                                             ec="none",
                                             patchA=None,
                                             patchB=e1,
                                             alpha=0.5))
                                             #relpos=(0.2,0.5)))
    fig.subplots_adjust(hspace=0.5, wspace=0.1)


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)
from matplotlib.patches import Ellipse
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv("19_YEAR_CHALLENGE.csv")

bold_font = FontProperties()
bold_font.set_weight('bold')

majorLocator = MultipleLocator(2)
majorFormatter = FormatStrFormatter('%d')
e1 = Ellipse((2,-1), 0.5,0.5)
chart_till = 2019

f1, axarr1 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f1, axarr1[0], data, 'INFOSYS', chart_till)
plotCompany(f1, axarr1[1], data, 'SILVERLINE', chart_till)

f2, axarr2 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f2, axarr2[0], data, 'PUNJLLOYD', chart_till)
plotCompany(f2, axarr2[1], data, 'LARSEN', chart_till)

f3, axarr3 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f3, axarr3[0], data, 'SRI ADHIKARI BROTHERS', chart_till)
plotCompany(f3, axarr3[1], data, 'ZEE ENTERTAINMENT', chart_till)

f4, axarr4 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f4, axarr4[0], data, 'DABUR INDIA', chart_till)
plotCompany(f4, axarr4[1], data, 'NESTLE INDIA', chart_till)

f5, axarr5 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f5, axarr5[0], data, 'KARNATAKA BANK', chart_till)
plotCompany(f5, axarr5[1], data, 'INDUSIND BANK', chart_till)

f6, axarr6 = plt.subplots(2,1,figsize=(10,10))
plotCompany(f6, axarr6[0], data, 'SHREE CEMENTS', chart_till)
plotCompany(f6, axarr6[1], data, 'ACC', chart_till)
