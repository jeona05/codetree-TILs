#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if ( (a > b && a > c && b > c) || (c > a && c > b && a < b) )
    printf("%d", b);
    else if ( (a > b && a > c && b < c) || (b > a && b > c && c > a) )
    printf("%d", c);
    else if ( (b > c && b > a && a > c ) || (c > a && c > b && a > b) )
    printf("%d", a);
    return 0;
}