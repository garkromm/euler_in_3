#include <stdio.h>
#include <math.h>
// Special Pythagorean triplet
// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
// a^2 + b^2 = c^2
// For example, 32 + 42 = 9 + 16 = 25 = 52.
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

int special_pyt_tripplet(int sum);

void main()
{
    int sum = 1000;
    int answer = special_pyt_tripplet(sum);
    printf("%d\n", answer);
}

int special_pyt_tripplet(int sum)
{
    int a, b, c;
    // a < b < c
    for (a = 1; a < sum / 3; a++)
    {
        for (b = 2; b < sum / 2; b++)
        {
            c = (sum - a - b);
            if (a * a + b * b == c * c)
            {
                return a * b * c;
            }
        }
    }
    return 0;
}