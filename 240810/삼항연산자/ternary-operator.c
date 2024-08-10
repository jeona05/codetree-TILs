#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);
    int b = a == 100 ? 0 : 1;
    if (b == 0)
    printf("pass");
    else
    printf("failure");
}