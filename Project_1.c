
/*main.c*/
 
//
// Netflix movie analysis: top-10 by rating and # of reviews.
//
// <<Name>>
// Windows with Visual Studio
// U. of Illinois, Chicago
// CS251, Spring 2017
// Project #01
//
 
// ignore stdlib warnings if working in Visual Studio:
#define _CRT_SECURE_NO_WARNINGS
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
 
 
//
// getFileName: inputs a filename from the keyboard, make sure the file can be
// opened, and returns the filename if so.  If the file cannot be opened, an
// error message is output and the program is exited.
//
typedef struct Movies {
char Movie_title[255];
int Movie_id;
double Movie_avg;

	
}movies_struct;

char *getFileName()
{
  char filename[512];
  int  fnsize = sizeof(filename) / sizeof(filename[0]);
 
  // input filename from the keyboard:
  fgets(filename, fnsize, stdin);
  filename[strcspn(filename, "\r\n")] = '\0';  // strip EOL char(s):
 
  // make sure filename exists and can be opened:
  FILE *infile = fopen(filename, "r");
  if (infile == NULL)
  {
    printf("**Error: unable to open '%s'\n\n", filename);
    exit(-1);
  }
 
  fclose(infile);
 
  // duplicate and return filename:
  char *s = (char *)malloc((strlen(filename) + 1) * sizeof(char));
  strcpy(s, filename);
 
  return s;
}
 
movies_struct *Array_Intialize(char* s,char*t) {
	FILE* infile;
	FILE *infile_1;
	char line[100]; 
	char line_1[100];
	int linesize=sizeof(line)/sizeof(line[0]) ;
	int N;//This is the number of movies;
	int R;//this is the number of Reviews
	int i;
	int x;
	int matches=0;
	double Sum=0;
	char *token;
	char *token_1;
	double Average;
	infile=fopen(s,"r");
	infile_1=fopen(t,"r");
	
	fgets(line, linesize,infile);
	line[strcspn(line, "\r\n")] = '\0'	;
	token=strtok(line,",");
	N=atoi(token);
	printf("this is number of movies: %d\n",N);
	
	fgets(line_1, linesize,infile_1);
	line_1[strcspn(line_1, "\r\n")] = '\0'	;
	token=strtok(line_1,",");					
	R=atoi(token);
	printf("this is number of Reviews: %d\n",R);
	
	movies_struct *array=(movies_struct*)malloc(sizeof(movies_struct)*N);

	i=1;
	fgets(line, linesize,infile);
	line[strcspn(line, "\r\n")] = '\0'	;
	while(i<N){	
		token=strtok(line,",");
		array[i].Movie_id=atoi(token);
		printf("%d",array[i].Movie_id );
		token=strtok(NULL,",");
		strcpy(array[i].Movie_title, token);
		printf("%s\n",array[i].Movie_title );
		
		//Here it begins to look for all the reviews that match the movie_id;
		infile_1=fopen(t,"r");
		fgets(line_1, linesize,infile_1);
		
		x=1;
		fgets(line_1, linesize,infile_1);
		line_1[strcspn(line_1, "\r\n")] = '\0'	;
		while(x<=R){
			token_1=strtok(line_1,",");
			if (atoi(token_1)==array[i].Movie_id){
				token_1=strtok(NULL,",");
				token_1=strtok(NULL,",");
				printf("%d\n",atoi(token_1));
				Sum=Sum+atoi(token_1);
			
				++matches;
			}
			fgets(line_1, linesize,infile_1);
			line_1[strcspn(line_1, "\r\n")] = '\0';
			++x;
			
		}//Here it finishes reading the review file
		fclose(infile_1);
		printf("Sum: %d\n",Sum);
		array[i].Movie_avg=Sum/matches;
		printf("Average: %f\n",array[i].Movie_avg);
		Sum=0;
		
		matches=0;
		fgets(line, linesize,infile);
		line[strcspn(line, "\r\n")] = '\0';
		++i;
		
} 
fclose(infile);

return array;

}



void sortNumReviews(){
	
}

void sortrating(char *s){

}



int main()
{
	movies_struct *Y;
// get filenames from the user/stdin:
  char *MoviesFileName = getFileName();
	char *ReviewsFileName = getFileName();
	
	Y=Array_Intialize(MoviesFileName,ReviewsFileName);
	
	
}