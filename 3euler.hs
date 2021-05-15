-- Largest prime factor
-- The prime factors of 13195 are 5, 7, 13 and 29.

-- What is the largest prime factor of the number 600851475143 ?

-- TODO still not working, fix it

largestPrime n = do 
    let largest = itterPrimes n 2 (primesFromTo 2 n)
    print largest


itterPrimes n prime (x:xs) 
    | n == 1 = prime
    | n `rem` prime == 0 = itterPrimes (quot n prime) (prime+1) (primesFromTo prime+1 n)
    | otherwise = itterPrimes n (prime+1) (primesFromTo (prime+1) n)


primesFromTo m n = filter isPrime [m..n]

-- stolen from https://wiki.haskell.org/Prime_numbers
isPrime n = n > 1 && noDivs n primesTD
primesTD  = 2 : 3 : filter (`noDivs` tail primesTD) [5,7..]
noDivs n ds = foldr (\d r -> d*d > n || (rem n d > 0 && r)) True ds

main = largestPrime 192