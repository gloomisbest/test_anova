#coding:utf-8
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd
from scipy.stats import ttest_ind
from scipy.stats import levene
import os


while True:
    Csv = raw_input("Please input the csv_file:")
    Csv = Csv + '.csv'
    if os.path.exists(Csv) == True:
        i = pd.read_csv(Csv)
        # print i.head()
        break
    else:
        print 'Csv_files not found!!'
        continue

formula = 's~ g + pp + g:pp '
anova_results = anova_lm(ols(formula,i).fit())
print '----------------------------------------------------------------------------'
print anova_results
print '----------------------------------------------------------------------------'

a = 3.021561e-02
b = 2.241421e-12
d = 9.495854e-01

print "%.3f" %a,"%.3f" %b,"%.3f" %d

G_group = i[i['g'] == 1]
C_group = i[i['g'] == 2]
#print G_group.head(),C_group.head()

x1 = G_group[G_group['pp'] == 1]['s']
y1 = G_group[G_group['pp'] == 2]['s']
x2 = C_group[C_group['pp'] == 1]['s']
y2 = C_group[C_group['pp'] == 2]['s']

print levene(x1,y1)
print ttest_ind(x1,y1, equal_var=True)
c1 = 4.535266245329503e-06
print 'p =',"%.3f" %c1
print '----------------------------------------------------------------------------'
print levene(x2,y2)
print ttest_ind(x2,y2, equal_var=True)
c2 = 2.19580320561406e-07
print 'p =',"%.3f" %c2

