#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
void arrayCopy (int fromArray[], int toArray[], int size) {
	
	int *dt;
	
	for (int x=0;x<size;++x){
		
		dt=&fromArray[x];
		
		toArray[x]= *dt;
		
		printf("this is what the copied on array has now %d,%d\n",*dt,toArray[x]);
	}	
		
	
}
void sort (int arr[], int size) { //Sorts in ascending order
	
	
	for (int x=0;x<size;++x){
		int smallest=arr[x];
		for (int j=x+1; j<size;++j){
			if (arr[j]<smallest){
				int temp;
				temp=arr[x];
				arr[x]=arr[j];
				smallest=arr[j];
				arr[j]=temp;
			}
		
		
		}
		
	}
	
}




void linSearch(int arr[],int size, int target, int *pi, int *o){
	
	for (int x=0;x<size-1;++x){
		if (arr[x]==target){
		
			*pi=x; //The number of comparisions is one more than the position of the array where it was found
			*o=x+1; //ANOTHER INTEPRETATAION ABOUT POINTERS HERE: Now the value of the pointer variable is now the same value as x. 
					//Since 'x' is a normal variable when you equate it, its the actual value. But since *pi is a pointer, you need the * to signify
			}		//this is the actual value the pointer variable has. pi would return the address of the variable. 
	
	}
		
}

	

int BinarySearch(int numbers[], int numbersSize, int key,int *comparisons) {  //Splits it in half than sees where the number is in relation to it, remember the array shoud
																// have been ordered already. 
   int mid = 0;
   int low = 0;
   int high = 0;
   int x=0;
   
   
   high = numbersSize - 1;
   
   while (high >= low) {
	  x++;
      mid = (high + low) / 2;
      if (numbers[mid] < key) {
         low = mid + 1;
		 
		
		
      }
      else if (numbers[mid] > key) {
         high = mid - 1;
		
		
      }
      else {
		 *comparisons=x;
		 
         return mid;
      }
	
	}
   
   return -1; // not found
}


//////////Here begins PROAMMING 2 PROJECT (fucntions and structures)////////////

 //////prgoraming project 2 and 3 together about stacks//////
 
 typedef struct Vertex{
	char *label;
	bool visited; 
 }vertex;
 
 void Matrixsetup(const char *file){
	FILE *infile;
	int N=0;
	int rows=0;
	int row=0;
	int column=0;
	int columns=0;
	char line[8];
	char *token;
	char *start;
	char *end;
	char *block;
	char *open;
	block="*";
	open=".";
	
	start="s";
	end="e";
	infile=fopen(file,"r");

	
	fgets(line,8,infile);	
	printf("these are the dimensions: %s\n",line);
	
	token=strtok(line," ");
	row=atoi(token);
	token=strtok(NULL," ");
	column=atoi(token);
	
	vertex* matrix[row][column];	//this is the newly created matrix with these many rows and these many columns but able to hold data structures of form 'vertex'
	for (int x=1;x<=row;++x){ // here it fills out the rest with "open" spaces
		for (int y=1;y<=column;++y){
			vertex *node=(vertex*)malloc(sizeof(vertex));
			printf("address of the node:%d\n", N);
			matrix[x][y]=node;
			matrix[x][y]->label=block;
			matrix[x][y]->visited=false;
			++N;
			
		}
		
	}
	
	
	//start
	fgets(line,8,infile); 
	token=strtok(line," ");
	rows=atoi(token);
	token=strtok(NULL,"");
	columns=atoi(token);
	printf("this is column: %d\n", columns);
	matrix[rows][columns]->label=start;
	matrix[rows][columns]->visited=true;
	
	
	printf("this should be s : %s\n",matrix[rows][columns]->label);


	///ending 
	fgets(line,8,infile);
	token=strtok(line," ");
	rows=atoi(token);
	token=strtok(NULL,"");
	columns=atoi(token);
	
	matrix[rows][columns]->label=end;
	matrix[rows][columns]->visited=false; 
	printf("this should be ending : %s\n", matrix[rows][columns]->label);
	
	
	fgets(line,8,infile); 
	while (!feof(infile)){	//here you need to make sure some of the errors the project specifies need to be taken care of...because you are now putting in
		token=strtok(line," ");//blockers but maybe the coordinate read from the file is outside of the range.
		rows=atoi(token);
		token=strtok(NULL,"");
		columns=atoi(token);
		
		matrix[rows][columns]->label=block;
		
		matrix[rows][columns]->visited=false; 
	
		fgets(line,8,infile); 
		
	}

		
	fclose(infile);
		
	}
	

	
	

 
 typedef struct node{
	 int data;
	 struct node *next; 
 }Node;
 
typedef struct linkedlist{
	Node *head;
	Node *tail;
	
}LinkedList;

void initializeList(LinkedList *list) {
    list->head = NULL;
	
}

void push(LinkedList *list, int data) {
	
    Node *node = (Node*) malloc(sizeof(Node));
    node->data = data;
    if (list->head == NULL) { //then this is first one being put on in the stack. (The stack is empty)
        list->tail=node;
		node->next=NULL;   
    } 
	else {
        node->next = list->head; //Means there is already a block, and the address shuold from now on point to the head (which is itself for ..right now) 
    }
    list->head = node; //list->head now points to the the newly created node as the new block head. 
}


void pop(LinkedList *Stack){
	Node *node=Stack->head;
	if (node==NULL){
		printf("stack is empty");///this will matter a lot for later on. for the purposes of the maze
	}
	if(node==Stack->tail){ //the stack had only one block so this what it will do
		Stack->tail=NULL;
		Stack->head=NULL;
		free(node);	
	}
	else{
		Stack->head=Stack->head->next;
	
		free(node);
		
	}	

	
}



void main(int argc, char **argv){

const char *filename;

char str1[40];
printf ("Enter in the filename \n");
scanf("%s",str1);

Matrixsetup(str1);



//*printf ("Enter in a list of numbers followed by the terminal value of -999\n");

//*fgets(line,3,stdin);
//*printf("this is line: %s\n",line);
//*stack_1=initialize_stack(3);
//*Push(stack_1,line);
//*printf("this is the position of the top of the stack : %d\n",stack_1->top_of_stack);

	//*int pi;
	//*int o;
	//*int comparisons;
	//*int position;
	//*int vector[]={2,15,33,66,500,504,607,620,699,700,765};
	
	//*linSearch(vector,5,66,&pi,&o);
	//*position= BinarySearch(vector,11,15,&comparisons);
	//*sort(vector,5);
	
	//*printf("this is teh ordered on array  %d\n",vector[4]);
	//*printf("this is position in the array for Linearsearch %d\n",pi);
	//*printf("this is comparisons for Linearsearch %d\n",o);
	//*printf("this is	position in the array  for Binarysearch  %d\n", position);	
	//*printf("this is	comparisons in the array  for Binarysearch  %d\n", comparisons);	//comparisons here is the pointer variable. 
	
}