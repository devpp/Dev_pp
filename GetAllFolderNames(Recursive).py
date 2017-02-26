# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:59:17 2017

@author: Purush
"""
import os, csv

filetowrite = input("Enter the path where you want to print the Results :")
#f.close()
## delete only if file exists ##
if os.path.exists(filetowrite + '\Results.csv'):
    os.remove(filetowrite + '\Results.csv')
else:
    #print("Sorry, I can not remove %s file.")
    
    with open(filetowrite + '\Results.csv', 'w') as fw:
        fw.close()

filepath = filetowrite + '\Results.csv'

f = open(filepath, "w+")
f.close()
f=open(filepath,'r+')
w=csv.writer(f)
dirtoscan = input("Enter the directory that has to be scanned (ex : drive:/folder/):")
i = 1
for path, dirs, files in os.walk(dirtoscan):
    for filename in dirs:
        item =str(i) + '|' + filename  + '|' + path
        print (item) 
        w.writerow([item])
        #w.writerow([path])
        i += 1
f.close()
print("The extract is complete!!!" + "check file %s",filetowrite + '\Results.csv')
