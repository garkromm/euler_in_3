import System.Random
import System.Random.Shuffle

progLangs = ["C", "Haskell", "Python"]
progMulti = concat $ replicate 3 progLangs

main = do
    gen <- getStdGen
    print $ shuffle' progMulti (length progMulti) gen

