/////FIRST LAB FOR QUICKSORT AND SELECTION SORT//////

//Selection sort///
for (i = 0; i < numbersSize; ++i) {
      
   // Find index of smallest remaining element
   indexSmallest = i;
   for (j = i + 1; j < numbersSize; ++j) {
      
      if (numbers[j] < numbers[indexSmallest]) {
         indexSmallest = j;
      }
   }
      
   // Swap numbers[i] and numbers[indexSmallest]
   temp = numbers[i];
   numbers[i] = numbers[indexSmallest];
   numbers[indexSmallest] = temp;
}


int Partition(int array[],int i, int k)
	int high=0;
	int low=0;
	int midpoint=(i+(k-i))/2;
	pivot=array[midpoint];
	int temp;
	bool done=false;
	while (!done){
		while(pivot>array[low]{			//Stops when
			++low;
		}
		
		
		while(pivot<array[high]{
			++high;
		}
		
		if (low>=high){
			done=true;
		}
		else{
			temp=array[low];
			array[low]=array[high];
			array[high]=temp;
		}
	return high	;
	}
void quicksort(int A[],int i, int k){   //
	
	//base case
	if (i>k){
		return;
	}
	
	int h;
	h=Partition(int A[],i,k);
	quicksort(A,i,h);
	quicksort(A,h+1,k);
	return 0;
	
	
}
/////Begins the CTA PROJECT/////


typedef struct Ridership{
	int station_ID;
	char date[16];
	char DayType;
	int Num_Rid;
	
	 struct Ridership *Next ;
}Ridership;


Ridership *InputRidership(char *filename, int *numRiderships){
	FILE *infile ;
	char line[100];
	int N=0;
	int linesize=sizeof(line);
	char *token;
	

	infile=fopen(filename,"r")
	if (infile==NULL){
		printf("Error unable to open '%s'", filename);
		return 0;
		
		}
	fgets(line, linesize,infile); //removes the headers than treats the next row to be the fields in the block of memory defined by the data strucuture RIdership
	Ridership*head=NULL;
	Ridership*tail=NULL;
	fgets(line, linesize,infile);
	
	while (!feof(infile))	{		//probably means until it reaches the end of the file.
	Ridership*node=(Ridership*)malloc(sizeof(Ridership)) //The pointer 'Ridership' points to the block (by its address)
	if (head==NULL)
		node=head;
		
	else     //makes the pointer point to the next node 
	tail->Next=node;
		
	
	tail=node
	tail->Next=NULL
	
	token=strok(line,",");
	assert(token!=NULL);
	strcopy(node->Name,token);
	
	token=strok(line,",");
	assert(token!=NULL);
	token=strok(NULL,",");
	strcpy(node->date, token);
	
	


	  fgets(line, linesize, infile); //gets line and then repeats. 
	  
	}
		fclose(infile);
	
 
	
*numRiderships = N;
	return head;
}




int main(void) {
	
Station   *stations;
  int        numStations;
  Ridership *ridership;
  int        numRiderships;
 
 ridership = InputRidership("ridership.csv", &numRiderships);
 
#ifdef DEBUG
  //
  // print the first and last 5 riderships:
  //
  printf(">> Number of Ridership data points: %d\n", numRiderships);
	
	
	
	
}



