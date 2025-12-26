def comparison(word,comparing_word):
    if word == comparing_word: 
        print('All right, bananas.')
    elif word < comparing_word: 
        print('Your word,' + word + ', comes before banana.') 
    elif word > comparing_word: 
        print('Your word,' + word + ', comes after banana.') 
    else: 
        print('All right, bananas.')

comparison('Pineapple','banana')