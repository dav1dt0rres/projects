#this program searches for just product na me before the IPO year for the firm. 
#inputs are from biotech ipo names
# it will look if a product will return any matches from teh clinical website (before IPO), then it will see if those matches are worth recording as data BEFORE IPO for
#firm X. It will look for company name, market matches, and therapeutic area matches. 
#output is 'new.txt'

import urllib
import string
import re
import requests
import itertools
Allergy_Immun=["immun","autoim","inflam","aller","asthm","5","allergy and immunology"]
Emergency=["acute","emergency","organ","critical","anest","9","emergency medicine"]
Antesiology=["critical","anest","migrain","pain","neuropathic","sedation","61","antesiology"]
Colon_Rectal=["intesti","prosta","bph","colon","rectal","polyps", "7","colon and rectal"]
Dermatology=["derma","skin","debrid","8","dermatology"]
Infectious_Int=["hiv","hbv", "hcv","vira","virus", "infecti","bacteria","antibiotic","23","infectious disease"]
Cardio_Int=["cardio","vascu","acute","strok","dvt","pvd","myocard","heart","cardiovas","thromb","arterial","hypertension","21","cardiology"]
Cancer_Int=["oncolo","metastatic","chemo","malignant","carcinoid","radia","prostate","tumor","stem","lymphoma","22","cancer"]
Metabolism_Endocinology_Int=["diabete","thyroid","endocri","metabo","insulin","lipid","hypothyro","hormone","24","metabolism_endocri"]
CriticalCare_Int=["organ","emergen","critical","trauma","injur","25","critical care"]
Gastronology_Int=["gastro","liver","ulcer","intestin","stomach","abdomina","bowel","26","gastronology"]
Hematology_Int=["blood","hematol","anemia","anemic","sickle","hemophil","leukemia","lymphoma","27","hematology"]
Nephrology_Int=["renal","kidney","urinary","28","nephrology"]
Pulmonary_Int=["pulmonar","lung","asthma","cardiopulm","respira","bronchitis","asthma","pneumonia","respira","29","pulmonary"]
Rheumatology_Int=["arthritis","joint","muscle","ligament","rheumat","musculoskeletal","20","rheumatology"]
Genetics=["heredita","genetic","gene","30","genetic"]
Neurology=["neurol","nervous","neuropathic","brain","psychi","cognitive","addict","central nervous","cns","stroke","parkinson","alzheimer","40","neuro"]
Nuclear_Medicine=["nuclear","radioactive","radio","tracers","50","nuclear_medicine","50","nuclear_medicine"]
Radiology=["radiopharm","imaging","radiology","ultrasound","electromagnetic","60","radiology"]
obstetrics_gynecology=["gyneco","obstet","reprodu","female","labor","pelvic","female","infertili","vagin","70","obstetrics_gynecology"]
opthamalogy=["ophthal","glaucoma","eye","retina","macular","vision","1","opthamalogy"]
otolaryngology=["head","neck","ear","heari","sinus","reconstructive","2","Otolaryngology"]
urulogy=["urinary","urolog","bladder","incontinence","pelvic","3","urology"]
sleep_subspec=["sleep","insomnia","63","sleep_subspec"]
brook=["vaniqa","end"]

Main=[Allergy_Immun,Emergency,Antesiology,Colon_Rectal,Dermatology,Infectious_Int,Cardio_Int,Cancer_Int,Metabolism_Endocinology_Int,CriticalCare_Int,Hematology_Int,Nephrology_Int,Pulmonary_Int,Rheumatology_Int,Neurology,Genetics,Nuclear_Medicine,Radiology,obstetrics_gynecology,opthamalogy,otolaryngology,urulogy,sleep_subspec]
def studyyear (sss):
	#looks for study year
	study_year_index=sss.find('first received: <span class=')
	study_year_final=sss.find('</span',study_year_index+30)
									
									
	
	study_year=sss[study_year_index+38:study_year_final]
	
	if study_year_index==-1:
		study_year=0
	return study_year 

def therapeutic(sss):
	#looks for the therapeutic area in the study		
	thera=sss.count(therapeutic)
	thera_1=therapeutic
	thera_length=len(thera_1)
	while thera==0 and thera_length>4:
		thera_1=thera_1[-(thera_length-1):]
		thera_length=len(thera_1)
		thera=sss.count(thera_1)
	thera_0=sss.count(therapeutic)	
	thera_1=therapeutic
	thera_length=len(thera_1)
	
	while thera==0 and thera_length >4:
		thera_1=thera_1[:(thera_length-1)]
		thera_length=len(thera_1)
		thera_0=sss.count(thera_1)
	return thera_0+thera
	
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
		form_year1=line.split(",")[4].strip("\t")
		market_number=line.split(",")[7].strip('\t')
		market_number1=line.split(",")[8].strip('\t')
		market_number2=line.split(",")[9].strip('\t')
		
		drug1=product_1
		p=0
		
		
		for i in drug1:											#Cleans the product names from unwanted charetevers 
			if ord(i)>128 :
				drug1=drug1.replace(i,"").strip(i).strip()	
				
		x=len(drug1)		
		for girl in brook	:		#it looks in the memory and checks if 
			if girl==drug1 and girl!="end" :
				print ("found a match already in memory", drug1)
				break
			if girl=="end":	
				while search>0 and x>5 or syntax>0 and x>5 :	#searches for drug until the length is to short
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
								print i
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
									weight1=0
									weight2=0
									weight3=0
									weight4=0
									weight5=0
									weight6=0
									weight7=0
									weight8=0
									weight9=0
									weight10=0
									weight11=0
									weight12=0
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
									study_year=studyyear(sss);
									
									print (study_year)
									
									
									index1=index+15
									
						
			
OpenFile.close()	