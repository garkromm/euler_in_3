#include <stdio.h>
#include <math.h>
// 10001st prime
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

int is_prime(int n);

void main()
{
    int answer = 1;
    int count = 1;
    int limit = 10001;
    int i = 2;
    while (count <= limit)
    {
        if (is_prime(i))
        {
            answer = i;
            count++;
        }

        i++;
    }
    printf("%d\n", answer);
}

int is_prime(int n)
{
    if (n == 2)
    {
        return 1;
    }
    if (n % 2 == 0)
    {
        return 0;
    }
    for (int i = 3; i <= (int)sqrt(n); i += 2)
    {
        if (n % i == 0)
            return 0;
    }
    return 1;
}
