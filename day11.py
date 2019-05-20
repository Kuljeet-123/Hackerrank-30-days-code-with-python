Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context 
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .


#######################################################################################################################
My Code........................
grid = list()

for i in range(6):
    row = input().strip().split(' ')
    row = list(map(int, row))
    grid.append(row)

def _get_hourglass_sum(grid, i, j):
    sum = 0
    sum += grid[i-1][j-1]
    sum += grid[i-1][j]
    sum += grid[i-1][j+1]
    sum += grid[i][j]
    sum += grid[i+1][j-1]
    sum += grid[i+1][j]
    sum += grid[i+1][j+1]
    return sum

# start max_hourglass_sum at smallest possible hourglass
max_hourglass_sum = -63
for i in range(1,5):
    for j in range(1, 5):
        current_hourglass_sum = _get_hourglass_sum(grid, i, j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum

print(max_hourglass_sum)
