inputString = input("Enter string: ")

inputString = inputString.split(",")
temp=""
for inpStr in inputString:
    inpStr = inpStr.split(":")
    letters = inpStr[0]
    number = inpStr[1]
    num = 0
    for i in number:
        num+=int(i)**2
    temp = ""
    if num%2==0:
        temp = letters[len(letters)-1:len(letters)]
        temp = temp+letters[0:len(letters)-1]
    else:
        temp = letters[0:2]
        temp = letters[2:len(letters)]+temp
    print(temp)