import numpy as np
import pandas as pd
# GOAL: Generate line of x words given an initial word + track runtime between two solutions
#* THIS IS A FIRST-ORDER MODEL: only considers T(n-1) for T(n) - "memoryless" property of a stochastic process

######## Take in input #########
# Get user input (initial word, and number of words to generate after it)
initial = input()
print(f"{initial}")
x = int(input())
print(f"{x}")
# TODO: Get user input (method of predicting x words: it or diag)

# Get ordered list of words
words = ["\n"]
line = input()
for word in line.split(','):
    words.append(word)
    # print(f"{word} ")
# record transition matrix
n = len(words) # + 1 if taking in csv, because csv doesn't include \n
print(f"{n} x {n}")
matrix = [[] for i in range(n)]
# npmatrix = np.zeros((n, n))

for i in range(0, n):
    try:
        row = input()
        for val in row.split(','):
            matrix[i].append(float(val))
            # print(f"{val} ")
    except EOFError: # reached end of file
        break

######## Functionality ######## 
#* 1. Get transformation matrix and an initial state
# transpose matrix
tmatrix = np.transpose(matrix)

print(f"{tmatrix}")

initialState = np.array([0 for i in range(n)])
initialState[words.index(initial)] = 1
# transform input from row to column vector
initialState.shape = (n, 1)
# print(f"{input}")

#* 2. Predict resultant state after n steps using - 
# TODO: Solution 1: for-loop OR recursive
nextState = initialState
for i in range(x):
    print(f"{nextState}")
    nextState = np.matmul(tmatrix, nextState)
    # transform nextState from nD into 1D array
    nextState1D = np.ndarray.flatten(nextState)
    print(f"{pd.Series(nextState1D).idxmax()}: {words[pd.Series(nextState1D).idxmax()]}")
    nextWord = pd.Series(nextState1D).idxmax()
    nextState = [0 for i in range(n)]
    nextState[nextWord] = 1

# TODO: Solution 2: Diagonalize, then raise to power