def bubbleShort(number):
    for i in range(len(number)-1,0,-1):
        for j in range(i):
          if number[j]>number[j+1]:
             temp = number[j]
             number[j]=number[j+1]
             number[j+1]=temp



numbers=[64, 34, 25, 12, 22, 11, 90,6,656,62,265,66,6459,5565,656,949,656]
bubbleShort(numbers)
print(numbers)

#bubble short