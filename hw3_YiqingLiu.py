# homework3
# python classes
# author @ Yiqing Liu

# Question 1: Create a line plot showing the number of marriages and divorces per capita in the U.S. between 1867 and 1880
# Question 2: Create a line plot showing the number of marriages and divorces per capita in the U.S. between 1875 and 1881



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Dataset:
	def __init__(self,filepath):
		self.data=pd.read_csv(filepath)
		self.index=1
	def lineplot(self,data,x_column,y_column,color,title):
		fig = plt.figure()
		
		for index in range(len(y_column)):
			y=data[y_column[index]]
			x=data[x_column[index]]
			l=plt.plot(x,y,color[index])
		plt.title(title)
		plt.legend()
		plt.savefig('/Users/yiqingliu/Google Drive/IS590DV/hw3/'+str(self.index)+'.png')
		self.index=self.index+1

	def contional_lineplot(self,x_column,y_column,color,title,compare_column,start_date,end_date):
		data=self.data[self.data[compare_column]>=start_date]
		data=data[data[compare_column]<=end_date]
		self.lineplot(data,x_column,y_column,color,title)

def main():
	d=Dataset("us-marriages-divorces-1867-2014.csv")
	d.contional_lineplot(['Year','Year'],['Marriages_per_1000','Divorces_per_1000'],['r--','g--'],'Marriages rate & Divorce rate from 1869 to 1880','Year',1869,1880)
	d.contional_lineplot(['Year','Year'],['Marriages_per_1000','Divorces_per_1000'],['r--','g--'],'Marriages rate & Divorce rate from 1875 to 1881','Year',1875,1881)

	
if __name__=='__main__':
	main()