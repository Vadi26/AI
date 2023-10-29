import copy

gameMatrix = [[-1, -1, -1],
              [-1, -1, -1], 
              [-1, -1, -1]]

new = copy.deepcopy(gameMatrix)

new[0][0] = 0

print(gameMatrix)
print(new)