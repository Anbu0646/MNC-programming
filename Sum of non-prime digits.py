'''
The program must accept an integer N as the input. The program must print the sum of non-prime digits in N as the output. 
If there is no such digit, the program must print -1 as the output. 

Condition(s): 1 <= N <= 10^8 

Input Format:  The first line contains N. 
Output Format: The first line the sum of non-prime digits in N or -1. 

Example Input/Output 1:

Input:  219517 
Output: 11 

Explanation: The non-prime digits in 219517 are 1, 9 and 1. 
             The sum of non-prime digits is 11 (1 + 9 + 1).
             So 11 is printed.
             
Example Input/Output 2:

Input:  3005 
Output: 0

Explanation:  The non-prime digits in 3005 are 0 and 0. 
              The sum of non-prime digits is 0. 
              So 0 is printed. 
              
Example Input/Output 3:

Input:  725
Output: -1

SOLUTION:
'''

def isprime(N):
    if N<=1:
        return False
    for i in range(2, N+1):
        if N%i == 0:
            return False
    return True
    
N = input().strip()
flag = 0
sumq = 0

for i in N:
    if not isprime(int(i)):
        sumq+=int(i) 
        flag = 1

if flag==0: print(-1)
else: print(sumq)
