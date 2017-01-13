
/* main.c */
 
//
// Program to experiment with sorting.
//
// Prof. Joe Hummel
// U. of Illinois, Chicago
// Spring 2017
// Lab exercise, week 01
//
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
 
// #################################################################
// 
// SelectionSort:
//
void SelectionSort(int A[], int N)
{
  printf("** Selection Sort...\n");
 
  int smallest;
 
  for (int i = 0; i < N-1; ++i)
  {
    smallest = i;  // assume i is index of smallest element:
 
    for (int j = i+1; j < N; ++j)
    {
      if (A[j] < A[smallest])  // found a smaller one!
        smallest = j;  // now this is index of smallest element:
    }
 
    if (smallest != i)  // swap smallest into place:
    {
      int T = A[i];
      A[i] = A[smallest];
      A[smallest] = T;
    }
  }
}
 
 
// #################################################################
// 
// QuickSort:
//
 
//
// partitions i..k elements into 2 sets, those <= pivot and
// those >= pivot.  Returns index j where left partition ends,
// so upon return the array is updated so that left partition 
// are elements i..j and right partition are elements j+1..k.
//
int partition(int A[], int i, int k)
{ 
  // pick middle element as pivot:
  int midpoint = i + (k-i)/2;
  int pivot = A[midpoint];
 
  // partition into 2 sets, those <= pivot and those > pivot:
  int low = i;
  int high = k;
 
  while (1)
  {
    // find an element on the left that's >= pivot:
    while (A[low] < pivot)
      ++low;
     
    // find an element on the right that's <= pivot:
    while (A[high] > pivot)
      --high;
 
    // do we have 2 elements to swap?
    if (low >= high)  // no more elements to swap:
      break;
     
    // swap low and high elements to other partitions:
    int T = A[low];
    A[low] = A[high];
    A[high] = T;
 
    // with these swapped, move on and look for more:
    ++low; 
    --high;
  }//while
 
  // done, return end of left partition:
  return high;
}
 
//
// sorts the range of elements A[i]..A[k], where i <= k.  The 
// quicksort algorithm partitions the data into roughly two
// equal halves, and then sorts the 2 halves recursively.
//
void quicksort(int A[], int i, int k)
{int h=0;
	
	//base case
	if (i>=k){
		return;
	}
	
	
	h=partition(A,i,k);
	quicksort(A,i,h);
	quicksort(A,h+1,k);
	return;
	
  // base case: if 0 or 1 elements, partition i..k already sorted, nothing to do
  // HINT: compare i and k...
  //
  // if (...)
  // {
  //    return;
  // }
  //
  // else
  // {
  //   recursive case: 2 or more elements in i..k partition, need to sort
  //
  //   step 1: partition the array
  //   HINT: call partition function, and capture return value
  //
  //   step 2: recursively sort left and right partitions!
  //   HINT:  call quicksort twice
  //
  // }
}
 
void QuickSort(int A[], int N)
{
  printf("** QuickSort...\n");
 
  quicksort(A, 0, N-1);
}
 
 
// #################################################################
// 
// main:
//
int main(int argc, char *argv[])
{
  int  N;
  int  *A;
 
  if (argc > 1) // we have at least one cmd-line arg:
  {
    // assume a value N:
    N = atoi(argv[1]);
  }
  else
  {
    N = 4000000;  // default value:
  }
 
  printf("** Filling array with %d random values...\n", N);
 
  A = (int *) malloc(N * sizeof(int));
 
  for (int i = 0; i < N; ++i)
    A[i] = rand() % (2*N);  // 0..2*N-1
 
  printf("** Unsorted values:\n");
  printf("   %d,%d,%d,...,%d,%d,%d\n\n",
    A[0],A[1],A[2],A[N-3],A[N-2],A[N-1]);
 
  clock_t startTime = clock();
 
  //SelectionSort(A, N);
   quicksort(A, 0, N-1);
 
  clock_t stopTime = clock();
  double time = (((double) stopTime) - ((double) startTime)) / CLOCKS_PER_SEC;
  printf("** Sort time: %f secs\n\n", time);
 
  printf("** Sorted values:\n");
  printf("   %d,%d,%d,...,%d,%d,%d\n\n",
    A[0],A[1],A[2],A[N-3],A[N-2],A[N-1]);
 
  // done:
  return 0;
}