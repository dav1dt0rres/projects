#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Student
{
  char Netid[16];
  int  Midterm;
  int  Final;
} Student;

// inputs and discards the remainder of the current line for the 
// given input stream, including the EOL character(s):
void skipRestOfInput(FILE *stream)
{
  char restOfLine[256];
  int rolLength = sizeof(restOfLine) / sizeof(restOfLine[0]);

  fgets(restOfLine, rolLength, stream);
}

char netid[16];
int  mid, fnl;
int i=0;
float division;
int main(int argc, char *argv[])
{
  Student students[100];
  

scanf("%s %d %d", netid, &mid, &fnl);

skipRestOfInput(stdin);
if (netid[0]=='#'){
	
   printf("Midterm : %s\n", "N/A");
   printf("Final : %s\n", "N/A");
   return 0 ;
}
 while (netid[0] != '#'){
	
	strcpy(students[i].Netid, netid);
	students[i].Midterm=mid;
	students[i].Final=fnl;
	
	++i;
	++division;
	
	scanf("%s %d %d", netid, &mid, &fnl);
	skipRestOfInput(stdin);
 }
int p;
float average;
double class_average_M;
double class_average_F;
double class_sum_M;
double class_sum_F;
float sum;
for (p=i-1;p>=0;--p){
	sum=students[p].Midterm+students[p].Final;
	average=sum/2;

	printf("%s: %d,%d,%f\n",students[p].Netid, students[p].Midterm, students[p].Final,average);
	class_sum_M=students[p].Midterm+class_sum_M;
	class_sum_F=students[p].Final+class_sum_F;

}
class_average_M=(class_sum_M)/(division);
class_average_F=(class_sum_F)/(division);

printf("Midterm: %f\n",class_average_M);
printf("Final: %f\n",class_average_F);
return 0 ;
 
}
