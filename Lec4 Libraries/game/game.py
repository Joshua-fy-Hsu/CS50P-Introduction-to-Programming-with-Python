import random
import sys

while True:
    try:
        n = int(input("Level: "))

        if n < 0:
            pass

        target = random.randint(1, n)
        
        while True:
            try:
                guess = int(input("Guess: "))

                if guess < 0:
                    pass

                if guess < target:
                    print("Too small!")
                    pass
                elif guess > target:
                    print("Too large!")
                else:
                    print("Just right!")
                    sys.exit()

            except ValueError:
                pass

    except ValueError:
        pass
    




