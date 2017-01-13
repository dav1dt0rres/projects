a= 6
import string
import re
OpenFile = open(r"C:\Users\David\Desktop\ftp.txt","r")
# read in the lines in the file
lines = OpenFile.readlines()
for line in lines:
	id2 = line.strip().split()[0].lower() # extract first word

	form_type = line.strip().split()[1].lower() # extract second word
	
	form_year = line.strip().split()[2].lower() # extract third word
	sitename = line.strip().split()[3].lower()
	try:
		f = urllib.urlopen(sitename)
		s = f.read()
        # Read from the object, storing the page's contents in 's'.
		lower_s = string.lower(s)
        # Save the file locally
		localfile = "./" + id2+"_"+form_year+"_"+form_type
		print localfile
		Outfile = open(localfile, "w") 
		Outfile.write(lower_s)
		Outfile.close()
        
    
	except IOError:
		print a 