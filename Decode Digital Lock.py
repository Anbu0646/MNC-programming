'''
The program must accept an integer X representing the encoded key of a digital lock.
There are two ways to decode the key of the digital lock. 

- If X is an armstrong number, then the key is the sum of even digits in the encoded key. 
- If X is not an armstrong number, then the key is the sum of odd digits in the encoded key. 

An armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits in the number.
The program must decode the key X and print it as the output. 

Boundary Condition(s): 1 <= X <= 10^8 

Input Format:  The first line contains X. 
Output Format: The first line contains the decoded key. 

Example Input/Output 1: 

Input:  1634 
Output: 10 

Explanation: The given integer 1634 (14 + 64 + 34 + 44) is an armstrong number. 
             The sum of even digits in 1634 is 10 (6 + 4). So 10 is printed. 
             
Example Input/Output 2: 

Input:  4105 
Output: 6

SOLUTION:
'''
