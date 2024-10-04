from engine import *

def main():
    NUM_SIMULATIONS = 100
    numGuessesList = []  # List containing needed guesses to win in each round
    
    # Generate the full list of numbers and precalculate all feedbacks
    NUMBER_LIST = generateNumberList() 
    print("Precalculating feedbacks...")
    feedbacksTable = precalcFeedbacks(NUMBER_LIST)
    print("Done!")
    print("Start game simulations")

    for i in range(NUM_SIMULATIONS):
        numListCopy = NUMBER_LIST[:]  # List of remaining possible numbers
        secret = chooseRandomNumber(NUMBER_LIST)  # Choose the secret number randomly
        totalGuesses = 0
        guess = "0123"  # Initial guess (following Knuth's strategy)

        while True:
            totalGuesses += 1
            feedback = feedbacksTable[(guess, secret)]  # Retrieve feedback from precalculated table

            if feedback[0] == 4:  # If 4 mates, the guess is correct
                numGuessesList.append(totalGuesses)
                print(f"Round finished in {totalGuesses} guesses.")
                break

            # Reduce the list of possible numbers based on the feedback
            numListCopy = reduce(numListCopy, guess, feedback, feedbacksTable)


            # Use Minimax strategy to select the next guess
            guess = selectGuess(numListCopy, feedbacksTable)
    
    # Calculate and print the average number of guesses through all simulations
    average(numGuessesList, NUM_SIMULATIONS)

    #Calculate the mode of the guesses through all simulations
    mode(numGuessesList)

if __name__ == "__main__":
    main()