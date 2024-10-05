# Magic Numbers Algorithm
Trying to find an algorithm that is able to win the Magic Numbers game in less than 5 movements.

## The game
Magic Numbers is a variant of the famous game Mastermind.

There are two main differences:
- While in Mastermind you have 6 possible colors (or numbers), in Magic Numbers you have 10 different numbers (from 0 to 9).
- While in Mastermind you can repeat colors, in Magic Numbers the secret code is build with 4 unique numbers.

## The main idea of the algorithm
After a research, it has been found that the best algorithm to found the secret guess using minimum guesses was the Knuth algorithm (Knuth, 1976-77), which is based in the Minimax strategy. Applying this algorithm to Mastermind, it is possible to crash the secret code with a maximum number of guesses of 5. So in this code, it has been implemented this algorithm in order to solve it using the minimum number of guesses.

Because of the differences between Mastermind and Magic Numbers, it has been shown that the minimum number of guesses needed to crash the number is bigger in Magic Numbers than in Mastermind.

## How it works

### Functions to simulate games

#### GenerateNumberList():
Generates a list of all possible numbers, having unique digits.

#### chooseRandomNumber():
Choose a random number from the list generated in order to have a secret code.

#### checkGuess(guess, secret):
Compare the guess and the secret number and returns a feedback list with the number of mates and checks, respectively.
Recieves as parameters the guess you make and the secret code.

#### precalcFeedbacks(numberList):
In order to optimize the code and reduce the computation time, this function calculates all possible feedbacks between all numbers and save them in a dictionary. With this dictionary, it is not necessary to calculate the feedback everytime, but look for it in this dictionary.

#### formatFeedback(guess, feedback):
Gives a visual feedback about the guess.

#### randomGuess(numberList):
Makes a random guess. Just for simulation testing purposes.

### Functions to implement Knuth algorithm

#### reduce(numberList, guess, feedback, feedbacksTable):
Reduce the list of possible numbers based on feedback stored in the dictionary with precalculated feedbacks.

#### selectGuess(numberList, feedbacksTable):
This function uses the Minimax strategy to select the next guess. 

## To Do
At this moment, optimizing works are needed in order to reduce the simulation time. The main idea to reduce this time is to implement parallel processing, which will be implemented soon, and create a file of all feedbacks, to avoid calculate them every time the simulation starts.

The other point to work on is to change the engine to work with classes instead of different functions.

Finally, in order to deeply understand the statistics of this algorithm when applied to Magic Numbers, new statistical functionalities are needed.