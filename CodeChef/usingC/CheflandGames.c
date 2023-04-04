#include <stdio.h>

int main(void) {
	int t,r1,r2,r3,r4;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d %d %d %d",&r1,&r2,&r3,&r4);
	    if(r1>0 || r2>0 || r3>0 || r4>0)
	        printf("OUT\n");
	    else
	        printf("IN\n");
	}
	
	return 0;
}
