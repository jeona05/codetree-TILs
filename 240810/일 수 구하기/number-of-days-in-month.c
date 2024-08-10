#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n <= 7){
        if (n % 2 == 1)
        printf("31");
        else if (n == 2)
        printf("28");
        else
        printf("30");
    }
    else{
        if (n % 2 == 1)
        printf("30");
        else
        printf("31");
    }
    return 0;
}