f = open("inputSmall.txt")
data = []

RED = '\033[91m'   # Jasnoczerwony
END = '\033[0m'    # Resetowanie koloru

for i in f:
    data.append(i.rstrip().split())

startPosition = 50
zeroPointer = 0

currentPosition = startPosition
rotates = 0

for move in data:
    if move[0][0] == 'R':
        addition = int(move[0][1:])%100
        
        if int(move[0][1:]) > 99:
            rotates += int(move[0][1])
        currentPosition += addition
        if currentPosition > 99:
            currentPosition = currentPosition - 100
            rotates+=1
        print("Current addition = ", addition, '\n' )
        print("Current pos: ", currentPosition, '\n')
    else:
        subtraction = int(move[0][1:])%100

        currentPosition -= subtraction
        if currentPosition < 0:
            currentPosition = currentPosition + 100
            rotates+=1
        print("Current subtraction = ", subtraction, '\n' )
        print("Current pos: ", currentPosition, '\n')
    
    if currentPosition == 0:
        zeroPointer+=1
        print(f"{RED} ZERO FOUND!!! {END}")


print("Zero occured ", zeroPointer , " times.")
print("Zero with rotates through zero: ", zeroPointer+rotates)



