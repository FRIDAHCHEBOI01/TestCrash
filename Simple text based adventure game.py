my_dict = {
    'girl':2, 'boy':3,
}
print(my_dict['girl'])

def getsinput():
    #creates a list of words
    command = input(': ').split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >=2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)
verb_dict = {
    "say": say,
}
while True:
    getsinput()
