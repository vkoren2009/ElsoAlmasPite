print("Hello and Welcome to My Library")
author=[]
title=[]

author.append(input("Who is the 1. author?"))
title.append(input("What is the 1. title?"))

x=0
while author[x] > "" :
  author.append(input("Who is the next author?"))
  title.append(input("What is the next title?"))
  x=x+1

print("Thanks for your input. Here are your submissions:")

x=0
while author[x] > "" :
  print(str(x+1) + ". " + author[x] + " : " + title[x])
  x=x+1
