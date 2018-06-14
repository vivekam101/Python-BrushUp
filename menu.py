import sys
from notebook import Note, NoteBook

class Menu:
    """interface to the users"""

    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {1:self.add_notes,
                   2:self.modify_notes_tags,
                   3:self.append_notes_tags,
                   4:self.search_notes,
                   5:self.display_notes,
                   6:self.quit}


    def show_menu(self):
        print(""" \n                       Menu\n-----------------------------------------------------------\n\n                     1. Add notes\n
                     2. Modify notes or tags\n
                     3. Append notes or tags\n
                     4. Search notes\n
                     5. Display notes\n
                     6. Quit\n""")

    def run(self):
        while True:
            self.show_menu()
            choice = int(input('Please enter your choice: '))
            if choice > 5 or choice < 0:
                print('Incorrect Choice')
                break
            else:
                self.choices[choice]()

    def add_notes(self):
        memo = input('Please enter your memo: ')
        tags = input('Please enter your tags: ')
        self.notebook.create_notes(memo,tags)
        print('Note added')

    def modify_notes_tags(self):
        id = input("Please let me know the Note id: ")
        if self.notebook.check_id(id):
            memo = input("Please let me know the updated Note memo: ")
            tags = input("Please let me know the updated Note tags: ")
            if memo:
                self.notebook.modify_notes_tags(id,memo)
            if tags:
                self.notebook.modify_notes_tags(id,tags)
        else:
            print('Id not available')

    def append_notes_tags(self):
        id = input("Please let me know the Note id: ")
        if self.notebook.check_id(id):
            memo = input("Please let me know the memo to be appended: ")
            tags = input("Please let me know the tags to be appended: ")
            if memo:
                self.notebook.append_notes_tags(id,memo)
            if tags:
                self.notebook.append_notes_tags(id,tags)
        else:
            print('Id not available')

    def search_notes(self):
        filter = input("Please enter the filter string: ")
        self.notebook.search(filter)

    def display_notes(self):
        self.notebook.display()

    def quit(self):
        exit()

if __name__ == '__main__':
    Menu().run()