#include <Python.h>


from __future__ import division
import urllib
import string
import re
import requests
import itertools
import decimal
from decimal import *

from collections import deque
#file that gets read it is both POST AND Pre IPO. PRe IPO information is on "Razvan_Pre.txt file" . POSTIPO information
#is on POSTIPORazvan.txt
#  Both sets of information are incomplete, you must make sure when you run the program that these files
#is complete with ALL Post IPO information (from the excel sheet inputforidontknow) and all pre ipo information
#is on excel sheet("Output List")
 
 
class Particle:
    def __init__(self, id, year, form_type, firmname,product_Name,phase,market_code):
		self.id = id
		self.year = year
		self.form_type = form_type
		self.firmname = firmname
		self.phase=phase
		self.product_Name=product_Name
		self.marketCode=market_code
		self.tricks = []  
		#tricks array contains other preclinical studies, starting from the most dependable first, least is last. 
class Post:
    def __init__(self, id, year, form_type, firmname,product_Name,phase,market,collaborator,collaboration,market_Code1,market_Code2,market_Code3,product_change):
		self.id = id
		self.year = year
		self.form_type = form_type
		self.firmname = firmname
		self.phase=phase
		self.product_Name=product_Name
		self.market=market
		self.collaborator=collaborator
		self.collaboration=collaboration
		self.market_Code1=market_Code1
		self.market_Code2=market_Code2
		self.market_Code3=market_Code3
		self.Product_Change=product_change
		self.tricks_1=[]
		#this tricks arraay contains the product information for the future years.
		
			

		
	
def Test(string,List):
	
	for y in List:
		count=0
		if string==y.id:
			
			for index in y.tricks:
				print ("Information on company:",index.id)
				print("PRoduct",index.phase)
				print("market code", index.product_Name)
				count += 1
			print ("count for this product",count)		

def Print_column_Post(Node,File):	
	
	File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',Node.id,",",Node.year,",",Node.form_type,",",Node.firmname,",",Node.product_Name,",",Node.phase,",",Node.market_Code1,",",Node.market_Code2,",",Node.market_Code3))
	
	for i in Node.tricks_1:
		File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',i.id,",",i.year,",",i.form_type,",",i.firmname,",",i.product_Name,",",i.phase,",",i.market_Code1,",",i.market_Code2,",",i.market_Code3))

		
def Print_column_Pre(Node,File,tolerance):	
	
	File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',Node.id,",",Node.year,",","Pre-IPO",",",Node.firmname,",",Node.product_Name,",",Node.phase,",",Node.marketCode))
	print("tolerance",tolerance)
	for i in range(0,tolerance-1):
		File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',Node.tricks[i].id,",",Node.tricks[i].year,",","Pre-IPO",",",Node.tricks[i].firmname,",",Node.tricks[i].product_Name,",",Node.tricks[i].phase,",",Node.tricks[i].marketCode))	
		print ("index", i)
		
#the below function will print each product and its history, before moving on to the next product of the firm's product line		
def Print_Entire_Product(Pre,Post,Directory,tolerance):
	
	
	OpenFile_1= open(Directory, 'a')
	print("inside",Directory)
	for j in Post:
		tol=int(tolerance)
		tol=(tol/10)
	
		for i in Pre:
			
			if j.product_Name==i.product_Name and j.id==i.id:
				
				tol=tol*len(i.tricks)
				tol=int(tol)
				print("tolerance",tol)
				print("product name",i.product_Name)
				Print_column_Pre(i,OpenFile_1,tol)
				tol=int(tolerance)
				tol=(tol/10)
		Print_column_Post(j,OpenFile_1)
			
	OpenFile_1.close()		
	
def Search_Begin_End(List,Begin,File):
	Year=List[Begin].year
	ID=List[Begin].id
	i=0
	while ((Begin+i)<len(List) and List[Begin+i].id== ID):
		#print("comparing during search",List[Begin+i].product_Name)	
		i+=1
		
		#print everything from Begin to i-1
			
	return Begin+ i-1	
	
def Print_Following_years(List,Start,End,File):
	Year=List[Start].year
	print("this should be it" ,List[End].product_Name)
	while(Year<=2015):		
		print("year",Year)
		for i in range(Start,End+1):
			print("compares at head",List[i].product_Name)
			if List[i].year==Year:
				print("prints b/c of head",List[i].product_Name)
				File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',List[i].id,",",List[i].year,",",List[i].form_type,",",List[i].firmname,",",List[i].product_Name,",",List[i].phase,",",List[i].market_Code1,",",List[i].market_Code2,",",List[i].market_Code3,",","First"))
			for j in range(0,len(List[i].tricks_1)):
				print("compares with node",List[i].tricks_1[j].product_Name)
				if List[i].tricks_1[j].year==Year:
					print("printing product",List[i].tricks_1[j].product_Name,"printing this year",List[i].tricks_1[j].product_Name)
					File.write('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%('\n',List[i].tricks_1[j].id,",",List[i].tricks_1[j].year,",",List[i].tricks_1[j].form_type,",",List[i].tricks_1[j].firmname,",",List[i].tricks_1[j].product_Name,",",List[i].tricks_1[j].phase,",",List[i].tricks_1[j].market_Code1,",",List[i].tricks_1[j].market_Code2,",",List[i].tricks_1[j].market_Code3,",","Top"))
		
		Year+=1	
	return End+1		
	
def Print_Entire_Year(Pre,Post,Directory, tolerance):
	tolerance=int(tolerance)
	print("tolerance here",tolerance)
	tolerance=(tolerance/10)
	tolerance=int(tolerance)
	OpenFile_1= open(Directory, 'a')
	End=Search_Begin_End(Post,0,OpenFile_1)
	new=Print_Following_years(Post,0,End,OpenFile_1)
	print("Original End",End,"Original Start",new)
	print("length of Post Ipo",len(Post))
	while (End<len(Post)-1):
		
		End=Search_Begin_End(Post,new,OpenFile_1)
		print("end",End)
		new=Print_Following_years(Post,new,End,OpenFile_1)
		print("start",new)
		
	OpenFile_1.close()
		
	
	
     
OpenFile = open(r"C:\Users\David\Desktop\Razvan_Pre.txt","r")

lines = OpenFile.readlines()

Record=[]
for line in lines:
	if line.count(",")!=16:
		print ("BROKE BECAUSE COMMAS")
		break
	#print "new line"
	a=0
	id = line.split(",")[0].strip('\t').lower()

	#print ("id",id)
	firm_name=line.split(",")[1].strip('\t').lower()
	#print firm_name
	form_type = line.split(",")[2].strip('\t').strip().lower() 
	#print ("form type",form_type)
	
	year= line.split(",")[12].strip('\t').strip('""').lower()
	year=int(year)
	#print ("year",year)
	phase=line.split(",")[13].strip('\t').strip('""').lower()
	#print ("phase",phase)	
	product=line.split(",")[5].strip('\t').strip('""').lower()
	product=product.replace("\xa0", " ")
	product=product.replace("\xae"," ")
	product=product.replace("\x92"," ")
	product=product.replace("\x99"," ")
	#print ("product",product)
	form_year=line.split(",")[3].strip('\t')
	#print ("form-year",form_year)
	market_code=line.split(",")[10].strip('\t').strip('""').lower()
	#print ("market code",market_code)
	
	
	p = Particle(id,year,form_type,firm_name,product,phase,market_code)
	
	for x in Record:
		if x.id==p.id:
			#print("compared to ",x.id)
			if x.product_Name==p.product_Name:
				#print("inserted as top",p.product_Name)
				a=1
				x.tricks.append(p)
	if a!=1:	
		#print("inserted as new block product name",p.product_Name)
		Record.append(p)


OpenFile = open(r"C:\Python27\PostIPOInput.txt","r")

lines = OpenFile.readlines()

Post_1=[]
for line in lines:
	if line.count(",")!=16:
		print ("BROKE BECAUSE COMMAS")
		break
	
	b=0
	id = line.split(",")[0].strip('\t').lower()

	print ("id",id)
	firm_name=line.split(",")[1].strip('\t').lower()
	
	#print firm_name
	technology=line.split(",")[7].strip('\t').strip().lower()
	technology=technology.replace("\xa0", " ")	
	technology=technology.replace("\x92"," ")
	#print ("technology",technology)
	collaborator=line.split(",")[10].strip('\t').strip().lower() 
	collaborator=collaborator.replace("\xa0", " ")
	collaborator=collaborator.replace("\x92"," ")
	#print ("collaborator",collaborator)
	collaboration=line.split(",")[11].strip('\t').strip().lower() 
	collaboration=collaboration.replace("\x92"," ")
	#print ("collaboration type",collaboration)
	form_type = line.split(",")[2].strip('\t').strip().lower() 
	#print ("form type",form_type)
	therapetic=line.split(",")[9].strip('\t').strip('""').lower()
	therapetic=therapetic.replace("\xa0", " ")
	therapetic=therapetic.replace("\x92"," ")
	#print("thera",therapetic)
	year= line.split(",")[4].strip('\t').strip('""').lower()
	year=int(year)
	print ("year",year)
	phase=line.split(",")[6].strip('\t').strip('""').lower()
	phase=phase.replace("\xa0", " ")
	#print ("phase",phase)	
	product=line.split(",")[5].strip('\t').strip('""').lower()
	product=product.replace("\xa0", " ")
	product=product.replace("\x92"," ")
	product=product.replace("\x99"," ")
	product=product.replace("\xae"," ")
	#print ("product",product)
	form_year=line.split(",")[3].strip('\t')
	#print ("form-year",form_year)
	market=line.split(",")[8].strip('\t').strip('""').lower()
	market=market.replace("\xa0", " ") 
	market=market.replace("\x92"," ")
	#print ("market",market)		
	market_Code1=line.split(",")[12].strip('\t').strip('""').lower()
	print ("market code 1",market_Code1)
	market_Code2=line.split(",")[13].strip('\t').strip('""').lower()
	#print ("market code 2",market_Code2)
	market_Code3=line.split(",")[14].strip('\t').strip('""').lower()
	#print("market code 3",market_Code3)
	product_change=line.split(",")[15].strip('\t').strip('""').lower()
	
	
	q = Post(id,year,form_type,firm_name,product,phase,market,collaborator,collaboration,market_Code1,market_Code2,market_Code3,product_change)
	for i in Post_1:
		if i.id==q.id:
			if i.product_Name==q.product_Name:
				i.tricks_1.append(q)
				print ("inserted at top",q.product_Name)
				b=1
	if b!=1:	
		print("inserted as new block product name",q.product_Name)
		Post_1.append(q)			
	
str= raw_input("Type in the function you would like to call: ");
	
if str=="Print by Product":
	str_1 = raw_input("Type the directoy you would like to data to be printed( e.g. C:\MyDocuments\Razvan.txt) : ")
	str_2=raw_input("Type the pre clincical tolerance(1-10). 10-All Clinical trials will be printed , 1-Only the most relevanat clinical trials will be outputed: ")
	Print_Entire_Product(Record,Post_1,str_1,str_2)

if str=="Print by Year":	
	str_1 = raw_input("Type the directoy you would like to data to be printed( e.g. C:\MyDocuments\Razvan.txt) : ")
	str_2=raw_input("Type the pre clincical tolerance(1-10). 10-All Clinical trials will be printed , 1-Only the most relevanat clinical trials will be outputed: ")
	Print_Entire_Year(Record,Post_1,str_1, str_2)
									
#Record.append(p)