#notepad
import os
def filedisp(name):
    try:
        f = open(name, 'r+')
        text = f.readlines()
        f.close()
        text = ''.join(text)
        print('Here are the contents ')
        print(text)
    except IOError:
        print('Cannot open file.....try again')


def printmenu():
    choice = '0'
    while choice not in '123':
        print('Enter your choice (It should be 1 , 2 or 3)\n'
              '1.Write into a new file\n'
              '2.Find and replace a word in a prewritten text\n'
              '3.view the contents of your file')
        choice = input()
    choice = int(choice)
    return choice

cont = 'y'
while cont == 'y' or cont == 'Y':
    choice = printmenu()
    if choice == 1:
        name = input('What do you want to name your file ? \n'
                   'Type in existing name if you want to append data\n')
        with open(name, 'a') as f:
            text = input('Enter the data you want to write to the file...'
                           '"enter" to terminate ')
            f.write(text)

    elif choice == 2:
        name = input('Enter the filename you want to find and replace ')
        filedisp(name)
        findword = input('Enter the word/substring you want to find ')
        replaceword = input('Enter the word/substring you want to replace ')
        f2 = open('tmp.txt', 'w')
        try:
            with open(name, 'r') as f:
                text = f.readlines()
                text = ''.join(text)
                text = text.replace(findword, replaceword)
                f2.write(text)
                f2.close()
            os.remove(name)
            os.rename('tmp.txt',name)
        except IOError:
            print('Cannot open file.....try again')
    elif choice == 3:
        name = input('Enter the name of the file you want to view ')
        filedisp(name)
    print('continue?(y/n) ')
    cont = input()


