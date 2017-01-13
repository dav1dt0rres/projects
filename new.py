import urllib
import string
import re
import os
import select

OpenFile = open(r"C:\Python27\new1.txt","r")
lines = OpenFile.readlines()
tt=[500,1000]
productsrange=[4,5,6,7,8,9,10]
Allergy_Immun=["immun","autoim","inflam","aller","asthm","allergy and immunology"]
Emergency=["acute","emergency","organ","critical","anest","emergency medicine"]
Antesiology=["critical","anest","migrain","pain","neuropathic","sedation","antesiology"]
Colon_Rectal=["intesti","prosta","bph","colon","rectal","polyps", "colon and rectal"]
Dermatology=["derma","skin","debrid","dermatology"]

Infectious_Int=["hiv","hbv", "hcv","vira","virus", "infecti","bacteria","antibiotic","infectious disease"]
Cardio_Int=["cardi","vascu","acute","strok","dvt","pvd","myocard","heart","cardiovas","thromb","cardiology"]
Cancer_Int=["oncolo","chemo","radia","prostate","tumor","stem","lymphoma","cancer"]
Metabolism_Endocinology_Int=["diabete","thyroid","endocri","metabo","lipid","hypothyro","metabolism_endocri"]
CriticalCare_Int=["organ","emergen","critical","trauma","injur","critical care"]

Main=[Allergy_Immun,Emergency,Antesiology,Colon_Rectal,Dermatology,Infectious_Int,Cardio_Int,Cancer_Int,Metabolism_Endocinology_Int,CriticalCare_Int]

#0 to 6 is infectious disease, 7 to 10 is Cancer, 11 to 15 is allergy 
for line in lines:
	for o in productsrange:
		t=0
		id2 = line.split(",")[0].strip('\t').lower()
		print id2
		form_type = line.split(",")[1].strip('\t').lower() 
		print form_type
		form_year = line.split(",")[2].strip('\t').lower() 
		print form_year
		localfile = line.split(",")[3].strip('\t').lower()
		print localfile
		product_1= line.split(",")[o].strip('\t').lower()
		print o
		if len(product_1)==0 or product_1=="," :
			break
		else: 
			print product_1
		
		filepath="C:\Users\David\Desktop" + id2+"_"+form_year+"_"+form_type
		print filepath
	
		drug1=product_1
		p=0
		for i in drug1:											#Cleans the product names from unwante charetevers 
			while ord(i)>128 and p<15 :
				drug1=drug1.replace(i,"").strip(i).strip()
				p=p+1
		print drug1
		try:
			f=open(filepath, "r")	
			s=f.read()
			if form_type== "10-k" or form_type== "10-k405":			#finds when to start looking for keywords and when to stop
				print "found 10-K"
				begin="business"
				end="government regulation"
				indexlimit= 4000
				index=s.find(begin)
				index1=s.find(end)
			
			else:
				begin="liquidity and capital resources"
				end="risk factors"
				indexlimit=30000
				index= s.rfind(begin)
				index1= s.find(end)
			
			print index
			print index1
			while index1-index < indexlimit :
				index1=s.find(end,index1)
				if index1== -1:
					break
				print index1
				index1+=15
			
			index0=index1
			product1=s.count(drug1,index,index1)
			x=10											#counts how many prouct mentions, used to determine lead product and etc between the start and end...
			while product1<5:
				index0=index0+3000
				product1=s.count(drug1,index,index0)
				print ("how many times product found", product1)
				if index0>700000 and x<=7:
					break
				if index0> 700000  :
					x=len(drug1)
					while x>7:
						drug1=drug1[1:x-1]					#this part will clip the ends and restart the search for the shorter version of the product
						print ("new search for drug1", drug1)
						x=len(drug1)
						index0=index1
						break
					
				
				
			if product1>=5 or index0>700000 :			#here if it found it more than 5 times between the indexes, than finds the markets
				drug1index=s.find(drug1,index,index0)
			
				while drug1index<index0 :
					drug1index=s.find(drug1,drug1index+15,index0)
					print ('found drug1 at the index', drug1index)
					for range in tt:
						for  item in Main:
							totalcount=0
							lista=item
							for position in lista:
								
								market1count=s.count(position,drug1index-range,drug1index+range)
								thera1 = s.count('therapeutic',drug1index-range,drug1index+range)
								thera2=s.count('thera',drug1index-range,drug1index+range)
								thera3=s.count('treament', drug1index-range,drug1index+range)
								diag1=s.count('diagnostic', drug1index-range,drug1index+range)
								
								print (range,position,market1count)
								
								totalcount=market1count+totalcount
								market1count=0
							if totalcount>2 :	
								Outfile1 = open("C:\Python27\count.txt", 'a')
								Outfile1.write(id2+"\t"+form_type+"\t"+ form_year+"\t"+"%d"%thera1+"\t"+"%d"%thera2+"\t"+"%d"%thera3+"\t"+"%d"%diag1+"\t"+ "%d"%totalcount+"\t"+"%d"%range+"\t"+position + "\t"+ drug1+"\n")
					if drug1index>700000 or drug1index==-1 :
						break
					
		except IOError:
			print 9


		
OpenFile.close()
