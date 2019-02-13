#include<stdio.h>
int meneng(int a[][2]) {
	printf("\nIN MENENG \n");
	int i, f=0;
	for(i=1;i<=5;i++) {
		if(a[i][0]!=0)	continue;
		else {	f=1;
			break;	}}
	if(f) 	return 1;
	else    return 0;
} 
int chooseman(int a[][2]) {
	int i;
	printf("\nIN CHOOSEMAN \n");
	for(i=1;i<=5;i++) {
		if(a[i][0]==0) 
		return i;
	}
}
void propose(int n, int s[][2], int m[][5], int f[][5]) {
	int i=1, j, k, b=0, v1, v2;
	printf("\nIN PROPOSE \n");
	for(i=1;i<=5;i++) {
		j=m[n-1][i-1];        // j is mans pref list holder - the woman, n is the man currently being used for proposal
		if(s[j][1]==0) {
		printf("\nIN PROPOSE IF \n");
			s[j][1]=n;
			s[n][0]=j;
			break;
		}
		else {		
		printf("\nIN PROPOSE  ELSE \n");	
			k=s[j][1];    // k is which man  s[j][1] -- the woman w he is currently proposing to is engaged to.
			for(b=0;b<5;b++) {	// in j's pref list(woman) is k better or n better? (m vs m')
	 			if(f[j-1][b]==n) 
					v1=b;
				else if(f[j-1][b]==k)
					v2=b;
				else
					continue;
			}
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
	int m[5][5] = { {2,1,4,5,3},           // MALE pref list
			{4,2,1,3,5},
			{2,5,3,4,1},
			{1,4,3,2,5},
			{2,4,1,5,3}};
	int f[5][5] = { {5,1,2,4,3},           // FEMALE pref list
			{3,2,4,1,5},
			{2,3,4,5,1},
			{1,5,4,3,2},
			{4,2,5,3,1}}; 
	int s[6][2] = {0};                    // array to hold the pairs of engaged people
	int a;
	while(meneng(s)) {
		a=chooseman(s);
		propose(a, s, m, f);
	}
	int i, j, b=1;
	printf("\n MAN \t WOMAN \n");
	printf("\n");
	for(i=1;i<=5;i++) {
		printf("\t%d\t%d",b++,s[i][0]);
		printf("\n");
	}
	return 0;
}
