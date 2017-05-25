#this program searches for just product na me before the IPO year for the firm. 
#inputs are from biotech ipo names
# it will look if a product will return any matches from teh clinical website (before IPO), then it will see if those matches are worth recording as data BEFORE IPO for
#firm X. It will look for company name, market matches, and therapeutic area matches. 
#output is 'new.txt'
from __future__ import division
import urllib
import string
import re
import requests
import itertools
import decimal
from decimal import *

Allergy_Immun=["immun","autoim","inflam","aller","asthm","5","allergy and immunology"]
Emergency=["acute","emergency","organ","critical","anest","9","emergency medicine"]
Antesiology=["critical","anest","migrain","pain","neuropathic","sedation","61","antesiology"]
Colon_Rectal=["intesti","prosta","bph","colon","rectal","polyps", "7","colon and rectal"]
Dermatology=["derma","skin","debrid","8","dermatology"]
Infectious_Int=["hbv", "hcv","vira","virus", "infecti","bacteria","antibiotic","23","infectious disease"]
Cardio_Int=["cardio","vascu","acute","strok","dvt","pvd","myocard","heart","cardiovas","thromb","arterial","hypertension","21","cardiology"]
Cancer_Int=["oncolo","metastatic","chemo","malignant","carcinoid","radia","prostate","tumor","stem","lymphoma","22","cancer"]
Metabolism_Endocinology_Int=["diabete","thyroid","endocri","metabo","insulin","lipid","hypothyro","hormone","24","metabolism_endocri"]
CriticalCare_Int=["organ","emergen","critical","trauma","injur","25","critical care"]
Gastronology_Int=["gastro","liver","ulcer","intestin","stomach","abdomina","bowel","26","gastronology"]
Hematology_Int=["blood","hematol","anemia","anemic","sickle","hemophil","leukemia","lymphoma","27","hematology"]
Nephrology_Int=["renal","kidney","urinary","28","nephrology"]
Pulmonary_Int=["pulmonar","lung","asthma","cardiopulm","respira","bronchitis","asthma","pneumonia","respira","29","pulmonary"]
Rheumatology_Int=["arthritis","joint","muscle","ligament","rheumat","musculoskeletal","20","rheumatology"]
Genetics=["heredita","genetics","genes","30","genetic"]
Neurology=["neurol","nervous","neuropathic","brain","psychi","cognitive","addict","central nervous","cns","stroke","parkinson","alzheimer","40","neuro"]
Nuclear_Medicine=["nuclear","radioactive","radio","tracers","50","nuclear_medicine","50","nuclear_medicine"]
Radiology=["radiopharm","imaging","radiology","ultrasound","electromagnetic","60","radiology"]
obstetrics_gynecology=["gyneco","obstet","reprodu","female","labor","pelvic","female","infertili","vagin","70","obstetrics_gynecology"]
opthamalogy=["ophthal","glaucoma","eye","retina","macular","vision","1","opthamalogy"]
otolaryngology=["neck","heari","sinus","reconstructive","2","Otolaryngology"]
urulogy=["urinary","urolog","bladder","incontinence","pelvic","3","urology"]
sleep_subspec=["sleep","insomnia","63","sleep_subspec"]
brook=["end"]
Record=[]

Main=[Allergy_Immun,Emergency,Antesiology,Colon_Rectal,Dermatology,Infectious_Int,Cardio_Int,Cancer_Int,Metabolism_Endocinology_Int,CriticalCare_Int,Hematology_Int,Nephrology_Int,Pulmonary_Int,Rheumatology_Int,Neurology,Genetics,Nuclear_Medicine,Radiology,obstetrics_gynecology,opthamalogy,otolaryngology,urulogy,sleep_subspec]
def SEC_function_count(id2,form_type,x):
	OpenFile2 = open(r"C:\Users\David\Desktop\ftp.txt",'r')
	lines1 = OpenFile2.readlines()
	contada=0
	for linesftp in lines1:
		print "now moved to the next line in ftp"
		id3 = linesftp.split(",")[0].lower().strip()
		year=linesftp.split(",")[2].lower().strip()
		form= linesftp.split(",")[1].lower().strip()
		id4=id2[-6:]
		id1=id2[-7:]
		print ("sic number:",id1,id2,id3)
		if id3=="end" :
			break
		if id4==id3  or id1==id3:
			print "found firm in ftp and now going to sec server"
			print form 
			
			sitename_1=linesftp.split(",")[3].strip().lower()
			sitename_1=sitename_1[36:]
			sitename_1=sitename_1[:-4]
		
			sitename_2= linesftp.split(",")[3].strip().lower()
			sitename_2=sitename_2[48:]
			sitename_2=sitename_2[:-11]
	
			sitename_3=linesftp.split(",")[3].strip().lower()
			sitename_3=sitename_3[51:]
			sitename_3=sitename_3[:-4]
		
			
			sitename = linesftp.split(",")[3].strip().lower()
			sitename=sitename[18:]
			sitename=sitename[:-14]
			sitename_final="https://www.sec.gov/Archives/"+sitename+sitename_2+sitename_3+sitename_1+"-index.htm"
			rr= requests.get(sitename_final)
			rrr=rr.content
			index=rrr.find("Archives")
			index_final=rrr.find(">",index+1)
			sitename_5="https://www.sec.gov/"+rrr[index:index_final-1]
			
			print sitename_5
			aa=requests.get(sitename_5)
			print (aa.url)
			
			path1="C:\Users\David\Desktop"+"_"+"seccsample"
			fff=open(path1,"w")
			
			fff.write(aa.content)
			fff.close()
			print("it wrote on the file.")
			rrr=open(path1,"r")
			fff=rrr.read()
			aaa=string.lower(fff)
			
			
			print ("this is the text its seraching",x)
			contada=Count(x,aaa)+contada
			print("this is the count for the text",contada)
	return contada 
	
			
												
class Particle:
    def __init__(self, drug, year, thera_count, firmname,sponsor_count,collab_count,market,intervention_count,phase):
		self.drug = drug
		self.year = year
		self.thera_count = thera_count
		self.firmname = firmname
		self.sponsor_count=sponsor_count
		self.collab_count=collab_count
		self.market=[]
		self.intervention_count=intervention_count
		self.phase=phase

def Count(x,secc):	
	if x==None:
		return 0
		
	x_1=x	
	original_length=len(x_1)
	x_count=secc.count(x_1)
	x_length=(len(x_1)/original_length)
	
	
	while x_count<2 and x_length>.5: #cuts its from the end of the word
		
		x_1=x_1[-(len(x_1)-1):]
		x_length=(len(x_1)/original_length)
		x_count=secc.count(x_1)
		

	x_1=x
	original_length=len(x_1)
	x_count_1=secc.count(x_1)
	x_length=(len(x_1)/original_length)
	while x_count_1<2 and x_length>.5: #cuts it from the beginning and searches
		
		x_1=x_1[:(len(x_1)-1)]
		x_length=(len(x_1)/original_length)
		x_count_1=secc.count(x_1)
	
	
	ttotal=x_count_1+x_count
	
	return ttotal
		
		
def Chemical_Func(sss):
	chemindex=sss.find("hit_syn")
	
	if chemindex>0:
		intervention=sss[chemindex+9:chemindex+20]
		return intervention

def Studyyear (sss):
	#looks for study year
	study_year_index=sss.find('first received: <span class=')
	study_year_final=sss.find('</span',study_year_index+30)
									
									
	
	study_year=sss[study_year_index+38:study_year_final]
	
	if study_year_index==-1:
		study_year=0
	return study_year 

def Therapeutic_function(sss,therapeutic): #returns the total amount of therapuetic matches 
	
	thera=sss.count(therapeutic)
	thera_1=therapeutic
	thera_length=len(thera_1)
	while thera==0 and thera_length>4: #cuts its from the end of the word
		thera_1=thera_1[-(thera_length-1):]
		thera_length=len(thera_1)
		thera=sss.count(thera_1)

	thera_0=sss.count(therapeutic)	
	thera_1=therapeutic
	thera_length=len(thera_1)
	
	while thera_0==0 and thera_length >4: #cuts it from the beginning and searches
		thera_1=thera_1[:(thera_length-1)]
		thera_length=len(thera_1)
		thera_0=sss.count(thera_1)
		
	
	return thera_0+thera
	
	#LOOKS FOR FIRM NAME
def	Firmname_function(sss,firm_name):
	firm_index=sss.find("sponsor")						
	firm_index1=sss.find("information provided by")
	firm=sss.find(firm_name,firm_index,firm_index1)
	firmlength=6
	while firm<0 and firmlength>5 : 
		firm_name=firm_name[:firmlength-1]
		firmlength=len(firm_name)
		firm=sss.find(firm_name,firm_index,firm_index1)
		if firm >0:
			return 1  #first weight labeled due to firm name 
		
		else:
			return 0
def Collect_sponsor(sss):										#gathers the collaborator and sponsor information but doesn't look for it in the sec files just yet. 
	
	collab_exist=sss.find('collaborator:</div>')
	if collab_exist>0 :
		collab_sponsor_index=sss.find('sponsors and collaborators')
		collab_sponsor_index1=collab_sponsor_index+82
		sponsor_end_index=sss.find('</div>',collab_sponsor_index1+8)
		sponsor=sss[collab_sponsor_index1:sponsor_end_index]
		
		collaborator_index=sss.find('<div class="info-text">',collab_exist+5)
		collaborator_index1=sss.find('</div>',collaborator_index+8)
		collaborator=sss[collaborator_index+23:collaborator_index1]
		collaborator=collaborator.strip().strip("\t")
		
		return sponsor 
	if collab_exist==-1:
		collab_sponsor_index=sss.find('sponsors and collaborators')
		collab_sponsor_index1=collab_sponsor_index+82
		sponsor_end_index=sss.find('</div>',collab_sponsor_index1+8)
		sponsor=sss[collab_sponsor_index1:sponsor_end_index]
	
		return sponsor								
	
def Collect_collaborator(sss):
	collab_exist=sss.find('collaborator:</div>')
	if collab_exist>0 :
		collab_sponsor_index=sss.find('sponsors and collaborators')
		collab_sponsor_index1=collab_sponsor_index+82
		sponsor_end_index=sss.find('</div>',collab_sponsor_index1+8)
		sponsor=sss[collab_sponsor_index1:sponsor_end_index]
	
		
		collaborator_index=sss.find('<div class="info-text">',collab_exist+5)
		collaborator_index1=sss.find('</div>',collaborator_index+8)
		collaborator=sss[collaborator_index+23:collaborator_index1]
		collaborator=collaborator.strip().strip("\t")
	
		return collaborator
	if collab_exist==-1:
		collaborator=None
		
def Drug_function(sss,drug1):
	#searches for drug name in intervention, returns 1. Else returns 0

	interindex=	sss.find("condition, intervention")
	interindex1=sss.find("study type")
	drug1=drug1.strip()
	interindex2=sss.find(drug1,interindex,interindex1)
	#looks to see if the product name from biotecch is in the intervention section of clinical trials
	if interindex2>0  :		  
		return 1
	else:
		return 0	
		
class Particle_1:
    def __init__(self, marketname,number,count):
		self.marketname= marketname
		self.number=number
		self.count=count
			
	
def _functioninsert(Array,number,text,totalcount):

	p=Particle_1(text,number,totalcount)
	print ("inside the _functioninsert function market number",p.number)
	Array.append(p)
	return Array
	
def _functionsort(Array):
	numberSize=len(Array)
	print numberSize	
	if numberSize==0:
		return Array	
	for num in range(0,numberSize-1): 
		indexbiggest=num
		for j in range(num+1,numberSize): 
			if (Array[j].count >= Array[indexbiggest].count):
				indexbiggest = j
				temp = Array[num]
				Array[num] = Array[indexbiggest]
				Array[indexbiggest] = temp
	
	
	return Array			
		
def Market_function(sss,market_number,market_number1,market_number2):
	weight3=0
	weight=0
	weight2=0
	Marketarray=[]

	for item in Main:#this the same market as listed
		totalcount=0
		Lista=item
		for position in Lista:
			if position.isdigit()==False:
				marketcount=sss.count(position)
				totalcount=marketcount+totalcount
				print(totalcount,position)
		if totalcount>3 :
			weight3=Lista[-2]
			weight_word=Lista[-1]
			Marketarray=_functioninsert(Marketarray,weight3,weight_word,totalcount)
			
			
	Marketarray=_functionsort(Marketarray);		
	return Marketarray


def _sorting(record,market_number,market_number1,market_number2,market_length):
#eliminates the ones that dont suggest any relevance to this drug
	
	numberSize=len(record)
	del record[numberSize-1]
	print ("This is the array size",numberSize)
	num=0
	while num<numberSize-1:
		print ("this is the the index in array ",num)
	
		if not record[num].market:
			break
		if record[num].firmname==0 and record[num].intervention_count==0 and record[num].drug==0 and record[num].thera_count<3 and record[num].market[0].number!=market_number and record[num].market[0].number!=market_number1 :
			print ("deleted this one", num)
			del record[num] 
			num=0
			numberSize=len(record)
		else :
			num+=1
	
		
	#orders by therapteutic count		
	numberSize=len(record)
		
	if numberSize==0:
		return record	
	for num in range(0,numberSize-1): 
		indexbiggest=num
		for j in range(num+1,numberSize): 
			if (record[j].thera_count >= record[indexbiggest].thera_count):
				indexbiggest = j
				temp = record[num]
				record[num] = record[indexbiggest]
				record[indexbiggest] = temp
				
				
				
	#orders by the sum of therapetuic count sponsor count collab count intervention count
	
	
	numberSize=len(record)
	
	if numberSize==0:
		return record
	for num in range(0,numberSize-1): 
		Suma=record[num].thera_count+record[num].sponsor_count+record[num].collab_count+record[num].intervention_count
		indexbiggest=num
		for j in range(num+1,numberSize): 
			Suma_1=record[j].thera_count+record[j].sponsor_count+record[j].collab_count+record[j].intervention_count
			if (Suma_1 >= Suma):
				indexbiggest = j
				temp = record[num]
				record[num] = record[indexbiggest]
				record[indexbiggest] = temp
				
				
#puts the drug matches first			
	numberSize=len(record)
	for num in range(0,numberSize-1):
		firstindex=num
		for j in range(num+1,numberSize):
			if record[j].drug==1:
				
				temp=record[num]
				record[num]=record[j]
				record[j]=temp
		
		

	
		
	return record
def Write_file(Record_Sorted,market_number,market_number1,market_number2,length_market):
	
	digit=len(Record_Sorted)
	print("length of array",digit)
	OpenFile_1= open("C:\\Python27\\new.txt", 'a')
	yy=0;
	while (yy<digit-1):
		print ("this is iteration",yy)
		print ("this is the year in the sort", Record_Sorted[yy].year)
		print ("this is the phase in the sort", Record_Sorted[yy].phase)
		print ("This is one was written", Record_Sorted[yy].market[0].marketname,Record_Sorted[yy].market[0].marketname)	
		OpenFile_1.write('%s%s%s%s%s%s%s%s%s%s%s'%('\n',line.rstrip('\n'),Record_Sorted[yy].market[0].number,",",Record_Sorted[yy].year,",",Record_Sorted[yy].phase,",",drug1,",",Record_Sorted[yy].market[0].marketname))	
		
		yy+=1;
	OpenFile_1.close()		
	return 0	

			
OpenFile = open(r"C:\Python27\new.txt","r")
lines = OpenFile.readlines()

Outfile1= open("C:\\Python27\\new.txt", 'a')
op=1
for line in lines:
	if op==1:
		id2 = line.split(",")[0].strip('\t').lower()
		power=id2	#so that the file path only has the original company name and not several shortned versions of the company name
		print id2
		search=1
		syntax=1
		firm_name=line.split(",")[1].strip('\t').lower()
		form_type = line.split(",")[2].strip('\t').strip().lower() 
		print form_type
		product_1= line.split(",")[5].strip('\t').strip('""').lower()
		print product_1	
		form_year=line.split(",")[3].strip('\t')
		print form_year
		therapeutic=line.split(",")[6].strip('\t').strip('""').lower()
		print therapeutic
		form_year1=line.split(",")[4].strip("\t")
		market_number=line.split(",")[7].strip('\t')
		market_number1=line.split(",")[8].strip('\t')
		market_number2=line.split(",")[9].strip('\t')
		
		drug1=product_1
		p=0
		
		
		for i in drug1:											#Cleans the product names from unwanted charetevers 
			if ord(i)>128 :
				drug1=drug1.replace(i,"").strip(i).strip()	
				
		x_original=len(drug1)
		
		x=len(drug1)		#establishes an 'original' length so taht the while loop stops once the percentage decrease is too much and youre gonna return too many matches	
		
		Percentage_D=(x)/(x_original)

		
		for girl in brook	:			#it looks in the memory and checks if 
			
			if girl==drug1 and girl!="end" :
				print ("found a match already in memory", drug1)
				break
			if girl=="end":	
				print "starts the while"
				
				while search>0 and Percentage_D>.60 or syntax>0 and Percentage_D>.60 :	#searches for drug until the length is to short
					print ("Drug name searched for",drug1)
					print form_year
					website = 'https://clinicaltrials.gov/ct2/results?'
					data={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
					r = requests.get(website, params=data,verify=False)
					print(r.url)
					filepath="C:\Users\David\Desktop"+ power+"_"+form_year+"_"+"clinicaltrials"
					print filepath
					f=open(filepath,"w") 
					f.write(r.content)
					f.close()	
					r=open(filepath, "r")
					s=r.read()
					x=len(drug1)															
					search=s.find("no studies found")			#looks for 0 studies
					syntax=s.find("syntax")
					print search
					print syntax
					if search==-1 and syntax==-1 :											#if it found result (s)
						print "print found a match"
						length9=len(brook)-1							#stores the drug in the memory if it found matches in clinical server
						brook.insert(length9,drug1) 
						print brook
						beg=s.find("results-summary")
						end=s.find("studies found for")				#how many studies have been found?
						if end==-1 :
							end=s.find("study found for")
						
						range_numbers=s[beg:end]
						for i in range_numbers:
							if i.isdigit():
								print ("This is the nth clinical trial study report",i)
								website = 'https://clinicaltrials.gov/ct2/results?'   #this just copies the texxt and copies it on a file
								data={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
								rr= requests.get(website, params=data,verify=False)
								path="C:\Users\David\Desktop"+ "clinicaltrialstest"+"_"+"sample"+"_"+"clinicaltrials"
								ff=open(path,"w") 
								ff.write(rr.content)
								ff.close()
								rr=open(path, "r")
								ss=rr.read()
								xx=0
								index1=0
								index=0
								while index !=-1:
									
									phase=0
									study_year=0
									index=ss.find("Show study",index1)		#looks for the NC code in order to ask for it and get the full lab report
									print ('index found', index)
									code=ss[index+11:index+22]
									print code
									site='https://clinicaltrials.gov/ct2/show/'+code+ '?'
									data1={"term":"","recr":"","rslt":"","type":"","cond":"","intr":drug1,"titles":"","outc":"","spons":"","lead":"","id":"","state1":"","cntry1":"","state2":"","cntry2":"","state3":"","cntry3":"","locn":"","gndr":"","rcv_s":"","rcv_e":"12/30/"+form_year,"lup_s":"","lup_e":""}
									cc=requests.get(site,params=data1,verify=False)
									print (cc.url)
									path1="C:\Users\David\Desktop"+ power+"_"+"actuallabreport"+"_"+"clinicaltrials"
									fff=open(path1,"w")
									fff.write(cc.content)
									fff.close()
									rrr=open(path1,"r")
									fff=rrr.read()
									sss=string.lower(fff) #SSS should be the input for a lot of functions
									ttt=string.lower(fff)
									
									#looks for phase
									phase_index=sss.rfind('<td class="body3" nowrap>')
									print ("phase index", phase_index)
									phase=sss[phase_index+26:phase_index+50]
									phase=phase.strip().strip("\t")
									test=phase
									while test!="phase" and len(test)>2:
										test=test[:-1]
										
									if test=="phase":
										print ("found phase",phase)
									else:
										phase=0
										#it starts the function calls right now
									study_year=Studyyear(sss);
									print ("study year",study_year)
									therapeutic_count=Therapeutic_function(sss,therapeutic);
									print ("therapuetic matches",therapeutic_count)
									sponsor=Collect_sponsor(sss);
									print("sponsor", sponsor)
									collab=Collect_collaborator(sss);
									print("collaborator", collab)
									drug=Drug_function(sss,drug1);
									print ("drug found in intervention section of clinilca trial?",drug)
									market=Market_function(sss,market_number,market_number1,market_number2);
									print("market match",market)
									firmname=Firmname_function(sss,firm_name);
									print ("firm found?",firmname)
									intervention= Chemical_Func(sss);
									print ("this is the chemeical name:",intervention)
									
									print ("looking for this sponsor", sponsor);
									sponsor_count=SEC_function_count(id2,form_type,sponsor);
									
									collab_count=SEC_function_count(id2,form_type,collab);
									intervention_count=SEC_function_count(id2,form_type,intervention);
									
									p = Particle(drug,study_year,therapeutic_count,firmname,sponsor_count,collab_count,market,intervention_count,phase)
									
									Record.append(p)
									
									
									
									
									index1=index+15
								
						
						
						
						
						
						
						
								
								length_market=len(market)
								Record_Sorted=_sorting(Record,market_number,market_number1,market_number2,length_market);
								length_market=len(Record_Sorted)
								Write_file(Record_Sorted,market_number,market_number1,market_number2,length_market);
								Record=[]		
					drug1=drug1[:x-1]	
					x=len(drug1)			
					Percentage_D=(x)/(x_original)
					Final=Decimal(Percentage_D)
					print ("original length in loop",x_original)
					print ("length of the word in loop",x)
					print  '%.11f' % Final
					
			
OpenFile.close()	