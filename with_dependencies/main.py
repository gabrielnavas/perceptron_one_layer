import numpy as np

stepFunction = lambda sum: 1 if sum > 0.00 else 0

def main():
  inputs = np.array([1, 7, 5])
  weights = np.array([0.8, 0.1, 0])

  weightsSum = inputs.dot(weights)
  oneOrTwo = stepFunction(weightsSum)
  print('functions result: ', oneOrTwo) # 1

main()