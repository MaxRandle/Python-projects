import random
print("Welcome to the random insult generator!")
def entity_chooser():
    entity_to_insult = input("please enter an entity to insult:\n")
    insult_generator(entity_to_insult)
      
def insult_generator(entity_to_be_insulted):
    chosen_opener = get_term("insult_openers.txt")
    chosen_adjective = get_term("insult_adjectives.txt")
    chosen_noun = get_term("insult_nouns.txt")
    
    print(entity_to_be_insulted, chosen_opener, chosen_adjective, chosen_noun)
    """
    player_command = input("\nPress 'Enter' to generate the next insult\n"
          + "Press 'R' to reset the entity to be insulted\n"
          + "Press 'Q' to quit\n")
        """
    entity_chooser()
    """
    if player_command == "Q" or "q":
        return "Bye"
    else:
        insult_generator(entity_to_be_insulted)
    """

def get_term(filename):
    """
    this function takes a file name as a parameter
    then returns a random article from the file
    separated by ","
    """
    file = open(filename, "r")
    contents = file.read()
    file.close()
    term_list = contents.split("\n")
    term_index = random.randrange(0, len(term_list), 1)
    chosen_term = term_list[term_index]
    return chosen_term
    
entity_chooser()
import doctest
doctest.testmod()






















