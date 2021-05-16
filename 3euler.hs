import Data.List

-- Largest prime factor
--
-- The prime factors of 13195 are 5, 7, 13 and 29.
-- What is the largest prime factor of the number 600851475143 ?

findSmallestFactor :: Int -> Maybe Int
findSmallestFactor n = do
    let limit = floor $ sqrt $ fromIntegral n
    find (\x -> n `mod` x == 0) [2..limit]

largestPrime :: Int -> Int
largestPrime n = case findSmallestFactor n of
    Just factor -> largestPrime $ n `div` factor
    Nothing -> n

numb :: Int
numb = 600851475143

main = print $ largestPrime numb