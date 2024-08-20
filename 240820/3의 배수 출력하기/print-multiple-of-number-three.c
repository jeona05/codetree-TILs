#include <stdio.h>

int main() {
    int n, i = 1;
    scanf("%d", &n);
    while (3*i <= n) {
        printf("%d ", i*3);
        i++;
    }
    return 0;
}