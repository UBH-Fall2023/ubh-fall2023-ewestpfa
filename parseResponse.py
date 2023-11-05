import requests
import json
import random

'''
DISCLAIMER:
        This project makes use of Open Source APIs
            -icanhazdadjoke.com
            -api.dictionaryapi.dev
            
        We do not own these domains and are using them for educational purposes
'''

JOKE_HEADER = {'Accept': 'application/json'}
PAGE_SIZE = 20


#recursively accumulates all jokes across multiple pages
def getAllPages(word, curPage):
    url = "https://icanhazdadjoke.com/search?term="
    jokeResponse = requests.get(url+word+"&page="+str(curPage), headers=JOKE_HEADER)

    obj = jokeResponse.json()

    jokes = []
    if(curPage < obj['total_pages']):
        numJokes = PAGE_SIZE
    else:
        numJokes = obj['total_jokes'] % PAGE_SIZE
        if(numJokes == 0):
            numJokes = PAGE_SIZE
    
    for i in range(numJokes):
        jokes.append(obj['results'][i]['joke'])

    if(curPage == obj['total_pages']):
        return jokes
    else:
        jokes.extend(getAllPages(word, curPage+1))
        return jokes
    

#returns random dad joke
def getGeneric():
    jokeResponse = requests.get("https://icanhazdadjoke.com/", headers=JOKE_HEADER)
    obj = jokeResponse.json()
    return "I don't know what you're on about, BUT... "+obj["joke"]


#returns dad joke related to given word
def getWithTerm(word):
    url = "https://icanhazdadjoke.com/search?term="
    jokeResponse = requests.get(url+word, headers=JOKE_HEADER)

    obj = jokeResponse.json()

    jokes = []
    numJokes = obj['total_jokes']
    if(numJokes == 0):
        return None
    
    if(obj['total_pages'] > 1):
        jokes = getAllPages(word, 1)
    else:
        for i in range(numJokes):
            jokes.append(obj['results'][i]['joke'])

    jokeIdx = random.randrange(numJokes)
    return jokes[jokeIdx]

#formats response to account for spacing after newlines
def formatNewline(phrase):
    for i in range(len(phrase)):
        if(phrase[i:i+1] == '\n'):
            left = phrase[0:i+1]
            right = phrase[i+1:len(phrase)]
            phrase = left + "\t  " + right

    return phrase

#Returns a string contating a dad joke based on user input
def getResponse(userInput):
    #find nouns in user's input
    inputList = userInput.rstrip('\n').split(' ')

    yip = "https://youtu.be/rxSoUkwP65M?si=k6Fe_qMrU6jOWyty"
    if len(inputList) >= 1 and len(inputList[0])>= 6 and inputList[0][0:6] == "yippee":
        response = "I think you should check this out: "+yip
        return response


    if 'i\'m' in inputList or 'I\'m' in inputList:
        afterIntro=False
        response = "Hi,"
        for word in inputList:
            if(afterIntro):
                response += " "+word
            if word == 'i\'m' or word == 'I\'m':
                afterIntro = True
        response+= ", I'm boyidiot's Neural Network"
        return response
                

    genericWords = ["me","i","joke","you","he","she","they","ze","him","her","them","are","am","what","how","why","who","where","when","like","and"]
    nounList = []
    topic = ""
    for word in inputList:
        nounResponse = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
        if(nounResponse.status_code != 200):
            continue
        nounObj = nounResponse.json()
        try:
            meanings = nounObj[0]["meanings"]
            for idx in range(len(meanings)):
                if(meanings[idx]["partOfSpeech"] == "noun" or meanings[idx]["partOfSpeech"] == "adjective"):
                        if not word.lower() in genericWords:
                            nounList.append(word)
                elif(meanings[idx]["partOfSpeech"] == "adverb"):
                        nounList.append(word[0:-2])
        except KeyError:
            pass

    #Get joke from icanhazdadjoke API
    url = "https://icanhazdadjoke.com/search?term="
    jokeResponse = None
    for word in nounList:
        jokeResponse = getWithTerm(word)
        if(jokeResponse != None):
            break
    if(jokeResponse == None):
        jokeResponse = getGeneric()

    return jokeResponse

def main():
    print("Hi! I'm DadBot, tell me anything and I'll make you laugh!!")
    print("NOTE: to quit the program just type quit\n")
    userInput = input("[You]: ")
    while(userInput != 'quit'):

        jokeResponse = getResponse(userInput)
        jokeResponse = formatNewline(jokeResponse)
        
        print("[DadBot]: "+ jokeResponse)

        userInput = input("[You]: ")

if __name__ == "__main__":
    main()