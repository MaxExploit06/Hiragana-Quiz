import random
import getpass
questions = ['あ', 'い', 'う', 'え', 'お']
def main():
    n=random.randint(0,4)
    print("Q. What character is", questions[n])
    answer = input("Ans: ")
    if n == 0:
        ans = 'a'
    if n == 1:
        ans = 'i'
    if n == 2:
        ans = 'u'
    if n == 3:
        ans = 'e'
    if n == 4:
        ans = 'o'    
    if answer == ans:
        print("That is correct!")
        restart()
    else:
        print('That is wrong...\n' + f'Correct answer was "{ans}"')
        restart()
def restart():
    reply = getpass.getpass("Click Enter to continue. press F to exit\n").lower()
    if reply == 'f':
        exit()
    else:
        main()
main()
