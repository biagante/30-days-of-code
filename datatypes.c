#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";

    int si;
    double sd;
    char str[100]; // this is not scalable for input of unknown size

    // Read inputs from stdin
    scanf("%d", &si);
    scanf("%lf", &sd);
    scanf("%*[\n] %[^\n]", str); 

    // Print outputs to stdout
    printf("%d\n", i + si);
    printf("%.01lf\n", d + sd);
    printf("%s%s", s, str);

    return 0;
}
