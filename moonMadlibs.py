from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, zombie, hungergames, code])
    m.madlib()
