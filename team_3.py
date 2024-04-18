#  ++++++++++++++++++++++++++++++++++++++++++++++++++++  #
#    Program Name:   Bibyte T3                           #
#    Date created:   18/04/2024                          #
#                                                        #
#    + Credits:                                          #
#           * Angela Amuzu                               #
#           * Caroline Aryeetey                          #
#           * Maria Arthur Gyamfi                        #
#           * Linda Maame Serwaa Adu Frimpong            #
#           * Victoria Adeku                             #
#           * Christopher Wiafe Debrah                   #
#                                                        #
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++  #       





# A program that accepts user inputs
#
# User chooses the unit (digital storage)  bit/byte,
#
# the program converts it to the other unit
#
# from bit to byte
# from byte to bit


# instruction:
    # create user prompt for player name
    # welcome user, and ask the user to choose the unit  \n
    # create another prompt to take user input
    
    
# for stopping the program in the while loop
import sys


# handles the calculation of changing bit to byte

def bit(bitTobyte):
    toByte = bitTobyte * 0.125
    return toByte


# handles the calculation of changing byte to bit
def byte(byteTobit):
    toBit = byteTobit * 8
    return toBit


# bit result handler
def bitProcess():
    print("\n Converting Bits to Bytes\n")
    bitNumber = int(input("Enter the number: "))
    convertedByte =  bit(bitNumber)
    print(f"The {bitNumber} bit(s) is {convertedByte} bytes\n")
    

# byte result handler
def byteProcess():
    print("\n Converting Byte to Bits\n")
    byteNumber = int(input("Enter the number: "))
    convertedBit =  byte(byteNumber)
    print(f"The {byteNumber} byte(s) is {convertedBit} bits\n")  
    
    
    
# handle program ending

def restartOrStopProgram():
    restartGame = input("Do you want you want to try again (y/n): ") 
    if restartGame.lower() == 'y':
        bitProcess()
    else:
        sys.exit(0)


# program starts:

print("========================\n")
print("Program name: Bibyte T3 \nIt is gonna be FUN!!\nNote:     B for Bit\n     Bt for Byte")
print("========================\n")

#input
#numberUpto100 = 1000
playerName = input("Enter your name: ")
if playerName == "" or playerName == " ":
    userReadiness = input(f"No-Name, are you ready (Y= yes and N = No): ") 

else:
    structurePlayerName = playerName.title()
    userReadiness = input(f" => {structurePlayerName}, are you ready (Y= yes and N = No): ")
    userReadyLowerCase = userReadiness.lower()
    

while True:       
    if userReadyLowerCase == "n" or userReadyLowerCase == "no":
        print("\nOh so early? \nPlease do not make T3 sad. Come back soon\n")
        break
    elif userReadyLowerCase == "y" or userReadyLowerCase == "yes":
        print("\nGood! Bring it on!\n")
        
        userUnitChecker = input("Type in 'b' for bit or bt for byte: ")
        userUnitCheckerLowerCase = userUnitChecker.lower()

        while True:       
            if userUnitCheckerLowerCase == "b" or userUnitCheckerLowerCase == "bit":
                bitProcess()
                restartOrStopProgram()

            elif userUnitCheckerLowerCase == "bt" or userUnitCheckerLowerCase == "byte":
                byteProcess()
                restartOrStopProgram()

            else:
                print("Wrong input please, try again")
                userUnitChecker = input("Type in 'b' for bit or bt for byte: ")
                userUnitCheckerLowerCase = userUnitChecker.lower()
                break
    else:
        print("Wrong input please, try again")
        userReadiness = input("Ready (Y= yes and N = No): ")
        userReadyLowerCase = userReadiness.lower()