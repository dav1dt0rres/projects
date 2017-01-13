/*main.c*/

// ignore stdlib warnings if working in Visual Studio:
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "memdebug.h"

typedef struct Student
{
  char  *Netid;
  char  *Email;
  int    Midterm;
  int    Final;
} Student;

// inputs and discards the remainder of the current line for the 
// given input stream, including the EOL character(s):
void skipRestOfInput(FILE *stream)
{
  char restOfLine[256];
  int rolLength = sizeof(restOfLine) / sizeof(restOfLine[0]);

  fgets(restOfLine, rolLength, stream);
}

int main(int argc, char *argv[])
{
char netid[16];
char email[64];
int  mid, fnl;
int i;
scanf("%s %s %d %d", netid, email, &mid, &fnl);
skipRestOfInput(stdin);

Student students[100];

if (netid[0]=='#'){
	printf("Min: %s\n", "N/A");
   printf("Max: %s\n", "N/A");

}

while(netid[0]!='#'){
students[i].Netid=(char*)malloc((strlen(netid)+1)*sizeof(char));
strcpy(students[i].Netid,netid);
students[i].Email=(char*)malloc((strlen(email)+1)*sizeof(char));
strcpy(students[i].Email,email);
students[i].Midterm=mid;
students[i].Final=fnl;

scanf("%s %s %d %d", netid, email, &mid, &fnl);
skipRestOfInput(stdin);
++i;
}
int p;
float average;
float sum;
float max=0.0;
float min=0.0;
for(p=i-1;p>=0;--p){
   sum=students[p].Midterm+students[p].Final;
   average=sum/2;
   
   if (average>max){
      max=average;
   }
   if (average<min){
      min=average;
   }
   printf("%s (%s): %d,%d, %f\n",students[p].Netid,students[p].Email,students[p].Midterm, students[p].Final,average);
}
printf("Min: %f\n", min);
printf("Max: %f\n", max);

memdebug_init(0);  // 1 => interactive; switch to 0 inside zyLabs

  // allocation stats:
printf("Allocations: %lu\n", memdebug_num_objects());

 return 0;
}