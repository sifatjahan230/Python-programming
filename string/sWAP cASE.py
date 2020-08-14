'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string S.

Constraints
0<len(S)<=1000

Output Format

Print the modified string S.
'''
def swap_case(s):
    out=''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
