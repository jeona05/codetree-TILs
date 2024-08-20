#include <stdio.h>

int main() {
    int n, i;
    scanf("%d", &n);
    i = 1;
    while (i<=n){
        printf("%c\n", '*');
        i++;
    }

    return 0;
}