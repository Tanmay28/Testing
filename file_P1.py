choice = 1
flag1 = 0
while choice >= 1 and choice <= 3:
    flag = 1
    print()
    print('Option 1: Create a new file')
    print('Option 2: Find and Replace')
    print('Option 3: View file')
    print('Option 4: Exit')
    print()
    while flag == 1:
        try:
            flag = 0
            choice = int(input('Enter your choice(1-4) : '))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again.")
            flag = 1
    if choice == 1:
        print()
        fName = input('Enter the File Name: ')
        print('Enter the data you wish to enter into the File ' + fName + ' ')
        data = input()
        with open(fName, 'w') as newF:
            newF.write(data + '\n')
    if choice == 2:
        print()
        fName = input('Enter the File Name: ')
        flag1 = 0
        try:
            with open(fName, 'r') as findF:
                data = findF.read()
        except IOError as e:
            print("No such file exists! Please try again")
            flag1 = 1
        while flag1 == 0:
            old = input('Enter the term to be searched: ')
            new = input('Enter the term to replace '+old+' with: ')
            data = data.replace(old,new)
            with open(fName, 'w') as repF:
                repF.write(data)
            flag1 = 1
    if choice == 3:
        print()
        fName = input('Enter the File Name: ')
        with open(fName, 'r') as readF:
            for line in readF:
                print(line.rstrip())
