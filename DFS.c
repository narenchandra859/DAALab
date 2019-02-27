#include<stdio.h>
#include<stdlib.h>
typedef struct list *lptr;
typedef struct list {
	int nodeNo;
	lptr link;
}list;
void printUList(lptr x);
void addEdge(int a, int b, lptr *adjList) {
	lptr t, t1, f=adjList[b-1], f1=adjList[a-1];
	while(f->link!=NULL)
		f=f->link;
	while(f1->link!=NULL)
		f1=f1->link;
	t=(lptr)malloc(sizeof(list));
	t1=(lptr)malloc(sizeof(list));
	t->nodeNo=a;
	t1->nodeNo=b;
	t->link=NULL;
	t1->link=NULL;
	f->link=t;
	f1->link=t1;
	//printUList(adjList[a-1]);
	//printUList(adjList[b-1]);
}
void printUList(lptr a) {
	printf("\n");
	while(a!=NULL) {
		printf("\t%d",a->nodeNo);
		a=a->link;
	}
}
void printList(lptr *adjList, int n) {
	int i;
	lptr t;
	for(i=0;i<n;i++) {
		t=adjList[i];
		printf("\nList %d ",i+1);
		while(t!=NULL) { 
			printf(" %d",t->nodeNo);
			t=t->link;
		}
	}
	printf("\n");
}
int main() {
	int n, u, v, i;
	printf("\nEnter the number of nodes in graph : ");
	scanf("%d",&n);
	lptr adjList[n];
	for(i=0;i<n;i++) {
		adjList[i]=(lptr)malloc(sizeof(list));
		adjList[i]->nodeNo=i+1;
		adjList[i]->link=NULL;
	}
	printf("\nEnter edges (u,v) [-1 to stop] - : ");
	while(1) {
		scanf("%d",&u);
		if(u==-1) break;
		scanf("%d",&v);
		addEdge(u,v,adjList);
	}
	printList(adjList, n);
	return 0;
}		
