Task 
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Input Format

The first line contains an integer,  (the number of test cases). 
Each line  of the  subsequent lines contain a String, .

Constraints

Output Format

For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.


###########################################################################################################################
My Code..............................
# Enter your code here. Read input from STDIN. Print output to STDOUT
for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])

