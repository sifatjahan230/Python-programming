'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
2<=n<=10
-100<=A[i]<=100
The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.
'''

input()
a=list(map(int,input().split()))
m=max(a)
print(max((x for x in a if x!=m)))
