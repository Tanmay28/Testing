choice=1
while choice>=1 and choice<=3:
    print()
    print('Option 1: Create a new file')
    print('Option 2: Find and Replace')
    print('Option 3: View file')
    print('Option 4: Exit')
    print()
    print('Enter your choice(1-4) : ',end='')
    choice=int(input())
    if choice==1:
        print()
        print('Enter the File Name: ',end='')
        fName = input()
        print('Enter the data you wish to enter into the File ' +fName+ ' ')
        data = input()
        with open(fName,'w') as newF:
            newF.write(data+'\n')
    if choice==2:
        print()
        print('Enter the File Name: ',end='')
        fName = input()
        with open(fName,'r') as findF:
            data = findF.read()
        print('Enter the term to be searched: ',end='')
        old=input()
        print('Enter the term to replace '+old+' with: ',end='')
        new=input()
        data=data.replace(old,new)
        with open(fName,'w') as repF:
            repF.write(data)
    if choice==3:
        print()
        print('Enter the File Name: ',end='')
        fName = input()
        with open(fName,'r') as readF:
            for line in readF:
                print(line.rstrip())
