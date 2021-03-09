inputs = [1,7,5]
weights = [0.8, 0.1, 0]

def stepFunction(x: float) -> int:
  if(x > 0.00):
    return 1
  return 0

def sumInputWithWeight(inputs: [], weights: []) -> float:
  weightsSum = 0
  for index in range(len(inputs)):
    product = inputs[index] * weights [index]
    weightsSum += product
  return weightsSum

def main():
  weightsSum = sumInputWithWeight(inputs, weights)
  oneOrTwo = stepFunction(weightsSum)
  print(oneOrTwo) # 1

main()