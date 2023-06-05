# #  #1
# def ranger():
#     for num in range(0,151):
#         print(num)


#  #2
# def multiplesOfFive():
#     fivers = []
#     for num in range(5,101):
#         if num%5==0:
#             fivers.append(num)
#     return fivers

# print(multiplesOfFive())

# #3

# def dojoWay():
#     placeHolder = []
#     for num in range(1,15):
#         if num%5 == 0:
#             placeHolder.append('Coding')
#         elif num%10 == 0:
#             placeHolder.append('Coding Dojo')
#         else:
#             placeHolder.append(num)
#     return placeHolder
# print(dojoWay())

#  #4
# def bigNum():
#     odds = 0
#     for num in range(500000):
#         if num%2 != 0:
#             odds = odds + num
#     return odds
# print(bigNum())



#5
# def countdown():
#     for num in range(2018, 0, -4):
#         if num%2==0:
#             print(num)
#     return holder

# print(countdown())

#6
def count():
    lowNum = 0
    highNum = 20
    mult = 2
    for num in range(lowNum, highNum, mult):
        print(num)

print(count())






