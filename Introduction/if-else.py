'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.'''
num=int(input());

if((2<=num<=5)&(num%2==0)):
    print("Not Weird")
elif((6<=num<=20)&(num%2==0)):
    print("Weird")
elif((num%2==0)&(num>20)):
    print("Not Weird")
else:
    print("Weird")
