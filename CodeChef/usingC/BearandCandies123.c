#include <stdio.h>

int main(void) {
	int t,a,b;
	scanf("%d",&t);
	while(t--){
	    scanf("%d %d",&a,&b);
	    for(int i=1;;i++)
	    {
    	    if(i%2)
    	    {
    	        a = a - i;
    	        if(a<0)
    	        {
    	            printf("Bob\n");
    	            break;
    	        }
    	    }
    	    else{
    	        b = b - i;
    	        if(b<0)
    	        {
    	            printf("Limak\n");
    	            break;                                                                                                         
    	        }
    	    }
    	       
	    }
	}
	return 0;
}

