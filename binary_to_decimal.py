#Unsigned binary

message = "Write a binary number: "
binary = int(input(message))
original = binary
decimal = 0
counter = 0

if binary >= 0:
    if binary == 0:
        decimal = 0
    else:
        while binary != 1:
            rest = binary % 10
            decimal = decimal + rest*2**counter
            binary = binary // 10
            counter = counter + 1
        decimal = decimal + binary*2**counter
    print("The number {} in decimal is {}".format(original, decimal))
else:
    print("This version only accepts an unsigned binary number, negative numbers are invalid in this context")