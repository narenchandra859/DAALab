#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void insertionsort(int* a, int n) {
	int i, j, hold, temp;
	for(i=1;i<n;i++) {	
		hold=a[i];
		j=i-1;
		while(hold<a[j]&&j>=0)
			a[j+1]=a[j--];
		a[j+1]=hold;
	}
}
int main() {
	int n, i;
	printf("\nEnter the number of elements : ");
	scanf("%d",&n);
	printf("\nEnter the elements : ");
	int *a;
	a=(int *)malloc(sizeof(int)*n);
	for(i=0;i<n;i++) 
		scanf("%d",(a+i));
	clock_t m;
	m=clock();
	insertionsort((int*)a,n);
	m=clock()-m;
	double t_time=((double)m)/CLOCKS_PER_SEC;
	printf("\nSorted array : ");
	for(i=0;i<n;i++) 
		printf("\t%d",a[i]);
	printf("\nTime taken = %fs\n",t_time);
	return 0;
}
