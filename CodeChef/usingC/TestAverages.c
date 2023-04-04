#include <stdio.h>

int main(void) {
	int t,m1,m2,m3;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d %d %d",&m1,&m2,&m3);
	    if((m1+m2)/2>=35 && (m1+m3)/2>=35 && (m3+m2)/2>=35 && (m1+m2+m3)/3>=35)
	        printf("PASS\n");
	    else
	        printf("FAIL\n");
	}
	
	return 0;
}

