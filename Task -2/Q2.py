mylist = []
n = int(input())

for i in range(n):
    command_parts = input().split() #هجزا الكومند عشان اعرف اقراه و اخد الجزء الاول اقارنه
    command = command_parts[0]
    
    
    if command == "insert":
        index = int(command_parts[1])
        element = int(command_parts[2])#كدا اكون خزنت القيم للانسرت
        mylist.insert(index, element)
    elif command == "print":
        print(mylist)
    elif command == "remove":
        element = int(command_parts[1])
        mylist.remove(element)
    elif command == "append":
        element = int(command_parts[1])
        mylist.append(element)
    elif command == "sort":
        mylist.sort()
    elif command == "pop":
        mylist.pop()
    elif command == "reverse":
        mylist.reverse()
        