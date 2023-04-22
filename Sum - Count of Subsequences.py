'''
The program must accept N integers as the input. The program must find the sum of N integers as S. 
Then the program must print the count of subsequences whose sum is equal to S-1 as the output. 

Boundary Condition(s): 1 <= N, Each integer value <= 10^5 

Input Format:  The first line contains N. The second line contains N integers separated by a space. 
Output Format: The first line contains an integer value representing the count of subsequences whose sum is equal to S-1. 

Example Input/Output 1: 

Input:  7 
        10 5 2 1 6 1 8 
        
Output: 2 

Explanation: Here N=7 and the given 7 integers are 10 5 2 1 6 1 8. 
             The sum of given 7 integers is 33. 
             All the possible subsequences whose sum is equal to 32 are given below.
             10 5 2 1 6 8 and 10 5 2 6 1 8. 
             The count of subsequences is 2, so 2 is printed as the output. 
             
Example Input/Output 2: 

Input:  8 
        6 14 2 11 5 4 9 20 
        
Output: 0

SOLUTION:
'''
