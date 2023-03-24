'''
You are required to complete the given code. You can click on Run anytime to check the compilation/execution status of the program. 
You can use printf to debug your code. The submitted code should be logically/syntactically correct and pass all test cases. 
Do not write the main() function as it is not required. 

Code Approach: For this question, you will need to complete the code as in the given implementation. We do not expect you to modify the approach. 

The function/method productOfSums accepts two arguments - SIZE and arr, an integer representing the size of the integer array arr and the integer array arr. 
The array can be divided into two parts, where the first part of the array (starting from 0 to i) is in ascending order and the second part of the array 
(starting from i to SIZE-1) is in descending order. 

The function/method productOfSums must find the sum of the first part F and the sum of the second part S. 
Finally, the function must return an integer representing the product of F and S. 

The function must return -1 if the size of the array is less than 3.

Your task is to complete the code in the function productOfSums so that it passes all the test cases. 

Boundary Condition(s): 1 <= N <= 100 
                      -10^5 <= Each integer value <= 10^5 

Example Input/Output 1:

Input:  7 
        4 7 15 11 10 5 2

Output: 1118 

Explanation:  The sum of integers in the first part of the array is 26 (4 + 7 + 15). 
              The sum of integers in the second part of the array is 43 (15 + 11 + 10 + 5 + 2). 
              The product of 26 and 43 is 1118.

Example Input/Output 2: 

Input:   4 
         4 8 -9 -10
Output: -132
