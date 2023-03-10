/*
The program must accept three integers X, Y and Z as the input. Each of these are four-digit integers. 
The program must generate a four-digit key K based on the following conditions.

- The 1st digit in K must be equal to the SMALLEST digit in the thousands place of all three integers.
- The 2nd digit in K must be equal to the LARGEST digit in the hundreds place of all three integers. 
- The 3rd digit in K must be equal to the SMALLEST digit in the tens place of all three integers.
- The 4th digit in K must be equal to the LARGEST digit in the units place of all three integers.

Boundary Condition(s): 1000 <= X, Y, Z = 9999 

Input Format:  The first line contains X, Y and Z separated by a space. 
Output Format: The first line contains K. 

Example Input/Output 1: 

Input:  107 1234 2948 
Output: 1908 

Explanation: The digits in the thousands place of all three integers are 5, 1 and 2. Here 1 is the smallest digit, so 1 is printed. 
The digits in the hundreds place of all three integers are 1, 2 and 9. Here 9 is the largest digit, so 9 is printed. 
The digits in the tens place of all three integers are 0, 3 and 4. Here 0 is the smallest digit, so 0 is printed. 
The digits in the units place of all three integers are 7, 4 and 8. Here 8 is the largest digit, so 8 is printed.

Example Input/Output 2: 

Input:  596 7413 2100 
Output: 2406

SOLUTION:
*/
