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