possibleSolutions = []
operations = ['+', '-', '*', '/']
numberList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
targetNum = 2019


def baseConvert(startBase, convertBase, value):
    charaterValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                      'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    value = str(value)
    if startBase != 10:
        base10Value = 0
        for positionInValue in range(len(value)):
            currentDigit = value[-(positionInValue+1)]
            digitValue = charaterValues.index(currentDigit)
            base10Value += digitValue * startBase ** positionInValue
    else:
        base10Value = value

    convertedValue = ''
    if convertBase != 10:
        while base10Value > 0:
            carry = base10Value%convertBase
            base10Value = (base10Value-carry)/convertBase
            convertedValue = str(charaterValues.index(str(int(carry)))) + convertedValue
        return convertedValue
    else:
        return base10Value


def numToOperations(number):
    number = str(number)
    while len(number) < len(numberList) - 1:
        number = '0' + number
    operationList = []
    for digit in number:
        operationList.append(operations[int(digit)])
    return operationList


def operationsToNum(operationL):
    number = ''
    for operation in operationL:
        number += str(operations.index(operation))
    return number


def calculateWithOrder(numbersEnter, operationListEnter):
    operationList = []
    operationList += operationListEnter
    numbers = []
    numbers += numbersEnter

    posOfOp = 0
    while posOfOp < len(operationList):
        operation = operationList[posOfOp]
        if operation == '*':
            numbers[posOfOp] *= numbers[posOfOp + 1]
            del numbers[posOfOp + 1]
            del operationList[posOfOp]
        elif operation == '/':
            numbers[posOfOp] /= numbers[posOfOp + 1]
            del numbers[posOfOp + 1]
            del operationList[posOfOp]
        else:
            posOfOp += 1

    posOfOp = 0
    while posOfOp < len(operationList):
        operation = operationList[posOfOp]
        if operation == '+':
            numbers[posOfOp] += numbers[posOfOp + 1]
            del numbers[posOfOp + 1]
            del operationList[posOfOp]
        elif operation == '-':
            numbers[posOfOp] -= numbers[posOfOp + 1]
            del numbers[posOfOp + 1]
            del operationList[posOfOp]
        else:
            posOfOp += 1

    return numbers[0]


for x in range(len(operations) ** (len(numberList)-1)):
    operationsToDo = numToOperations(baseConvert(10, len(operations), x))
    value = int(calculateWithOrder(numberList, operationsToDo))
    if value == targetNum:
        possibleSolutions.append(operationsToDo)


print(possibleSolutions)
