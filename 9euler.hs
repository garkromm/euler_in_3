-- Special Pythagorean triplet
-- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
-- a^2 + b^2 = c^2
-- For example, 32 + 42 = 9 + 16 = 25 = 52.
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.
-- u^2 + uv = 500 // u(u+v) = 500 // for v > 0 ==> u > 23 because u > sqrt(500)
-- TODO find bounds

sumN = 1000

-- specialPytTripplet :: Int -> Int
-- specialPytTripplet n = head [a*b*(sumN-a-b) | a <- [1..(sumN `div` 3)], b <- [2..(sumN `div` 2)], a^2 + b^2 == (sumN-a-b)^2]

sideA u v k = k*(u^2 - v^2)
sideB u v k = k*2*u*v
sideC u v k = k*(u^2 + v^2)
prodABC u v k = (sideA u v k)*(sideB u v k)*(sideC u v k)
condTrip u v k = (sideA u v k) + (sideB u v k) + (sideC u v k) == sumN

specialPytTripplet :: Int -> Int
specialPytTripplet n = head [prodABC u v k | u <- [2..], v <- [1..], k <- [1..], condTrip u v k]



main = print $ specialPytTripplet sumN
