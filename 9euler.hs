-- Special Pythagorean triplet
-- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
-- a^2 + b^2 = c^2
-- For example, 32 + 42 = 9 + 16 = 25 = 52.
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.

sumN = 1000

specialPytTripplet :: Int -> Int
specialPytTripplet n = head [a*b*(sumN-a-b) | a <- [1..(sumN `div` 3)], b <- [2..(sumN `div` 2)], a*a + b*b == (sumN-a-b)*(sumN-a-b)]

main = print $ specialPytTripplet sumN