#include <stdio.h>
int main(void) {
    int n,i=10;
    scanf("%d",&n);
    while(i>0){
        if(n%i==0)
        {
            printf("%d",i);
            break;
        }
        i--;
    }
	return 0;
}