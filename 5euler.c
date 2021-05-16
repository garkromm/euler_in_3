#include <stdio.h>

// Smallest multiple
// 2520 is the smallest number that can be divided by each of the
// numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

void main()
{
    int x = 1;
    int answer = 0;
    int limit = 20;

    while (1)
    {
        for (int i = 1; i <= limit; i++)
        {
            if (x % i != 0)
            {
                break;
            }
            if (i == limit)
            {
                answer = x;
            }
        }
        if (answer != 0)
        {
            break;
        }
        x++;
    }

    printf("%d\n", answer);
}