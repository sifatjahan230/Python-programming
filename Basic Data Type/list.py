'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N=4
append 1
append 2
insert 3 1
print

: Append 1: Append 1 to the list,arr=[1] .
: Append 2: Append 2 to the list,arr=[1,2] .
: Insert 3 1: Insert 3 at index 1,[1,3,2] .
: Print the array.'''
N = int(input())
L = []
for i in range(N):
    command = input().split()
    if command[0] == 'print':
        print(L)
    elif command[0] == 'append':
        L.append(int(command[1]))
    elif command[0] == 'insert':
        L.insert(int(command[1]), int(command[2]))
    elif command[0] == 'remove':
        L.remove(int(command[1]))
    elif command[0] == 'reverse':
        L.reverse()
    elif command[0] == 'sort':
        L.sort()
    elif command[0] == 'pop':
        L.pop()
