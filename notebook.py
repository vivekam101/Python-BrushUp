import datetime

last_id=0


class Note:
    """ This class initiate notes with tags,memo"""

    def __init__(self,memo,tags=''):
       self.memo = memo
       self.tags = tags
       self.creation_date = datetime.date.today()
       global last_id
       last_id += 1
       self.id = last_id

    def match(self,string):
        """ Searching string match in notes """

        return str.lower(string) in str.lower(self.tags) or string in str.lower(self.memo)


class NoteBook:
    """ Class will do Note management such as create,search,modify"""

    def __init__(self):
        """initiate a notebook with empty notes"""

        self.notes = []

    def _find_note(self,id):
        """find note based on id"""

        for note in self.notes:
            if str(note.id) == str(id):
                return note
        return None

    def create_notes(self,memo,tags=''):
        """ creating notes"""

        self.notes.append(Note(memo,tags))

    def modify_notes_tags(self,id,memo='',tags=''):
        """track based on id and update memo"""

        note=self._find_note(id)
        if note:
            if memo:
                note.memo = memo
            if tags:
                note.tags = tags
        else:
            print('No matching id found')

    def check_id(self,id):
        """check id is available and return True"""
        if self._find_note(id):
            return True
        else:
            return False

    def append_notes_tags(self,id,memo='',tags=''):
        """track based on id and update memo"""

        note=self._find_note(id)
        if note:
            if memo:
                note.memo += memo
            if tags:
                note.tags += tags
        else:
            print('No matching id found')

    def search(self,filter):
        """ search based on filter"""

        for note in self.notes:
            if note.match(filter):
                self._display_notes_id(note.id)


    def _display_notes_id(self,id):
        """display notes by id"""

        for note in self.notes:
            if note.id == id:
                print("Id: {}\n date: {}\n Memo: {}\n Tags: {}\n\n".format(note.id,\
                                                             note.creation_date,\
                                                             note.memo,note.tags))

    def display(self):
        """display all the notes"""

        for note in self.notes:
            print("Id: {}\n date: {}\n Memo: {}\n Tags: {}\n\n".format(note.id,\
                                                             note.creation_date,\
                                                             note.memo,note.tags))