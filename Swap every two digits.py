'''
The program must accept two integers X and Y as the input. The program must swap every two digits in both X and Y. 
Then the program must print the sum of the revised values of X and Y as the output. 
If the number of digits in an integer is odd, the last digit remains the same as there is no digit to swap. 

Boundary Condition(s): 1 <= X, Y <= 10^8 

Input Format:  The first line contains X and Y separated by a space. 
Output Format: The first line contains the sum of the revised values of X and Y.

Example Input/Output 1: 

Input:  27521 7809 
Output: 81041 

Explanation: After swapping every two digits in X, it becomes 72251. 
             After swapping every two digits in Y, it becomes 8790. 
             The sum of 72251 and 8790 is 81041. 
             So 81041 is printed as the output. 

Example Input/Output 2: 

Input:  1005 12345 
Output: 21585 

Explanation: After swapping every two digits in X, it becomes 150. 
             After swapping every two digits in Y, it becomes 21435. 
             The sum of 150 and 21435 is 21585. 
             So 21585 is printed as the output.

SOLUTION:
'''

X, Y = map(int, input().split())
Liz_X = list(str(X)); Liz_Y = list(str(Y))
for i in range(0, len(Liz_X) - 1, 2):
    Liz_X[i], Liz_X[i + 1] = Liz_X[i + 1], Liz_X[i]
    X = int("".join(Liz_X))
for j in range(0, len(Liz_Y) - 1, 2):
    Liz_Y[j], Liz_Y[j + 1] = Liz_Y[j + 1], Liz_Y[j]
    Y = int("".join(Liz_Y))
print(X+Y)
