#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n >= 100)
    printf("vapor");
    else if (n < 0)
    printf("ice");
    else
    printf("water");
    return 0;
}