#include <stdio.h>

int main() {
    int a, b = 0, c = 0;
    for (int i = 1; i <= 10; i++) {
        scanf("%d", &a);
        if (a % 3 == 0)
        b++;
        if (a % 5 == 0)
        c++;
    }
    printf("%d %d", b, c);
    return 0;
}