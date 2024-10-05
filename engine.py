import random
import pickle

def generateNumberList():
    '''
    Generates a list of possible numbers.
    '''
    numberList = []
    number = ""
    for i in range (0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        number = str(i)+str(j)+str(k)+str(l)
                        numberList.append(number)
                        number = ""
    return numberList

def chooseRandomNumber(numberList):
    '''
    Choose a random number from a list.
    '''
    randomIndex = random.randint(0, len(numberList) - 1)
    randomNumber = numberList[randomIndex]
    return randomNumber

def checkGuess(guess, secret):
    '''
    Compare your guess and the secret number and return
    feedback list with the numbers of mates and checks,
    respectivevly.
    '''
    if guess == secret:
        return [4, 0]
    
    feedback = [0, 0]
    pos = 0

    for digit in guess:
        if digit in secret:
            if digit == secret[pos]:
                feedback[0] += 1
            else:
                feedback[1] += 1
        pos += 1
    
    return feedback

def precalcFeedbacks(numberList):
    ''' Precompute feedbacks for every pair of guess-secret combinations. '''
    feedbackTable = {}
    for guess in numberList:
        for secret in numberList:
            feedback = tuple(checkGuess(guess, secret))
            feedbackTable[(guess, secret)] = feedback
    return feedbackTable

def formatFeedback(guess, feedback):
    '''
    Gives a visual feedback about the guess.
    '''
    print("Guess:", guess)
    print("Mates:", feedback[0], "Checks:", feedback[1])

def randomGuess(numberList):
    '''
    Makes a guess randomly. Just for simulation testing purposes.
    '''
    index = random.randint(0, len(numberList) -1)
    return numberList[index], index

'''
Save and load a file of precalcFeedback
'''

def feedbacks2file(feedbackTable, filename="feedbacksTable"):
    '''
    Serializes and saves the feedbacks table to a file.
    '''
    with open(filename, 'wb') as file:
        pickle.dump(feedbackTable, file)
    print(f"Feedbacks table saved to {filename}")

def file2feedbacks(filename="feedbacksTable"):
    '''
    Loads serialized feedbacks from a file.
    '''
    with open(filename, 'rb') as file:
        feedbackTable = pickle.load(file)
    print(f"Feedbacks table loaded from {filename}")
    
    return feedbackTable

'''
To apply the Knuth algorithm
'''

def reduce(numberList, guess, feedback, feedbacksTable):
    ''' Reduce the list of possible candidates based on feedback using precalculated feedbacks. '''
    return [number for number in numberList if feedbacksTable[(guess, number)] == feedback]

def selectGuess(numberList, feedbacksTable):
    ''' Use Minimax strategy to select the next guess. '''
    minWorstCase = float('inf')
    bestGuess = None

    for guess in numberList:
        feedbackGroups = {}
        
        for number in numberList:
            feedback = feedbacksTable[(guess, number)]

            if feedback not in feedbackGroups: feedbackGroups[feedback] = 0
            feedbackGroups[feedback] += 1
            if feedbackGroups[feedback] > minWorstCase: break
        
        print(f"Feedback groups: {feedbackGroups}")

        worstCase = max(feedbackGroups.values())
        
        if worstCase < minWorstCase:
            minWorstCase = worstCase
            bestGuess = guess

        print(f"worst case: {worstCase}")

    return bestGuess


'''
Statistical functions
'''

def average(numGuessesList, numSimulations):
    '''
    Calculates the average of guesses needed to break the code through all simulations and print the result
    '''
    average = sum(numGuessesList)/numSimulations
    print(f"Simulation of {numSimulations} games completed.")
    print(f"The average tries needed to guess the number is: {average:.2f}")

def mode(numGuessesList):
    '''
    Calculates the mode of the number of guesses needed to break the code through all simulations.
    It also find out if there is more than one mode, so we find if the collection of values is modal, bimodal or multimodal.
    '''
    freq = {}
    for number in numGuessesList:
        if number not in freq.keys():
            freq[number] = 0
        freq[number] += 1
    
    value = 0
    mode = []
    for number, count in freq.items():
        if count == value: mode.append(number)
        elif count > value: 
            mode = [number]
            value = count

    print(f"The mode of guesses is: {mode} with a frequency of: {value}")
    print(f"Frequency table:")
    
    for item in freq.items():
        print(f"Frequency of: {item}")