#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    for (int i = a; i <= b;) {
        printf("%d ", i);
        if (i % 2 == 0)
        i += 3;
        else
        i *= 2;
    }
    return 0;
}