from Attributes.train import wagonLength

def calculateSpeed(seconds):
    washSpeed = (wagonLength/1000)/(seconds/3600)
    print(washSpeed)