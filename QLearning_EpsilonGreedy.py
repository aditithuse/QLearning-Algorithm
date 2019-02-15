import math
import random
import csv

def initialRewardValues(rewardFile):

	reader = open(rewardFile, 'rU')
	i = 0
	for row in reader:
		if i > 0:
			cells = row.split(",")
			R[i-1][0] = (int)(cells[1])
			R[i-1][1] = (int)(cells[2])
			R[i-1][2] = (int)(cells[3])
			R[i-1][3] = (int)(cells[4])

		i = i + 1


def calculateNextState(startState):

	possNextState = [0 for i in range(0,4)]	
	
	for i in range(0,4):

		if (i == 0): 
			if(startState - 10 >= 0):
				possNextState[i] = startState - 10
			else:
				possNextState[i] = -1

		if (i == 1):
			if(startState + 10 < 100):
				possNextState[i] = startState + 10
			else:
				possNextState[i] = -1	

		if (i == 2):
			if(startState - 1 >= 0):
				possNextState[i] = startState - 1
			else:
				possNextState[i] = -1

		if (i == 3):
			if(startState + 1 < 100):
				possNextState[i] = startState + 1
			else:
				possNextState[i] = -1

	return possNextState

def greedyQLearning(startState):

	initialRewardValues(reward)
	iterations = 0

	while(startState != goalState):
		
		possibleActions = []
		possNextState = [0 for i in range(0,4)]
		nextState = 0
		r = 0.0
		qMax = 0
		qMaxExploit = 0

		possNextState = calculateNextState(startState)


		#Determining the next state
		for action in range(0, len(R[startState])):
			if (R[startState][action] != 999.0):
				possibleActions.append(action)

		#getting random number between 0 and 1 and checking with epsilon
		if (len(possibleActions) > 0):
			r = random.uniform(0, 1)

			# exploit
			if r <= epsilon:
				print ("exploit: ", possNextState)
				for action in range(0, len(R[startState])):
					if (R[startState][action] != 999 and qMaxExploit <= Q[startState][action]):
						qMaxExploit = Q[startState][action]
						actionIndex = action
				
				nextState = possNextState[actionIndex]

			# explore
			else:
				print ("explore: ", possNextState)
				actionIndex = possibleActions[(random.randrange(len(possibleActions)))]
				nextState = possNextState[actionIndex]

			print ("nextState",nextState)

			for action in range(0, len(R[nextState])):
					if (R[nextState][action] != 999 and qMax <= Q[nextState][action]):
						qMax = Q[nextState][action]

			# Q calculation
			Q[startState][actionIndex] = Q[startState][actionIndex] + alpha * (R[startState][actionIndex] + (beta * qMax) - Q[startState][actionIndex])
			startState = nextState

			iterations += 1

	print ("\nIterations: ", iterations)
	print ("Q",Q)


def main():
	greedyQLearning(startState)

# reward file
reward = "./reward.csv"

# discount factor
beta = 0.9 
# learning rate
alpha = 0.01
# for greedy algorithm
epsilon = 0.2

#storing the q values
Q = [[0.0 for i in range(4)] for j in range(100)]
R = [[0.0 for i in range(4)] for j in range(100)]

initialRewardValues(reward)

# goal state
goalState = 55
# starting sate
startState = 0

main()
