# Date: 31/3/23 / Author: Stanley Denyer / Purpose: a basic terminal based note taking app

import os

notes = []

def main():
    print('📔 Welcome to my note taking app! 📔')
    while True:
        print(f'These are your notes:')
        for i in notes:
            print(f': {i}')
        option = input('Would you like to make a new note (m) or delete (d) a previous note (enter (esc) to leave)? ')
        if option == 'm':
            name = input('What is the name for your note? ')
            note_maker(name)
            text = input('What would you like your note to be? ')
            note_editor(name, text)
            notes.append(name)
            print('✅ Note saved ✅')
            continue
        elif option == 'd':
            name = input('What is the name for your note? ')
            if name in notes:
                note_deleter(name)
                notes.remove(name)
                print('❌ Note deleted ❌')
                continue
            else:
                print('Note not found!')
                continue
        elif option == 'esc':
            quit()
        else:
            print('Command unknown!')


def note_maker(name):
    file = open(f'{name}', 'w')

def note_editor(name, text):
    with open(f'{name}', 'a') as file:
        file.write(text)
    file.close()

def note_deleter(name):
    os.remove(f'/Users/stanley/Desktop/coding-basics/{name}')
    
main()


        

    
    