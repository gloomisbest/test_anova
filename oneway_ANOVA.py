# coding:utf-8

import pandas as pd
from scipy import stats
import csv
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy.stats import levene
import os



def ANOVA_test(args1):
    w, p = stats.levene(*args1)
    if p < 0.05:
        print "方差齐性不成立"
    else:
        print "方差齐性成立"
        f, p1 = stats.f_oneway(*args1)
        # print f, p1
        return f, p1

def Data_test(str1, str2,str_Group):
    data = pd.read_csv(str1)
    G_data = data[data[str_Group] == 1][str2]
    C_data = data[data[str_Group] == 2][str2]
    args1 = [G_data, C_data]
    sumG = 0
    sumC = 0
    for i in G_data:
        sumG = sumG+i
    Average_G = sumG/len(G_data)
    for i in C_data:
        sumC = sumC+i
    Average_C = sumC/len(C_data)
    #print Average_G,Average_C
    return args1,Average_G,Average_C

# noinspection SpellCheckingInspection
def Get_row(str_f):
    with open(str_f, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for i, rows in enumerate(reader):
            if i == 0:
                row = rows
    #print row
    return row

def Levene_test(Csv,str_Group):
    with open(Csv, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row[str_Group] for row in reader]
        column = list(set(column))
        sum_column = len(column)

    print sum_column

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

#Csv = raw_input("Please input the csv_file:")
#Csv = Csv+'.csv'
str_Group = raw_input('Please input the Comparison group:')
i = Get_row(Csv)
# print i
i = i[2:]
# print i
data = pd.read_csv(Csv)
print data.head()


for n in i:
    print n
    data1 = data[data[str_Group] == 1][n]
    data2 = data[data[str_Group] == 2][n]
    w,p = levene(data1,data2)
    #a = Levene_test(Csv,str_Group)
    if p > 0.05:
        print n,'数据方差齐性。'
        fo_str = str_Group + '~ ' + n + ' '
        # print fo_str
        formula = fo_str
        anova_results = anova_lm(ols(formula, data).fit())
        print '----------------------------------------------------------------------------'
        print anova_results
        print '----------------------------------------------------------------------------'
        anova_results.to_csv('data_anova.csv', mode='a')
    else:
        print n,'数据方差不齐性。'
        
        
'''
for n in i:
    if n != 'learning_condition_post-test':
        print n
        args,Average_G,Average_C = Data_test(Csv, n, str_Group)
        # print args
        f, p1 = ANOVA_test(args)
        print 'GroupG_Average =',"%.2f" %Average_G,'  GroupC_Average =',"%.2f" %Average_C
        print 'F =', "%.2f" %f, 'P =', "%.3f" %p1
        if 0.01 < p1 < 0.05:
            print n, "显著*"
        elif p1 < 0.01:
            print n, "显著**"
        else:
            print n, "不显著"
        print '--------------------------'
    elif n == 'learning_condition_post-test':
        pass
#print "%.2f" % a
'''
