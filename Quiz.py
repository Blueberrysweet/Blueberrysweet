import random 

game = False

#Questions and categories
categories = ['Video games', 'Science', 'Brands']
videogames_questions = [
    'What did nintendo make when they where first founded?',
    'What year did the first Xbox come out in?']
videogame_answers = ['a.Play cards\nb.Toys\nc.Hotels\nd.Video games',
                     'a.2008\nb.2011\nc.2001\nd.2013']
videogames_questions_correct = ['a', 'c']

science_questions = [
    'What 2 molecules is water made out of?',
    'Whats the element symbol for Gold on the periodic table?']
science_answers = ['a.Oxygen and helium\nb.Carbon and hydrogen\nc.Carbon and helium\nd.Oxygen and Hydrogen',
                   'a.Fe\nb.Au\nc.Ag\nd.Cu']
science_questions_correct = ['d', 'b']

brand_questions = [
    'Finish the slogan "America runs on ___"',
    'What year was apple founded?']
brand_answers = ['a.Coffee\nb.Starbucks\nc.Dunkin\nd.Donuts',
                 'a.1990\nb.2001\nc.1967\nd.1976']
brand_questions_correct = ['c', 'd']

#Lets the player choose their name and greets them.
def intro(name):
    print('\nIts a pleasure to meet you', name, '\n', '\nWould you like to play a game?' )


name = input('\nBefore anything may I have your name? ')

intro(name=name)


choice = input('\nYes or No\n>')
#This decides whether the game continues or not
if (choice == 'Yes') or (choice == 'yes'):
    print('\nAlright let\'s get straight to it!!')
    game = True
elif (choice == 'No') or (choice == 'no'):
    print('Aww that\'s too bad\nHope to see you next time', name)
    game = False
else:
    print('Sorry I don\'t understand')

#This is where the game starts if the player said yes
while game == True:
    
    print('\nPick a category', '\n', categories)
    category = int(input('->'))
    
    def videogame_questions(category = categories[0]):

        
        question1 = random.choice(videogames_questions)
        question2 = random.choice(videogames_questions)
        i = 0

        if question1 == videogames_questions[0]:
            print(question1)
            print('\n', videogame_answers[0])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == videogames_questions_correct[0]:
                print('Correct!')
            else:
                print('Incorrect')
        elif question1 == videogames_questions[1]:
            print(question1)
            print('\n', videogame_answers[1])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == videogames_questions_correct[1]:
                print('\nCorrect!')
            else:
                print('\nIncorrect')

        
        

        if question2 != question1:  
            if question2 == videogames_questions[0]:
                print(question2)
                print('\n', videogame_answers[0])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == videogames_questions_correct[0]:
                    print('Correct!')
                else:
                    print('Incorrect')
            elif question2 == videogames_questions[1]:
                print(question2)
                print('\n', videogame_answers[1])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == videogames_questions_correct[1]:
                    print('\nCorrect!')
                else:
                    print('\nIncorrect')
        elif question2 == question1:
            while i < 1:
                question2 = random.choice(videogames_questions)               
                if question2 != question1:
                    i = 7
                    if question2 == videogames_questions[0]:
                        print(question2)
                        print('\n', videogame_answers[0])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == videogames_questions_correct[0]:
                            print('Correct!')
                        else:
                            print('Incorrect')
                    elif question2 == videogames_questions[1]:
                        print(question2)
                        print('\n', videogame_answers[1])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == videogames_questions_correct[1]:
                            print('\nCorrect!')
                        else:
                            print('\nIncorrect')
                    
        
                     
        
      

    def nerd_questions(category = categories[1]):


        question1 = random.choice(science_questions)
        question2 = random.choice(science_questions)
        i = 0

        if question1 == science_questions[0]:
            print(question1)
            print('\n', science_answers[0])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == science_questions_correct[0]:
                print('Correct!')
            else:
                print('Incorrect')
        elif question1 == science_questions[1]:
            print(question1)
            print('\n', science_answers[1])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == science_questions_correct[1]:
                print('\nCorrect!')
            else:
                print('\nIncorrect')

        
        

        if question2 != question1:  
            if question2 == science_questions[0]:
                print(question2)
                print('\n', science_answers[0])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == science_questions_correct[0]:
                    print('Correct!')
                else:
                    print('Incorrect')
            elif question2 == science_questions[1]:
                print(question2)
                print('\n', science_answers[1])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == science_questions_correct[1]:
                    print('\nCorrect!')
                else:
                    print('\nIncorrect')
        elif question2 == question1:
            while i < 1:
                question2 = random.choice(science_questions)               
                if question2 != question1:
                    i = 7
                    if question2 == science_questions[0]:
                        print(question2)
                        print('\n', science_answers[0])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == science_questions_correct[0]:
                            print('Correct!')
                        else:
                            print('Incorrect')
                    elif question2 == science_questions[1]:
                        print(question2)
                        print('\n', science_answers[1])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == science_questions_correct[1]:
                            print('\nCorrect!')
                        else:
                            print('\nIncorrect')
    


    def brand_stuff(category = categories[2]):


        question1 = random.choice(brand_questions)
        question2 = random.choice(brand_questions)
        i = 0

        if question1 == brand_questions[0]:
            print(question1)
            print('\n', brand_answers[0])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == brand_questions_correct[0]:
                print('Correct!')
            else:
                print('Incorrect')
        elif question1 == brand_questions[1]:
            print(question1)
            print('\n', brand_answers[1])
            player_answer = input('Pick the letter of your answer->')
            if player_answer == brand_questions_correct[1]:
                print('\nCorrect!')
            else:
                print('\nIncorrect')

        
        

        if question2 != question1:  
            if question2 == brand_questions[0]:
                print(question2)
                print('\n', brand_answers[0])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == brand_questions_correct[0]:
                    print('Correct!')
                else:
                    print('Incorrect')
            elif question2 == brand_questions[1]:
                print(question2)
                print('\n', brand_answers[1])
                player_answer = input('Pick the letter of your answer->')
                if player_answer == brand_questions_correct[1]:
                    print('\nCorrect!')
                else:
                    print('\nIncorrect')
        elif question2 == question1:
            while i < 1:
                question2 = random.choice(brand_questions)               
                if question2 != question1:
                    i = 7
                    if question2 == brand_questions[0]:
                        print(question2)
                        print('\n', brand_answers[0])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == brand_questions_correct[0]:
                            print('Correct!')
                        else:
                            print('Incorrect')
                    elif question2 == brand_questions[1]:
                        print(question2)
                        print('\n', brand_answers[1])
                        player_answer = input('Pick the letter of your answer->')
                        if player_answer == brand_questions_correct[1]:
                            print('\nCorrect!')
                        else:
                            print('\nIncorrect')



    
    
                    
    if category == 0:
        videogame_questions(category = categories[0])
        exit = input('\ncontinue?\nYes or No\n->') 

        if (exit == 'Yes') or (exit == 'yes'):
            print('\nAlright!')
        elif (exit == 'No') or (exit == 'no'):
            print('\nThanks for playing\nSee ya next time', name)
            game = False
    elif category == 1:
        nerd_questions(category = categories[1])
        exit = input('\ncontinue?\nYes or No\n->') 

        if (exit == 'Yes') or (exit == 'yes'):
            print('\nAlright!')
        elif (exit == 'No') or (exit == 'no'):
            print('\nThanks for playing\nSee ya next time', name)
            game = False
    elif category == 2:
        brand_stuff(category = categories[2])
        exit = input('\ncontinue?\nYes or No\n->') 

        if (exit == 'Yes') or (exit == 'yes'):
            print('\nAlright!')
        elif (exit == 'No') or (exit == 'no'):
            print('\nThanks for playing\nSee ya next time', name)
            game = False
    
    
                

    


