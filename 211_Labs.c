#include <stdio.h>
#include <stdlib.h>
///This program will form an encrpyted message from the inputs 
int *brook(int x,int y){
	int c;
	c=x+y;
	return c;
	
}
int *lauren(int x, int y){
	
	
}


int *carly(int x){
	
}
typedef struct Node*{
	
}
int main(){
	int size=50;
	int arr0[size];
	int *arr1;
	int *arr2;
	int *arr3;
	
	arr1=(int*)malloc(sizeof(int)*size);
	printf("this is the address of arr1 :%d\n",arr1 );
	arr2=(int*)malloc(sizeof(int)*size);
	printf("this is the address of arr2 : %d\n", arr2);
	arr3=(int*)malloc(sizeof(int)*size);
	printf("this is the address of arr3 : %d\n", arr3);
	for (int i=0; i< size;++i){
	arr1[i]=i;
	arr2[i]=i*8;
	arr3[i]=arr2[i]-arr1[i] ;
	arr0[i]=i*i;
	}
	for (int j=0; j<size; ++j){
			if (arr3[j]%2==0){
				arr3[j]=0;
			}
		printf("This is the array  : %d\n", arr3[j]);
	}
	
}
