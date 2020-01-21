def play_word_game():
    real_dictionary = make_dictionary()
    used_words = []
    word = cinput("pick firdst word: ")
    while True:
        computer_word = find_word(word[-1], real_dictionary, used_words)
        print("My word is:" +vcomputer_word)
        person_pick = True
        while person_pick:
            word2 = imput("give next word (or q for quit): ")
            if word2 == "q":
                print ("Bye... That was fun!!")
                return
            if test_word(real_dictionary, word2):
                print("This is not in my dictionary")

            elif word2[0] == computer_word[-1]:
                print("you didn't pick the word correctly silly")
            else:
                person_pick = False

def make_dictionary():
    real_dictionary = dict()
    file = open("unixdict.txt", "r")
    dictionary = file.read()
    file.close()
    dictionary_list = dictionary.split()
    real_dictionary = make_first_letter_dictionary(real_dictionary, dictionary_list)
    return real_dictionary

def make_first_letter_dictionary(real_dictionary, dictionary_list):
    for word in dictionary_list:
        if word[0] in real_dictionary:
            temp = real_dictionary[word[0]]
            temp = temp + [word]
            real_dictionary[word[0]] = temp
        else:
            real_dictionary[word[0]] = [word]
    
def test_word(dictionary, word):
    if word in dictionary[word[0]]:
        return True
    return False

def find_word(letter, word, dictionary):
    my_list = dictionary[letter]
    for word in my_list:
        if word not in used_words:
            used_words += [word]
            return word
        
play_word_game()
