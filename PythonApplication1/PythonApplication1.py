#Import TextBlob
from textblob import TextBlob

#A list of reviews
reviews= ['Every time you hit map or inventory button a popup ad comes up for the season pass its a fun game but ads on a game I spent money on is very annoying',
          'Out of all the Assassin\'s Creed games I have played, Odyssey has to be the first which I\'ve really fallen in love with. It\'s compelling story keeps you hooked for the next cut-scene, and killing becomes a chore. This, along with it\'s beautiful visuals and refined gameplay mechanics, have made for a truly, outstanding game.',
          'I like the game! I like the graphics, the story and the general design. BUT! EVERYONE HAS TO STOP BUYING THE MICROTRANSACTION CRAP THAT SEEMS TO BE THE UBISOFT TRADEMARK THESE DAYS! If you stop buying it, they will stop doing it!',
          'I really like the story of the game.Good optimization, great gameplay , great story. I recommend the game !',
          'It does not feel like an Assassin\'s Creed game at all but it is a very fun and worthy game to play and sink many hours into.']

#Used for the input
answer=0 

#This method looks at each review and determines if it is negative or positive.
def Analyze(positive):

    #For thhe current review
    for review in reviews:

        #Create a new TextBlob object
        text= TextBlob(review)
        #If the review is positive, print it
        if(positive==True and text.polarity>0 ):
            print(review)
            print(text.sentiment)
            print("")

        #If the review is negative print it
        elif(positive==False and text.polarity<0):
            print(review)
            print(text.sentiment)
            print("")

    #Set answer back to zero        
    answer= 0

#Main program
while (True):
    
    print("Welcome to Text Analyzer for game revews. What would you like to do?")
    print("1. View the positive reviews")
    print("2. View the negative reviews")

    #Set answer to the user input 
    answer=int(input(""))
    print("")

    #If we want to list all of the positive reviews
    if(answer==1):

        #Anaylyze and set positive to True
        Analyze(True)

    #If we want to list all of the negative reviews
    if(answer==2):
        
        #Anaylyze and set positive to False
        Analyze(False)
