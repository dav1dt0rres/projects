#This will manipulate the variableles create quantatiative measure for inputs into the classification tree. Including time is a huge INPUT
#This includes teh actual classification tree algorithm
#Remember, time is a vector into the algorithm
import urllib
import string
import re
import requests
import itertools


#you need numpy for sklearn
#you need scipy, for numpy.
#and you need blas/laplack http://ab-initio.mit.edu/wiki/index.php/Template:Installing_BLAS_and_LAPACK
#import code for LVCS Machine Learning https://pythonprogramming.net/linear-svc-example-scikit-learn-svm-python/



OpenFile = open("C:\Python27\dav1dt0rres.txt","r")
lines = OpenFile.readlines()
for i in range(0,len(lines)):
	line=lines[i]
	
	id2 = line.split(";")[0].lower()
	print id2
	firm_name=line.split(";")[1].strip('\t').lower()
	form_type = line.split(";")[2].strip('\t').strip().lower() 
	product_original= line.split(";")[5].strip('\t').strip('()').strip('""').lower()
	year_0=line.split(";")[3].strip('\t').strip().lower()
	year_0=int(float(year_0))
	technology=line.split(";")[7].strip('\t').strip().lower()
	year_1=line.split(";")[4].strip('\t').strip().lower()
	year_1=int(float(year_1))
	year=year_1-year_0
	
	product_1=product_1.strip('\t\n\r')
	
	print firm_name 
	print product_1
	print year
	print technology
	for x in range(i+1,len(lines)):
		linea=lines[x]
		id_0=linea.split(";")[0].strip('\t')
		year_f=linea.split(";")[4].strip('\t').strip().lower()
		year_f=int(float(year_f))
		if id_0 == id2 :
			if year_f!=year_1:
			difference=x-i
			for y in range(i,i+difference)
			List=[]
			#here it confirmed that the year and company is the same, so it will gather information here about that year.
			product_f= line.split(";")[5].strip('\t').strip('()').strip('""').lower()
			
		if id_0!=id2:
			break
			
	
			
	
	
	