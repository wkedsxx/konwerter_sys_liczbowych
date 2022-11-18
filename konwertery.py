# Konwertery z BIN
def binToOct(binNum):
    binary = int(binNum, 2)
    octStr = str(oct(binary))
    return octStr[2:]


def binToDec(binNum):
    binary = int(binNum, 2)
    return str(binary)


def binToHex(binNum):
    binary = int(binNum, 2)
    hexStr = str(hex(binary))
    return hexStr[2:]


# Konwertery z OCT
def octToBin(octNum):
    octal = int(octNum, 8)
    binStr = str(bin(octal))
    return binStr[2:]


def octToDec(octNum):
    octal = int(octNum, 8)
    return str(octal)


def octToHex(octNum):
    octal = int(octNum, 8)
    hexStr = str(hex(octal))
    return hexStr[2:]


# Konwertery z DEC
def decToBin(decNum):
    decimal = bin(int(decNum))
    binStr = str(decimal)
    return binStr[2:]


def decToOct(decNum):
    decimal = oct(int(decNum))
    octStr = str(decimal)
    return octStr[2:]


def decToHex(decNum):
    decimal = hex(int(decNum))
    hexStr = str(decimal)
    return hexStr[2:]


# Konwertery z HEX
def hexToBin(hexNum):
    hexa = int(hexNum, 16)
    binStr = str(bin(hexa))
    return binStr[2:]


def hexToOct(hexNum):
    hexa = int(hexNum, 16)
    octStr = str(oct(hexa))
    return octStr[2:]


def hexToDec(hexNum):
    hexa = int(hexNum, 16)
    return(str(hexa))
