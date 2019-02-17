#include<stdio.h>
int meneng(int a[][2], int t) {
	//printf("\nIN MENENG \n");
	int i, f=0;
	for(i=1;i<=t;i++) {
		if(a[i][0]!=0)	continue;
		else {	f=1;
			break;	}}
	if(f) 	return 1;
	else    return 0;
} 
int chooseman(int a[][2], int t) {
	int i;
	//printf("\nIN CHOOSEMAN \n");
	for(i=1;i<=t;i++) {
		if(a[i][0]==0) 
		return i;
	}
}
void propose(int t, int s[][2], int m[t][t], int f[t][t], int n) {
	int i=1, j, k, b=0, v1, v2;
	//printf("\nIN PROPOSE \n");
	for(i=1;i<=t;i++) {
		j=m[n-1][i-1];        // j is mans pref list holder - the woman, n is the man currently being used for proposal
		if(s[j][1]==0) {
		//printf("\nIN PROPOSE IF \n");
			s[j][1]=n;
			s[n][0]=j;
			break;
		}
		else {		
		printf("\nIN PROPOSE  ELSE \n");	
			k=s[j][1];    // k is which man  s[j][1] -- the woman w he is currently proposing to is engaged to.
			for(b=0;b<t;b++) {	// in j's pref list(woman) is k better or n better? (m vs m')
	 		//printf("\nin for of else %d = , %d = , %d =, %d, %d",f[j-1][b],k,n,v2,v1);
				if(f[j-1][b]==n) 
					v1=b;
				else if(f[j-1][b]==k)
					v2=b;
				else
					continue;
			}
			//printf("\nout of for of else ");
			if(v2<v1)  
				continue;            // she prefers k itself, m iterates. 
			else {			// breakup k and w, and new engagement of w and n
				s[k][0]=0;    // k becomes unengaged
				s[n][0]=j;
				s[j][1]=n;
				break;
			}	
		}
	}
}
int main() {		
	/*int m[5][5] = { {2,1,4,5,3},           // MALE pref list
			{4,2,1,3,5},
			{2,5,3,4,1},
			{1,4,3,2,5},
			{2,4,1,5,3}};
	int f[5][5] = { {5,1,2,4,3},           // FEMALE pref list
			{3,2,4,1,5},
			{2,3,4,5,1},
			{1,5,4,3,2},
			{4,2,5,3,1}}; 
	int s[6][1] = {0};           	// array to hold the pairs of engaged people
	*/
	printf("\nEnter the number of men and women - \"n\" : ");
	int n;
	scanf("%d",&n);
	int a, i, j, b=1;
	int m[n][n];
	int f[n][n];
	int s[n+1][2];
	int t = n;
	for(i=1;i<=n;i++) {
		s[i][1]=0;
		s[i][0]=0;
	}
	printf("\nEnter MENS pref list, in order of 1 - %d (lower is better) : ",n);
	for(i=0;i<n;i++) {
		printf("\nEnter for man number %d : ",i+1);
		for(j=0;j<n;j++) {
			scanf("%d",&m[i][j]);
		}
	}
	printf("\nEnter WOMENS pref list, in order of 1 - %d (lower is better) : ",n);
        for(i=0;i<n;i++) {
                printf("\nEnter for woman number %d : ",i+1);
                for(j=0;j<n;j++) {
                        scanf("%d",&f[i][j]);
                }
	}
	while(meneng(s,t)) {
		a=chooseman(s,t);
		propose(t, s, m, f, a);
	}
	printf("\n MAN \t WOMAN \n");
	printf("\n");
	for(i=1;i<=t;i++) {
		printf("\t%d\t%d",b++,s[i][0]);
		printf("\n");
	}
	return 0;
}
