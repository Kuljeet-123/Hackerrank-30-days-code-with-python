A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , the number of test cases. 
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

######################################################################################
My Code............................
# Enter your code here. Read input from STDIN. Print output to STDOUT
    
import math

def isPrime(n):
    if n <= 1:
        return False
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return False
    for i in range(2, int(sqrt_n)+1):
        if n%i == 0:
            return False
    return True


num_test_cases = int(input())
for i in range(num_test_cases):
    n = int(input())
    if isPrime(n):
        print('Prime')
    else:
        print('Not prime')
