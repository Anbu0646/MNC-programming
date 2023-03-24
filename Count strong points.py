'''
The program must accept an integer matrix of size RxC as the input. The program must print the number of strong points in the given matrix as the output. The strong points are located at the element(s) whose all the surrounding elements are smaller than the given element. 

Boundary Condition(s): 2 <= R, C <= 50 
                       1 <= Matrix element value <= 1000 

Input Format:  The first line contains R and C separated by a space. 
               The next R lines, each containing C integers separated by a space. 
Output Format: The first line contains the number of strong points in the given matrix. 

Example Input/Output 1: 

Input: 3 3 
       56 92 45
       19 41 51
       55 31 80 

Output: 3 

Explanation: The 3 strong points are given below. 
		 92 > [56, 19, 41, 51, 45] 
		 55 > [19, 41, 31] 
		 80 > [41, 51, 31] 
Hence the output is 3. 

Example Input/Output 2: 

Input: 6 5 
	 69 45 47 35 62 
	 43 68 22 55 72 
       53 96 21 24 49
       89 34 86 10 37 
       94 31 93 12 70 
       74 81 13 60 95 

Output: 6

SOLUTION:
'''

