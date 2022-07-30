fNum = int(input("Любе число:"))
    
def prime(fNum):
    if  fNum == 2:
        print("True = " +  str(fNum))
    if  fNum == 3:
        print("True = " +  str(fNum))
    if  fNum == 999:
        print("False = " +  str(fNum))
    else:
        if fNum < 1000:
            if fNum % 2 == 0:
                print("False = " + str(fNum))
            else:
                print("True = " + str(fNum))
        else:
            print("Error! The Number is > 1000")

print(prime(fNum))
