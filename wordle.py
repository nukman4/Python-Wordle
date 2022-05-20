import random
x=random.randint(0,12946)
lines = open("words.txt").read().splitlines()
word=list(lines[x])
green = "\033[1;32m"
yellow = "\033[1;33m"
reset = "\033[1;0m"
def choose():
  choice = input()
  print ('\033[F\033[K\033[F')
  if choice not in lines:
    print("not in word list")
    return 0
  else:
    choice = list(choice)
    return choice
def wordle():
  print("Terrible Python Wordle")
  for i in range(0,6):
    guess = i+1
    correct = 0
    choice = choose()
    while choice == 0:
      choice = choose()
    for i in range(len(word)):
      for i in range(len(choice)):
        if word[i] == choice[i]:
          choice[i] = green + choice[i] + reset
          correct += 1
        elif choice[i] in word:
          choice[i] = yellow + choice[i] + reset
    print(*choice, sep="",end=" ")
    print(guess)
    if correct == 5:
      print("you win!!!")
      return
wordle()
print("the word was ", *word,sep="")
