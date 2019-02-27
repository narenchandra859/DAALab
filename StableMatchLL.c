#include<stdio.h>
#include<stdlib.h>
typedef struct list *listptr;
typedef struct list {
	int index;
	int manMi;
	int womMi;
	listptr link;
}list;
int MenEng(listptr front) {
	listptr t=front;
	printf("\nIn MenEng");
	while(t!=NULL) {
		if(t->manMi!=0) {
			t=t->link;
			continue;
		}
		else
			return 1;
	}
	return 0;
}
int getIndex(listptr front) {
	printf("\nIn getIndex");
	listptr t=front;
	while(t!=NULL) {
		if(t->manMi==0) {
			printf("\nIn getIndex, current index check = %d",t->index);
			return t->index;
		}
		t=t->link;
	}
}
void propose(int n, listptr front, int getIndexVal, int m[n][n], int f[n][n]) {
	int index=getIndexVal;
	printf("\nIn propose");
	listptr t=front;
	while(t->index!=index){
		printf("\nParsing t, index = %d",t->index);
		t=t->link;
	}
	int i, ti=index-1, j, b, v1, v2;
	for(i=0;i<n;i++) {
		j=m[ti][i];
		listptr w=front;
		while(w->index!=j)
			w=w->link;
		printf("\nIn propose, Man %d proposing to Woman %d",index,j);
		if(w->womMi==0) {
			printf("\nNo breakup case");
			w->womMi=index;
			t->manMi=j;
			return;
		}
		else {
			printf("\nChecking m vs m', womMi -> %d",w->womMi);
			int ti1=w->womMi;
			//printf("\nDeclared ti1 = %d",ti1);
			printf("\n M = %d, M' = %d",index,ti1);
			for(b=0;b<n;b++) {
				if(f[j-1][b]==ti1)
					v1=b;
				else if(f[j-1][b]==index)
					v2=b;
				else
					continue;
			}
			if(v2>v1)
				continue;
			else { 	
				listptr breakup=front;			
				printf("\nBreaking up : ");
				w->womMi=index;
				t->manMi=j;
				while(breakup->index!=ti1)
					breakup=breakup->link;
				breakup->manMi=0;
				return;
			}
		}
	}
}
void printList(listptr t) {
	while(t!=NULL) {
		printf("\nIndex - %d ManMi - %d WomMi - %d",t->index,t->manMi,t->womMi);
		t=t->link;
	}
}
int main() {
	int n;
	printf("\nEnter the number of men and women - ");
	scanf("%d",&n);
	int m[n][n], f[n][n], t=n, a, i, j;
	listptr front, final;
	front=(listptr)malloc(sizeof(list));
	front->index=t;
	front->manMi=0;
	front->womMi=0;
	front->link=0;
	for(i=0;i<n-1;i++) {
		t--;
		listptr temp;
		temp=(listptr)malloc(sizeof(list));
		temp->index=t;
		temp->manMi=0;
		temp->womMi=0;
		temp->link=front;
		front=temp;
	}
	/*listptr te=front;
	while(te!=NULL) {
		printf("\n index = %d",te->index);
		te=te->link;
	}*/
	final=front;
	printf("\nEnter mans pref list, in order of 1 - %d  : ",n);
        for(i=0;i<n;i++) {
                printf("\nEnter for man number %d : ",i+1);
                for(j=0;j<n;j++) {
                        scanf("%d",&m[i][j]);
                }
        }
        printf("\nEnter WOMENS pref list, in order of 1 - %d : ",n);
        for(i=0;i<n;i++) {
                printf("\nEnter for woman number %d : ",i+1);
                for(j=0;j<n;j++) {
                        scanf("%d",&f[i][j]);
                }
        }
	while(MenEng(front)) {
		a=getIndex(front);
		propose(n,front,a,m,f);
		printList(front);
	}
	printf("\n Final pairs : \n\tMan\tWoman\n");
	for(i=0;i<n;i++) {
		printf("\t%d\t%d\n",final->index,final->manMi);
		final=final->link;
	}
	return 0;
}
