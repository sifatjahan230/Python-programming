'''
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°
'''
from math import atan2
from math import degrees
degree_sign = "\N{DEGREE SIGN}"
ab = float(input())
bc = float(input())
b=str(round(degrees(atan2(ab, bc))))

print( "{}{}".format(b,degree_sign) )
