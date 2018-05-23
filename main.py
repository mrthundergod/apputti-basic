import time
import random
from sing import *
from joke import *


def nameGet():
  check = True
  c = 0
  while check == True:
    if c==0:
      inVal = input("... \n")
    if inVal.lower() == 'hello':
      inVal = input("Hello! What's your name? "+ '\n')
      c = 1
    elif inVal.lower() == 'end':
      endGame()
    else:
      if c != 1:
        nameChk = input("Is that your name?"+ '\n')
        if nameChk.lower() == 'yes':
          print("Hello, "+inVal+". My name is Appu v0.0.1"+ '\n')
          time.sleep(3)
          check = False
        elif nameChk.lower() == 'no':
          inVal = 'hello'
      elif c==1:
        print("Hello, "+inVal+". My name is Appu v0.0.1")
        time.sleep(3)
        check = False

  return inVal

def welcome(name):
  print("Welcome to the program, " + name + ". If you need me to do something, let me know! To end the program at anytime, type 'stop'."+ '\n')
  time.sleep(2)
  check2 = input('Start/Stop? \n')
  if check2.lower() == 'start':
    print("So, I can sing(or type a song, lol), tell you some jokes, or tell you the news. Just enter song, joke or news to continue!!! ^_^ \n")
    time.sleep(2)

    doStuff()
    body()

  elif check2.lower() == 'stop':
    endGame()
  else:
    print(" Did'nt understand :(")


def doStuff():
  doWhat = input("What do you want me to do?"+ '\n'+ '\n')
  if doWhat == 'sing':
    song()
  elif doWhat == 'joke':
    joke()
  elif doWhat == 'news':
    news()
  elif doWhat == 'end':
    endGame()
  else:
    print("Oops! I didn't get that :("+ '\n')
  body()

def body():
  bodyChk = input("Yay! So hope that was fun! Wanna continue?\n"+ '\n')
  if bodyChk =='yes':
    doStuff()
  elif bodyChk == 'no':
    endGame()

def endGame():
  print("Oh.... Okay...")
  time.sleep(1)
  print("I guess its good bye! :( ")
  time.sleep(1)
  print("Come again sometime ^_^")
  time.sleep(1)
  exit()

def song():
  poem()
  print('\n')
  time.sleep(1)

def joke():
  funny()
  time.sleep(1)

def news():
  print('NEWS')

if __name__ == '__main__':
  end = False
  name = nameGet()
  while True:
    welcome(name)
    



  


