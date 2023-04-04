#include <stdio.h>
int main(void) {
	int t,r1,r2,r3,r4;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d %d %d %d",&r1,&r2,&r3,&r4);
	    r3=r3/r1;
	    r4=r4/r2;
	    printf("%d\n",r3+r4);
	}
	
	return 0;
}