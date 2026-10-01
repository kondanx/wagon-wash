import time

#Railcar length
railcarLength = int(25)

def calculateSpeed(seconds):
    washSpeed = (railcarLength/1000)/(seconds/3600)
    print(washSpeed)

calculateSpeed(60)