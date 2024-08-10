#include <stdio.h>

int main() {
    char a1, a2, a3;
    int b1, b2, b3, cnt;
    cnt = 0;
    scanf("%c %d\n%c %d\n%c %d", &a1, &b1, &a2, &b2, &a3, &b3);
    if (a1 == 'Y' && b1 >= 37)
    cnt += 1;
    if (a2 == 'Y' && b2 >= 37)
    cnt += 1;
    if (a3 == 'Y' && b3 >= 37)
    cnt += 1;
    if (cnt >= 2)
    printf("E");
    else
    printf("N");
    return 0;
}