#include <stdio.h>

int main() {
    int a, b, c, min;
    scanf("%d %d %d", &a, &b, &c);
    if (a <= b && a <= c)
    min = a;
    else if (b <= a && b <= c)
    min = b;
    else if (c <= a && c <= b)
    min = c;

    if (a == min)
    printf("1 ");
    else
    printf("0 ");
    if (a==b && b==c)
    printf("1");
    else
    printf("0");
    return 0;
}