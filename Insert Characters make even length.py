'''
The program must accept a string S and an integer K as the input. 
The program must modify the given string K times based on the following conditions. 

- If the length of the string is odd, then the program must append or prepend an asterisk alternatively to make the length even.
- Once the length becomes even, then the program must insert the string "#x#" at the middle of S (where x ranges from 1 to K). 

Finally, the program must print the revised string S as the output. 

Boundary Condition(s): 1 <= Length of S <= 100 
                       1 <= K <= 1000 
                       
Input Format:  The first line contains S. The second line contains K. 
Output Format: The first line contains the revised string S.

Example Input/Output 1:

Input:  rock 
        3 
        
Output: *ro#1##3#2##ck* 

Explanation: 

Here K = 3. 
After the 1st modification, the string becomes ro#1#ck. 
After the 2nd modification, the string becomes ro#1#2##ck*. 
After the 3rd modification, the string becomes *ro#1##3#2##ck*. 

Example Input/Output 2: 

Input:  MANGO 
        6 

Output: ***MAN##2##4##6#5##3##1#GO*** 

Example Input/Output 3: 

Input:  RING 
        14
Output: ****RI#1##3##5##7##9#1#1#1#1#14#3#2#1#0##8##6##4##2##NG*****

SOLUTION:
'''
