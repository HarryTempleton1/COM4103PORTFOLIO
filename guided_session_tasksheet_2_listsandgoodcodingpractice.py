import math
def main():
    #simple lists
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(weekdays[0])
    print(weekdays[1])
    print(weekdays[2])
    print(weekdays[3])
    print(weekdays[4])
    print(weekdays[5])
    print(weekdays[6])
    for i in range(len(weekdays)):
        print(weekdays[i])

    #all strings are sequences
    firstName = 'Harry Templeton'
    print(firstName[0])

    #strings as lists
    for i in range(len(weekdays)):
        dayString = weekdays[i]

        if(dayString[0] == "S" or dayString[0] == "T"):
            print(dayString)

    #strings as lists 2
    for i in range(len(firstName)):
        print(firstName[i])
    
    #sum of all list elements
    numbers = [1, 3, 4, 6, 7, 8, 19, 2, 4, 6, 7, 8, 13, 17, 11]
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    print("sum of numbers list is", sum)
    
    #list from user input
    userListSize = int(input("enter a list size"))
    userList = []
    for i in range(userListSize):
        userInput = input("input list value")
        userList.append(userInput)

    for i in range(userListSize - 1, -1, -1):
        print(userList[i])
    

    #plus minus 
    arr = [2, 6, 1,1,0,-1,-1]
    zero = 0
    pos = 0
    neg = 0
    for i in range(len(arr)):
        if(arr[i] == 0):
            zero += 1
        if(arr[i]>0):
            pos += 1
        if(arr[i]<0):
            neg += 1
    print(pos, neg, zero)

    pRatio = pos/len(arr)
    nRatio = neg/len(arr)
    zRatio = zero/len(arr)
    print(pRatio, nRatio, zRatio)




if __name__ == '__main__':
    main()