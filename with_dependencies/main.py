import numpy as np

inputs = np.array([1,7,5])
weights = np.array([0.8, 0.1, 0])

def stepFunction(x: float) -> int:
  if(x > 0.00):
    return 1
  return 0

def sumInputWithWeight(inputs: [], weights: []) -> float:
  """
    dot product, use numpy 
    to great performance 
    sum = inputs[0] x weights[0] +
    inputs[1] x weights[1] +
    inputs[2] x weights[2] +
  """ 
  sum = inputs.dot(weights)
  return sum

def main():
  weightsSum = sumInputWithWeight(inputs, weights)
  oneOrTwo = stepFunction(weightsSum)
  print(oneOrTwo) # 1

main()