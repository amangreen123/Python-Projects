emotions = [ "anger","disgust","fear","happiness","sadness","surprise"]
emotions[0]= "anger"
emotions[1]= "disgust"
emotions[2]= "fear"
emotions[3]= "happiness"
emotions[4]= "sadness"
emotions[5]= "surprise"

def main():
    Primeloop()
    Ending()

def Primeloop():
    currEm=3
    action=0
    while True:
        action = getInteraction()
        if action == 9:
            break
        else:
            currEm = lookupEmotion(currEm,action)
            showEmotion(currEm)
    

# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten

def getInteraction():
    action = int(input("specify an action(0-reward,1-punish,2-threaten,3-jokes,9-quit"))
    if action ==0:
        print("I'm happy")
    elif action == 1:
        print("Dont hurt Me")
    elif action == 2:
        print("Bring it on")
    elif action == 3:
        print("HAHAHAHA")
    elif action == 9:
        print("Goodbye")
        #break
    return action
# TODO prompt user to choose an action
     
 # return a corresponding integer
# Based on a given emotion and action, determine the next emotional state
# Params:

    
    
# Returns: an emotion

def lookupEmotion(currEmotion, action):
    emotionMatrix =[[0,2,3,1,5,4], #0
    [1,3,0,1,1,2], #1
    [0,1,3,2,4,5],#2
    [0,2,1,3,4,5]] #3
    return emotionMatrix[action][currEmotion]
def showEmotion(currEm):
    emotions = [ "anger","disgust","fear","happiness","sadness","surprise"]
    print(emotions[currEm])
main()
