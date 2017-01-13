/* main.c */

/*
 * Sorting students by Major, then Netid
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct STUDENT
{
char  Netid[16];
int   Uin;
char  Major[16];
} STUDENT;


void SortStudentsByMajorThenNetid(STUDENT students[], int numStudents)
{
int x=0;
int a;   
int temp;      //declares the temp
char temp_netid[16];
char temp_major[16];
 for ( x=0;x<numStudents;++x){
 
	for (int j=x+1; j<numStudents;++j){
	
		if (strcmp(students[x].Major, students[j].Major) > 0) {
         
			temp=students[x].Uin;   //gives the temp a value
			strcpy(temp_netid,students[x].Netid);
			strcpy(temp_major,students[x].Major);
		
			strcpy(students[x].Netid , students[j].Netid); //here is the real switching occuring
		    strcpy(students[x].Major , students[j].Major);
		    students[x].Uin=students[j].Uin;
		
		    
		
		    students[j].Uin=temp;               //then the entry that HELD the smaller is now replaced with the bigger one
		    strcpy(students[j].Netid,temp_netid);
		    strcpy(students[j].Major,temp_major);
		}
        if (strcmp(students[x].Major, students[j].Major) == 0){	//if the majors are the same then arrange with Netid
			if (strcmp(students[x].Netid,students[j].Netid) > 0){
				temp=students[x].Uin;   //gives the temp a value
			strcpy(temp_netid,students[x].Netid);
		   strcpy(temp_major,students[x].Major);
		
		   strcpy(students[x].Netid , students[j].Netid); //here is the real switching occuring
		   strcpy(students[x].Major , students[j].Major);
		   students[x].Uin=students[j].Uin;
		
		  
		
		   students[j].Uin=temp;               //then the entry that HELD the smaller is now replaced with the bigger one
		   strcpy(students[j].Netid,temp_netid);
		   strcpy(students[j].Major,temp_major);
			}
        
           
            
         }
	}
   
      
      
   }

 }

// inputs and discards the remainder of the current line for the 
// given input stream, including the EOL character(s):
void skipRestOfInput(FILE *stream)
{
  char restOfLine[256];
  int rolLength = sizeof(restOfLine) / sizeof(restOfLine[0]);

  fgets(restOfLine, rolLength, stream);
}


STUDENT *InputStudents(FILE *input, int *numStudentsPtr)
{
  char  netid[16];
  int   uin;
  char  major[16];
  int   N = 0;

  // hack: we only allow at most 16 students:
  STUDENT *students = (STUDENT *)malloc(sizeof(STUDENT) * 16);

  fscanf(input, "%s %d %s", netid, &uin, major);
  skipRestOfInput(input);
  
  while (strcmp(netid, "#") != 0)  // until we see EOF marker
  {
    strcpy(students[N].Netid, netid);
    students[N].Uin = uin;
    strcpy(students[N].Major, major);

    N++;

    // next:
    fscanf(input, "%s %d %s", netid, &uin, major);
    skipRestOfInput(input);
  }

  // done:
  *numStudentsPtr = N;

  return students;
}

int main()
{
  STUDENT *students;
  int      N;

  students = InputStudents(stdin, &N);
  
  SortStudentsByMajorThenNetid(students, N);

  for (int i = 0; i < N; ++i)
    printf("%s: %s (%d)\n",
      students[i].Major,
      students[i].Netid,
      students[i].Uin);

  return 0;
}
