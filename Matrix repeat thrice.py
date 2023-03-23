'''
The program must accept a number matrix having R rows and C columns. 
Then the program must check whether a number is repeated consecutively for 3 times either in a row, in a column or along a diagonal. 
If there are more than one such repeated numbers then the program must print the minimum value V. 
The program must print -1 if no such value is repeated. 

Note: C = R+1 

Boundary Condition(s): 1 <= R <= 20 

Input Format:  The first line contains R. 
               The next R lines contain C integer values separated by a space. 

Output Format: The first line contains V. 

Example Input/Output 1: 

Input:  7
        2 3 4 5 6 2 4 3
        2 3 4 7 6 7 6 2
        2 3 5 5 5 5 2 5
        2 3 1 1 2 1 3 6 
        10 1 1 1 9 0 3 51 
        2 10 1 1 5 1 51 7
        5 2 10 1 1 51 2 1 

Output: 1 

Explanation: The repeated values are 5 1 2 3 10 51. The minimum value is 1. 

Example Input/Output 2: 

Input:  9 
        648 318 24 374 376 616 6 308 222 944 
        100 321 34 861 551 871 440 334 583 294 
        676 500 98 694 324 466 869 516 362 680 
        883 212 599 315 338 115 152 585 118 469 
        867 517 180 97 69 27 479 626 462 277
        661 988 150 578 17 217 978 509 263 660
        76 337 306 774 520 423 619 181 838 757 
        156 658 786 198 764 473 211 746 196 670
        962 857 159 420 766 377 738 747 674 624 

Output: -1 

Example Input/Output 3: 

Input:  9 
        648 318 24 374 376 616 6 308 222 944 
        100 321 34 861 551 871 440 334 944 294 
        676 500 98 694 324 466 869 944 362 680
        883 212 599 315 338 115 152 585 118 469 
        867 517 180 97 69 27 479 626 462 277 
        661 988 150 578 17 217 978 509 263 660
        76 337 306 774 520 423 619 181 838 747
        156 658 786 198 764 473 211 746 747 670
        962 857 159 420 766 377 738 747 674 624

Output: 747 

Example Input/Output 4: 

Input:  9 
        648 318 24 883 376 616 6 308 222 944 
        100 321 883 861 551 871 440 334 583 294 
        676 883 98 694 324 466 869 516 362 680
        883 212 599 315 338 115 152 585 118 469 
        867 517 180 97 69 27 479 626 462 277 
        661 988 150 578 17 217 978 766 263 660 
        76 337 306 774 520 423 766 181 838 757
        156 658 786 198 764 766 211 746 196 670 
        962 857 159 420 766 377 738 747 674 624
        
Output: 766

SOLUTION:
'''
