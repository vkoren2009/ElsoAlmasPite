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

for x in author: print(x)
for x in title: print(x))
