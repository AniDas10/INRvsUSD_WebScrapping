import matplotlib.pyplot as plt
import csv
import pandas as pd

df = pd.read_csv('currency.csv')

inr=df[df.columns[3]]
date=df[df.columns[1]]
data_set={'date':date,'INR':inr}
final_dataframe = pd.DataFrame(data_set)
final_dataframe.set_index('date', inplace=True)
final_dataframe.to_csv('currency_v2.csv', header=True)

#file = open('currency_v2.csv','w+')
#print(file)
filename = "currency_v2.csv"
  
# initializing and rows list 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    #print("Total no. of rows: %d"%(csvreader.line_num)) 
  
xaxis=[]
yaxis=[]  

#replace 10 with any number acc to your convenience 
for row in rows[1:10]: 
    # parsing each column of a row 
    xaxis.append(row[0]) 
    yaxis.append(row[1][:6])

#print(xaxis)
#print(yaxis)
plt.title('1 USD vs INR')
plt.plot(xaxis, yaxis)
plt.xlabel('Day-wise analysis')
plt.ylabel('1 USD in Indian Rupees')
plt.legend()
plt.show()
