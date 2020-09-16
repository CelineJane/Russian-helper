import random

# words
verbs = {'to speak' : 'говорить'}
colours = {'red' : 'красный', 'dark blue' : "синий" , 'white' : "белый", "black" : "чёрный" , "brown": "коричневый" , "pink" : "розовый", "green" : "зелёный" , "purple" : "фиолетовый", "yellow" : "жёлтый", "orange" : "оранжевый" , "light blue" : "голубой", "grey" : "серый"}
#numbers = {"1" "2" "3" "4" "5" "6" "7" "8" "9" "10"}
allWords = {'verbs': verbs, 'colours' : colours}


def main():
    
    print('привет!\n')
    language = input('Would you like to go from English to Russian or English to Russian?(e2r/r2e):')
    
    while not(language == 'e2r' or language == 'r2e') :
        language = input('Would you like to go from English to Russian or English to Russian?(e2r/r2e):')
        
    print('\nList of topics:')
    topics = list(allWords.keys())
    topics.append('random')
    for word in topics:
        print(word)
    
    topicChoice = input('\nWhat topic would you like to practice?')
    while topicChoice not in topics:
        topicChoice = input('What topic would you like to practice?')
    
    qNum = int(input('\nHow many questions? max 30:'))
    while not(qNum > 0 and qNum < 30):
        qNum = int(input('\nHow many questions? max 30:'))
        
    play(language, topicChoice, qNum)
    
   
def play(language, topicChoice, qNum):
    score = 0;
    
    if topicChoice == 'random':
        print('yep')
    else:
        words = allWords[topicChoice]
        wordPairs = list(words.items())
        wordKeys = list(words.keys())
        wordValues = list(words.values())
        
        
        if language == 'r2e': 
            
            for n in range(qNum):
                question = random.choice(wordValues)
                print(question)
                answer = input('Answer: ')
                
                answerPair = (answer, question)
                               
                if answerPair in wordPairs:
                    print('Correct!')
                    score = score + 1
                else:
                    indexAnswer = wordValues.index(question)
                    print('Incorrect :(\nThe correct answer is "' + wordKeys[indexAnswer] + '" ')
       
        elif language == 'e2r':
            
            for n in range(qNum):
                question = random.choice(wordKeys)
                print(question)
                answer = input('Answer: ')
                
                answerPair = (question, answer)
                               
                if answerPair in wordPairs:
                    print('Correct!')
                    score = score + 1
                else:
                    print('Incorrect :(\nThe correct answer is "' + words.get(question) + '" ')
    
    print('You scored: ' + str(score) + ' out of ' + str(qNum))
    playAgain = input('Play again?(y/n): ')
    
    if playAgain == 'y':
        main()
    else:
        exit()
        
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    

