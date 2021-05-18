#include <stdio.h>
#include <stdlib.h>

// Smallest multiple
// 2520 is the smallest number that can be divided by each of the
// numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

// https://en.wikipedia.org/wiki/Least_common_multiple
// https://en.wikipedia.org/wiki/Euclidean_algorithm

int gcd(int x, int y);
int lcm(int x, int y);

void main()
{
    int answer = 1;
    int limit = 20;
    for (int i = 2; i < limit; i++)
    {
        answer = lcm(answer, i);
    }
    printf("%d\n", answer);
}

int lcm(int x, int y)
{
    return abs(x * y) / gcd(x, y);
}

int gcd(int x, int y)
{
    if (y == 0)
    {
        return x;
    }
    else
    {
        return gcd(y, x % y);
    }
}

// void main()
// {
//     int x = 1;
//     int answer = 0;
//     int limit = 20;

//     while (1)
//     {
//         for (int i = 1; i <= limit; i++)
//         {
//             if (x % i != 0)
//             {
//                 break;
//             }
//             if (i == limit)
//             {
//                 answer = x;
//             }
//         }
//         if (answer != 0)
//         {
//             break;
//         }
//         x++;
//     }

//     printf("%d\n", answer);
// }
