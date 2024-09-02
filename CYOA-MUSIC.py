from time import sleep
import sys
import datetime
import random
import string
global inventory
global counter

global counterQ

global counterQE

global timer75
global timer15
global timer35
global counterQW

import winsound
def retry():
    RetryGame = input("Restart from the the very beginning?(Y/N).")
    if RetryGame == "Y":
        print("\n\n")
        storyline()   
    elif RetryGame == "N":
        sys.exit()
    else:
        print("Please enter a valid input.")
        retry()
    
def getElapsedTimeSeconds(startTime):
    
    currentTime = datetime.datetime.now()
    elapsedTime = datetime.datetime(1, 1, 1) + abs(startTime - currentTime)
    return elapsedTime.second
#75 & 15 SECOND TIMER#
def checktime75():
    getElapsedTimeSeconds(timer75)
    timeElapsed = getElapsedTimeSeconds(timer75)
    if timeElapsed > 75:   
         timedEnding()
         sys.exit()
def checktime15():
    getElapsedTimeSeconds(timer15)
    timeElapsed = getElapsedTimeSeconds(timer15)
    if timeElapsed > 15 :   
         timedEnding()
         sys.exit()
def checktime35():
    getElapsedTimeSeconds(timer35)
    timeElapsed = getElapsedTimeSeconds(timer35)
    if timeElapsed > 35 :   
         timedEnding()
         sys.exit()
####
def storyline():
    winsound.PlaySound("music/MainMusic.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
    print("This night marks the first day of the country-wide Christmas holiday, and you can't be any happier. You are robbing the largest jewelry bank in the world, with a single diamond valued at $500 000. So, you decide to infiltrate the back, since it has the least guards watching (You do not wear a mask):") 
    print("\nWhat choices will you input? Do you have what it takes to run away with the precious jewels?")
    input("Press 'ENTER' to begin!")
    guardWatching()

def guardWatching():
    global timer75
    choiceGuard = input("\nThere is one guard watching the back door. Which item will you use? Will you distract him? Or fight?\n'R' = Use your revolver.\n'D' = Use your 'distracting skills'.\n'S' = Shoot a silent sleep dart at him (you have two in your pocket). \nType one of the keys and Press 'ENTER'.") 
    if choiceGuard == "D":
        print("\nDid you really think shouting 'hey look, a butterfly!' would get you into the bank? You were arrested immediately for suspicion, and your items were all confiscated.")
        failGuardWatching()
    elif choiceGuard == "S":
        print("\nBefore moving on, you get the idea of stealing the guards uniform. You have all the time in the world, why not? ")
        stealUniform()
    elif choiceGuard == "R":
        print("\nThe officer dies, but you made a loud sound with your revolver, raising suspicion.  You're now in the museum, but the 75 second lock-down timer has begun! You better steal that diamond fast, or you'll get caught!")
        timer75 = datetime.datetime.now()
        laser()
    else:
        print ("Please enter a valid input.")
        guardWatching()

def laser():
    global timer15
    checktime75()
    choiceLaser = input("You've gotten into the diamond room, but it is protected by a deadly laser shield. What will you use to pass it?\n'D' = Use the zero years of training you got at dodging laser shields.\n'I' = Use your permeation device.\n'H' = Hack the security system(Will trigger the emergency 15-second lockdown)\n ")
    if choiceLaser == 'D':
        print("\nYou failed so bad, the guards began laughing at you. Did you think you were in a movie?")
        retryLaser()
    elif choiceLaser == 'I':
        print("\nThere it is! You're right in front of the diamond! All you have to do now is crack the safe its kept in.")
        crackLaser()
    elif choiceLaser == "H":
        print("\nGreat! You reached the diamond, and the safe is already unlocked since you took the time to hack the system. *15 SECOND EMERGENCY TIMER HAS COMMENCED*")
        timer15 = datetime.datetime.now()
        hack()
    else:
        print("Please choose a valid input.\n")
        
        laser()
def hack():
    checktime15()
    hackChoice = input("You're really low on time, so you must choose the best way to escape!\n'T' = Teleportation.\n'J' = Jetpack.\n'O' = Use your 'Olympic sprinting experience'\n")
    if hackChoice == "T":
        checktime15()
        coolEnd()
    elif hackChoice == "J":
        print("Your jetpack is low on fuel, and you only have enough weight to fly away safely without the diamond.")
        checktime15()
        jetpack()
    elif hackChoice == "O":
        checktime15()
        print("You really thought you could outrun a police car?")
        retryHack()
    else:
        print("Please enter a valid input.")
        hack()

def retryHack():
    checktime15()
    choiceRetryHack = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choiceRetryHack == "R":
        checktime15()
        print("\n\n")
        storyline()
    elif choiceRetryHack== "L":
        hack()     
    else:
        print("Please enter a valid input.")
        retryHack()
        
def jetpack():
    jetpackChoice = input("\nWill you guarantee your safety by dropping the diamond('D'), or keep the diamond and take your chances(1/5)('L')?")
    if jetpackChoice == "D":
        checktime15()
        safeEnding()
    elif jetpackChoice == "L":
        l = random.randint(1,5)
        if l == 1:
            checktime15()
            coolEnd()
        elif l >= 2:
            checktime15()
            death()
    else:
        print("Please enter a valid input.")
        jetpack()
def crackLaser():
    checktime75()
    crackInput = input("Choose one of the three choices to help you crack the code!\n'CODE' = Word to Number Decryption(Minigame).\n'MATH' = Multiplication Challenges(Minigame).\n'PEN' = Laser Pen\n")
    if crackInput == 'CODE':
        checktime75()
        codeNumbers()
    elif crackInput == 'MATH':
        checktime75()
        mathGame()
    elif crackInput == 'PEN':
        print("FAILURE. Did you really think a $5 laser pen could melt through an iron safe?")
        laserPen()
    else:
        print("Please enter a valid input.")
        crackLaser()

def laserPen():
    checktime75()
    choicelaserPen = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choicelaserPen == "R":
        print("\n\n")
        storyline()
    elif choicelaserPen== "L":
        crackLaser()     
    else:
        print("Please enter a valid input.")
        laserPen()

def stealUniform():
    global inventory
    stealUni = input("Steal his uniform?\n'Y' = Yes\n'N' = No\n")
    if stealUni == "Y":
        inventory = True
        print("\nAnyways, you used the most efficient way and got past the guard without anyone noticing!\n\nWith all the time in the world, you just need to take the diamond and escape.") 
        walkingGuards()
    elif stealUni == "N":
        inventory = False
        print("\nAnyways, you used the most efficient way and got past the guard without anyone noticing!\n\nWith all the time in the world, you just need to take the diamond and escape.") 
        walkingGuards()
    else:
        print("Please enter a valid input.")
        stealUniform()
def walkingGuards():
    global inventory
    choiceWalking = input("\nAt the diamond room entrance, you hear two guards walking to your left. What do you do?\n'B' = Be the boring guy and wait until they pass by.\n'C' = Change into the uniform you stole and engage a conversation with the guards\n'M' = Use the magic pebble you've been carrying around since second grade.\n")
    if choiceWalking == "B":
        boring()
    elif choiceWalking == "C" and inventory:
        winsound.PlaySound("music/SecretMusic.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        print("\nYour conservation with one of the two guards was so amazing, you stop caring about stealing the diamond, as winning his/her friendship is worth more to you than the most expensive diamond in the world (you have no friends). You decide to take a walk with them outside, but you remember that you put a guard to sleep there!")  
        conversation()
    elif choiceWalking == "C" and not inventory:
        print("\nHow do you expect to disguise as a security guard without any uniform? Choose a valid option.")
        walkingGuards()
    elif choiceWalking == "M":
        print("\nYour magic worked! The pebble miraculously knocks out the guard. Just kidding, you call this a diamond robbery? You were arrested immediately for attacking an officer, and your items were all confiscated.")
        pebble()
    else:
        print("Please enter a valid input.")
        walkingGuards()
        
def pebble():
    choicePebble = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choicePebble == "R":
        print("\n\n")
        storyline()
    elif choicePebble== "L":
        walkingGuards()     
    else:
        print("Please enter a valid input.")
        pebble()
    
def conversation():
    convoChoice = input("How do you handle the situation?\n'F' = Since you are the only guards in the whole museum, slip your extra sleep dart into one of the two guards' pockets (the one you don't really care about), and claim they put the guard to sleep to steal his clothes, all  in an elaborate attempt to rob the bank!\n'P' = Try to play it off by making it look like a stranger is currently robbing the bank, and volunteer to take the guard to the hospital.\n'R' = RUN!!!\n")
    if convoChoice == "R":
        WorstEnding()
    elif convoChoice == "F":
        IdealEnding()
    elif convoChoice == "P":
        charge()
    else:
        print("Please enter a valid option.")
        conversation()

def charge():
    chargeChoice = input("You immediately take charge, and order the two guards to turn the lock down system on and to check on the diamond. Without giving them time to respond, you drive off with the guard and take him to the hospital. What do you next?\n\n'H' = Take the guard to the hospital, and make sure he is checked up on.\n\n'D' = Drive to the middle of the desert to kill the guard, and get out of the country while you can!\n") 
    if chargeChoice == "H":
        HappyEnding()
    elif chargeChoice == "D":
        PoorEnding()
    else:
        print("Please enter a valid option.")
        charge()
def boring():
    boringChoice = input("The diamond is right in front of you, but its encased in a safe. How do you crack it open?\n\n'CODE' = Code Decryption (Numbers to Letters) - Minigame\n\n'MISTAKE' = Find the Mistake! - Minigame\n\n'I' = Use that safe cracking method you saw in the new 'Mission Impossible' movie!\n")
    if boringChoice == "I":
        print("You spend hours trying to figure out the code, and before you know it, its daytime! Guards realize you have been trying to crack the safe and arrest you.") 
        boringRetry()
    elif boringChoice == "CODE":
        codeWords()
    elif boringChoice == "MISTAKE":
        mistake()
###FIND THE MISTAKE! MINIGAME ###
def mistake():
    
    input("You have chosen the 'Find the Mistake!' minigame.\n\nIn this game, you will be given a sentence, and will be required to enter the mistake, all in lowercase answers.\n\nFor example, the mistake in 'Applle' would simply be 'l'(without the apostrophes), because there is an extra l. \n\nPress ENTER to begin.")

    correction = (input("\nWhat is the mistake in the the following list: ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n\n"))
    if correction == "the":
        successSafeGames()
    elif correction != "the":
        mistakeretry()

def mistakeretry():
    ask = input("Incorrect! Retry? Or admit defeat? Y = Retry, N = Defeat.\n\n")
    if ask == "Y":
        mistake()
    elif ask == "N":
        shamefulEnding()
    else:
        print("Please enter a valid input.")
        mistakeretry()
############
###CODE (NUMBERS TO LETTERS) MINIGAME###
def codeWords():
    print ("You have chosen the 'Code(Numbers to Letters) Minigame'. To crack open the case, you will be given a set of numbers to decrypt. Every letter in the alphabet is assigned a number from 1 to 26, in order. Do not put any spaces between the letters in your final code. Now go find that password!")
    input ("\nPress 'ENTER' to begin.")
    codeNumber = input("\nCODE TO DECRYPT: '16-1-19-19-23-15-18-4'\n")
    if codeNumber == "password":
        successSafeGames()
    else:
        print("Incorrect!")
        retryCodeWords()
   
def retryCodeWords():
    retryCode =input("Do you admit your defeat, or retry?\n'A' = Admit Defeat\n'R' = Retry\n")
    if retryCode == 'R':
        codeWords()
    elif retryCode =='A':
        shamefulEnding()
    else:
        print("Please enter a valid input.")
        retryCodeWords()
###############

def successSafeGames():
    print("Success! You have the diamond, now get out!")
    successCodeInput = input("You go back where you came from, but the guard is awake! What do you do?\n'R' = RUN!!!(Quicktime - Words Minigame)\n'D' = Just put him back to sleep with your second dart(Duh)\n") 
    if successCodeInput == "D":
        epicEnding()
    elif successCodeInput == "R":   
        question1A()
###QUICKTIME (WORDS) MINIGAME###
def question1A():
    global counterQW
    counterQW=0
    Q3 = ''.join(random.choice(string.ascii_letters + string.ascii_uppercase) for _ in range(4))
    print("You've chosen the 'Quicktime(Words) Minigame path'. You will be presented with three randomized sets of letters, with 3 seconds to type each exactly as they appear. After typing the set of letters, press 'ENTER' to move onto the next one. You have no time in between questions to pause.")

    input("Press 'Enter' when you're ready to go. ")

    timer1 = datetime.datetime.now()
    print(Q3)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 3 or answer != Q3:
        
        print("Incorrect, Next!")
        question2A()
    elif timeElapsed <= 3 and answer == Q3:

        counterQW = counterQW + 1
        question2A()

def question2A():
    global counterQW
    Q3 = ''.join(random.choice(string.ascii_letters + string.ascii_uppercase) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q3)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q3:
        print("Incorrect, Next!")
        question3A()
    elif timeElapsed <= 2 and answer == Q3:
        counterQW = counterQW + 1
        question3A()

def question3A():
    global counterQW
    Q3 = ''.join(random.choice(string.ascii_letters + string.ascii_uppercase) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q3)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q3:
        print("Incorrect, Next!")
        checkQW()
    elif timeElapsed <= 2 and answer == Q3:
        counterQW = counterQW + 1
        checkQW()

def checkQW():
    global counterQW
    print(f'\nYour final score is {counterQW}/3.')
    if counterQW >=2:
        successfulEnding()
    elif counterQW < 2:
        trip()
################
def trip():
    print ("\nYou tripped! The guard is starting to gain a lead on you, what do you do?.")
    choiceFall()
    
def choiceFall():
    choiceTrip = input("\n'P' = Use your magic pebble, that'll definitely save you!\n'S' = Turn on your emergency speed shoes to outrun him!\n'G' = Just turn around and shoot him(What's the worst that could happen?)\n")
    if choiceTrip == "P":
        legendaryEnding()
    elif choiceTrip == "S":
        criminalEnding()
    elif choiceTrip == "G":
        gunshot()
    else:
        print ("Please enter a valid input.")
        choiceFall()

def gunshot():
    print("\nGreat thinking, you really got him off your trail...now the WHOLE POLICE FORCE is after you.")
    resetGun()
def resetGun():
    resetGunChoice = input("\nRestart from the last point, or the very beginning?\n'R' = Restart from the beginning.\n'L' = Restart from the last point.")
    if resetGunChoice == "R":
        print("\n\n")
        storyline()
    elif resetGunChoice == "L":
        trip()

def boringRetry():
    choiceRetryBoring = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choiceRetryBoring == "R":
        print("\n\n")
        storyline()
    elif choiceRetryBoring== "L":
        boring()     
    else:
        print("Please enter a valid input.")
        boringRetry()
        
def retryLaser():
    
    choiceRetryLaser = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choiceRetryLaser == "R":
        print("\n\n")
        storyline()
    elif choiceRetryLaser== "L":
        laser()     
    else:
        print("Please enter a valid input.")
        retryLaser()

def failGuardWatching():
    
    choicefailGuard = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choicefailGuard == "R":
        print("\n\n")
        storyline()
    elif choicefailGuard == "L":
        guardWatching()     
    else:
        print("Please enter a valid input.")
        failGuardWatching()
###CODE (LETTERS TO NUMBERS) MINIGAME###
def codeNumbers():
    checktime75()
    print ("You have chosen the 'Code(Letters to Numbers) Minigame'. To crack open the case, you will be given a set of seven letters to decrypt. Every letter in the alphabet is assigned a number from 1 to 26, in order. Do not put any spaces between the numbers in your decrypted code. Don't take too long, or you might run out of time!")
    input ("Press 'ENTER' to begin.")
    checktime75()            
    codeNumber = input("CODE TO DECRYPT: 'aktvpqv'\n")
    if codeNumber == "1112022161722":
        checktime75()
        print ("Correct! You have the diamond, now get out!")
        diamondgetout()
    else:
        print ("Incorrect!There's no going back now, the 35 - second emergency alarm has kicked in and SWAT team members are running towards you as we speak. Get out!")
        SWAT()
###############
###MATH GAME###
def mathGame():
    checktime75()
    print("You have selected the 'Math Minigame'. The objective of this game is to correctly answer the multiplication question given to you. Don't forget, the 75 second timer is running!")
    input("Press 'ENTER' to continue.")
    q1()
def q1():
    checktime75()
    global counter
    counter = 0
    n = random.randint(0,10)
    y = random.randint(0,50)
    answer = input(f'What is {n} * {y}? ')
    if answer == (f'{n * y}'):
        print ("Correct!")
        counter = counter + 1
        q2()
    else:
        print ("Incorrect!")
        q2()

def q2():
    checktime75()
    global counter
    n = random.randint(0,10)
    y = random.randint(0,50)
    answer = input(f'What is {n} * {y}? ')
    if answer == (f'{n * y}'):
        print ("Correct!")
        counter = counter + 1
        q3()
    else:
        print ("Incorrect!")
        q3()

def q3():
    checktime75()
    global counter
    n = random.randint(0,10)
    y = random.randint(0,50)
    answer = input(f'What is {n} * {y}? ')
    if answer == (f'{n * y}'):
        print ("Correct!")
        counter = counter + 1
        check()
    else:
        print ("Incorrect!")
        check()

def check():
    checktime75()
    global counter
    print(f'\nYour final score is {counter}/3')
    if counter >=2:
        checktime75()
        print ("You have the diamond, now get out!")
        diamondgetout()
    elif counter == 0 or 1:
        checktime75()
        print ("There's no going back now, the 35 - second emergency alarm has kicked in and SWAT team members are running towards you as we speak. Get out!")
        SWAT()
################
###QUICKTIME MINIGAME (HARD)###

def question1B():
    checktime35()
    global counterQ
    counterQ=0
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    print("You've chosen the 'Quicktime Game path'. You will be presented with six sets of uppercase letters, with 1 second to type each exactly as they appear. After typing the uppercase letters, press 'ENTER' to move onto the next one. Your only way of freedom is to get all of them right, and there is no time in between questions to pause, so act quick!")

    input("Press 'Enter' when you're ready to go. ")
    checktime35()
    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        
        print("Incorrect, Next!")
        question2B()
    elif timeElapsed <= 1 and answer == Q:

        counterQ = counterQ + 1
        question2B()

def question2B():
    global counterQ
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        print("Incorrect, Next!")
        question3B()
    elif timeElapsed <= 1 and answer == Q:
        counterQ = counterQ + 1
        question3B()

def question3B():
    global counterQ
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        print("Incorrect, Next!")
        question4B()
    elif timeElapsed <= 1 and answer == Q:
        counterQ = counterQ + 1
        question4B()
def question4B():
    global counterQ
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        print("Incorrect, Next!")
        question5B()
    elif timeElapsed <= 1 and answer == Q:
        counterQ = counterQ + 1
        question5B()

def question5B():
    global counterQ
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        print("Incorrect, Next!")
        question6B()
    elif timeElapsed <= 1 and answer == Q:
        counterQ = counterQ + 1
        question6B()

def question6B():
    checktime35()
    global counterQ
    Q = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    timer1 = datetime.datetime.now()
    print(Q)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 1 or answer != Q:
        print("Incorrect, Done!")
        checkQ()
    elif timeElapsed <= 1 and answer == Q:
        print("Done!")
        counterQ = counterQ + 1
        checkQ()
def checkQ():
    global counterQ
    print(f'\nYour final score is {counterQ}/6')
    if counterQ == 6:
        checktime35()
        safeEnding()
    elif counterQ < 6:
        checktime35()
        badEnding()
#############################
###PATTERN MINIGAME (HARD)###       
def patternHard():
    checktime35()
    input ("You have chosen the 'Pattern Minigame'. When the game begins, you will be presented with a 5-term number pattern.\n\nThe objective of this game is to correctly guess the next two terms of the pattern in this format:(term6), (term7).\n\nFor example, the answer for the pattern (1, 2, 3, 4, 5, ?, ?) would simply be (6, 7), without the brackets included. Don't forget, the 75 second timer is still running!\n\nPress 'ENTER' to commence.")
    patternAnswer = input("\n1, 2, 6, 24, 120, ?, ?\n")
    if patternAnswer == ("720, 5040"):
        checktime35()
        print("\nCorrect! This pattern represents the list of factorials (n! =  n*n-1, n*n-2,...), from 1! to 7!.")
        safeEnding()
    else:
        checktime35()
        print("\nIncorrect!")
        badEnding()
###############################
###QUICKTIME MINIGAME (EASY)###
def question1():
    checktime75()
    global counterQE
    counterQE=0
    Q2 = ''.join(random.choice(string.digits) for _ in range(4))
    print("You've chosen the 'Quicktime Game path'. You will be presented with six different numbers, with 2 seconds to type each exactly as they appear. After typing the number, press 'ENTER' to move onto the next one. You have no time in between questions to pause, so act quick!")

    input("Press 'Enter' when you're ready to go. ")

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        
        print("Incorrect, Next!")
        question2()
    elif timeElapsed <= 2 and answer == Q2:

        counterQE = counterQE + 1
        question2()

def question2():
    global counterQE
    Q2 = ''.join(random.choice(string.digits) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        print("Incorrect, Next!")
        question3()
    elif timeElapsed <= 2 and answer == Q2:
        counterQE = counterQE + 1
        question3()

def question3():
    global counterQE
    Q2 = ''.join(random.choice(string.digits) for _ in range(4)) 

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        print("Incorrect, Next!")
        question4()
    elif timeElapsed <= 2 and answer == Q2:
        counterQE = counterQE + 1
        question4()
        
def question4():
    global counterQE
    Q2 = ''.join(random.choice(string.digits) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        print("Incorrect, Next!")
        question5()
    elif timeElapsed <= 2 and answer == Q2:
        counterQE = counterQE + 1
        question5()

def question5():
    global counterQE
    Q2 = ''.join(random.choice(string.digits) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        print("Incorrect, Next!")
        question6()
    elif timeElapsed <= 2 and answer == Q2:
        counterQE = counterQE + 1
        question6()

def question6():
    checktime75()
    global counterQE
    Q2 = ''.join(random.choice(string.digits) for _ in range(4))

    timer1 = datetime.datetime.now()
    print(Q2)
    answer = input("What is your answer? ")
    timeElapsed = getElapsedTimeSeconds(timer1)

    if timeElapsed > 2 or answer != Q2:
        print("Incorrect, Done!")
        checkQE()
    elif timeElapsed <= 2 and answer == Q2:
        print("Done!")
        counterQE = counterQE + 1
        checkQE()

def checkQE():
    global counterQE
    print(f'\nYour final score is {counterQE}/6.')
    if counterQE >=4:
        successfulEnding()
    elif counterQE == 3:
        cheapEnding()
    elif 0 <= counterQE <=2:
        escapeDrop()

###############################
def escapeDrop():
    checktime75()
    print("You weren't able to successfully escape, and are either forced to drop the diamond to guarantee your safety, or take a 1/3 chance of escaping.")
    choiceLuck()
    
#####PATTERN (EASY) MINIGAME####
 
def choiceLuck():
    checktime75()
    choiceDrop = input("\n'D' = Drop\n'L' = Take a 1/3 Chance.\n")
    if choiceDrop == "D":
        safeEnding()
    elif choiceDrop == "L":
        n = random.randint(1,3)
        if n == 1:
            successfulEnding()
        elif n == 2 or 3:
            badEnding()
    else:
        print ("Please enter a valid input.")
        choiceLuck()

def patternEasy():
    checktime75()
    input ("You have chosen the 'Pattern Minigame'. When the game begins, you will be presented with a 4-term number pattern.\n\nThe objective of this game is to correctly guess the next term of the pattern in this format:(term5).\n\nFor example, the answer for the pattern (1, 2, 3, 4, ?) would simply be (5), without the brackets included. Don't forget, the 75 second timer is still running!\n\nPress 'ENTER' to commence.")

    patternAnswer = input("\n5, 10, 20, 50, ?\n")
    if patternAnswer == ("100"):
        print("\nCorrect! This pattern represents the Canadian Dollar denominations, from least to greatest.")
        successfulEnding()
    else:
        print("\nIncorrect!")
        escapeDrop()
################################
def shrink():
    choiceShrink = input("Restart from the last point, or the very beginning?\n'R' = Beginning.\n'L' = Last Point.")
    if choiceShrink == "R":
        storyline()
    elif choiceShrink== "L":
        checktime75()
        diamondgetout()     
    else:
        print("Please enter a valid input.")
        shrink()
        
def SWAT():
    global timer35
    timer35 = datetime.datetime.now()
    SWATchoice = input("What will you do?\n'Q' = Quicktime Minigame(Hard)\n'P' = Pattern Minigame(Hard)\n")
    if SWATchoice == "Q":
        question1B()
    elif SWATchoice == "P":
        patternHard()
    else:
        print("Please enter a valid input.")
        SWAT()
        
def diamondgetout():
    checktime75()
    dOut = input("What will you do?\n'Q' = Quicktime Minigame(Easy)\n'P' = Pattern Minigame(Easy)\n'S' = Shrink Potion\n")
    if dOut == "Q":
        question1()
    elif dOut == "P":
        patternEasy()
    elif dOut == "S":
        print("Great, you're tiny now what? You get mistaken for an ant, and get stepped on by one of the guards!")
        shrink()
    else:
        print("Please enter a valid input.")
        diamondgetout()

#ENDINGS

def cheapEnding():
    winsound.PlaySound("music/Cheap_Ending.wav", winsound.SND_ASYNC)
    print("You barely make it out, but wait, where's the diamond!?")
    sleep(3)
    print("\nOne Day Passes by...")
    sleep(3)
    print("\nTwo Days Pass by...\n\nWoah, the diamond washed up ashore right beside your house!\n\nWhile you didn`t make the best choices, you were able to act fairly quickly in a dior situation, so you made it out with the diamond.The End.")
    retry()
def successfulEnding():
    winsound.PlaySound("music/Successful_Ending.wav", winsound.SND_ASYNC) 
    print("\nSuccessful Ending:\nYou steal the diamond and safely escape with $500 000! The End.")    
    retry()
def death():
    winsound.PlaySound("music/Death_Ending.wav", winsound.SND_ASYNC)
    print("\nFatal Ending: Your jetpack turns off mid-air due to the lack of fuel, and you fall to your sad, agonizing death.")
    retry()
def badEnding():
    winsound.PlaySound("music/Unlucky_Ending.wav", winsound.SND_ASYNC)
    print("\nBad Ending:\nYou are arrested , and have to live the rest of your life in fear from your cellmates. Accept your defeat.")
    retry()
def safeEnding():
    winsound.PlaySound("music/Safe_Ending.wav", winsound.SND_ASYNC)
    print("\nSafe Ending:\nYou couldn't steal anything, but you made it out uncaught and alive! The End.")           
    retry()
def coolEnd():
    winsound.PlaySound("music/Cool_Ending.wav", winsound.SND_ASYNC)
    print("\nCool Ending: Wow! You made it out by taking the most risks!\n Total Earnings: $500 000.")
    retry()
def WorstEnding():
    winsound.PlaySound("music/Worst_Ending.wav", winsound.SND_ASYNC)
    print("Worst, Sad Ending(Secret): The trained guards immediately take their tasers out and restrain you. Not only did you lose their friendship, but also your life, as you are arrested. You live the rest of your life in depression and anguish, awaiting its end every single day while you slowly rot in your prison cell.")
    retry()
def IdealEnding():
    winsound.PlaySound("music/Ideal_Ending.wav", winsound.SND_ASYNC)
    print("Ideal Ending(Secret): Both guards deny your claim at first, but when you check the other guards pocket and find the dart, everything begins to fall in your favor. The guard (as expected) denies all allegations, but you and the third guard have enough proof to arrest him. You are praised by your newly formed friend and the whole police department. Since they think you prevented one of the biggest heists to date from happening, you immediately get promoted to detective ($200k/year), and you become best friends with the guard you spoke with in the museum. You went from robbing the bank, to living your best life.")
    retry()
def HappyEnding():
    winsound.PlaySound("music/Happy_Ending.wav", winsound.SND_ASYNC)
    print("Happy Ending(Secret): After you return to the museum, you are recognized by the warden for your heroic acts, and he offers you a job as manager of police guards at the museum ($100k/year). You take the offer, and spend everyday of your life working with your newly formed friends. You begin becoming a better person too, since you finally get the chance to experience the feeling of friendship, something you always wished of having.")
    retry()
def PoorEnding():
    winsound.PlaySound("music/Poor_Ending.wav", winsound.SND_ASYNC)
    print("Cynical, Poor Ending: You quickly grab your belongings, and leave the country. You end off worse than when you started, living the rest of your life, homeless, and in regret. ")
    retry()
def shamefulEnding():
    winsound.PlaySound("music/Shameful_Ending.wav", winsound.SND_ASYNC)
    print("Shameful Ending: You gave up and turned yourself into the police, so much for an adventure!")
    retry()
def epicEnding():
    winsound.PlaySound("music/Epic_Ending.wav", winsound.SND_ASYNC)
    print("Epic Ending: You casually walk away, completely undetected, like a boss.")
    retry()
def criminalEnding():
    winsound.PlaySound("music/Epic_Ending.wav", winsound.SND_ASYNC)
    print("\n\nCriminal Ending:\nYou steal the diamond, and use your speed shoes to quickly grab your belongings and move out of the country. Since you have nothing to leave behind, its a success!\nTotal Earnings: $500 000.")
    retry()
def legendaryEnding():
    winsound.PlaySound("music/Legendary_Ending.wav", winsound.SND_ASYNC)
    print("\n\nLegendary Ending:\nTHE PEBBLE PREVAILED! The guard is knocked out, so he is unable to call back-up(you walk back to pick up your pebble), and you gain serious a reputation in the villain world for pulling off the biggest diamond heist in history. You go down as the infamous 'Mr. Pebble', and sell your pebble on the black market for $2 million dollars to a superstitious mob leader. This the LIFE!\nTotal Earnings: $2.5 Million.")
    retry()
def timedEnding():
    winsound.PlaySound("music/Timed_Ending.wav", winsound.SND_ASYNC)
    print("TIMES UP! The bank went into lock-down mode, and you were caught by the authorities.")
    retry()
#MAIN
storyline()



