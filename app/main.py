class Note:
   High = "high"
   Medium = "Medium"
   Low = "low"

   def __init__(self, code, str, title: str, importance: str):
       self.code = code
       self.title = title
       self.text = text
       self.importance = importance
       self.creation_date = datetime.now()
       self.tags = []

       def add_tag(self, tag: str):
           if tag not in self.tags:
               self.tags.append(tag)

        def __str__(self):
            return f"date: {self.creation_date}\n{self.tittle}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        code= len(self.notes) + 1
        note = Note(str(code), title, text, importance)
        self.notes.append(note)
        return code

    def delete_note(self, code: int):
        self.notes = [note for note in self.notes if note.code != str(code)]

    def important_ notes(self):
    return [note for note in self.notes if note.code != str(code)]

    def important_notes(self):
        return [note for note in self.notes if tag in note.tags]

    def tag_with_most_notes(self):
        tag_count = {}
        for note tag in note.tags:
            tag_count[tag] = tag_count.get(tag, 0) + 1

        if not tag_count:
            return None
        return sorted(tag_count.items(), key=lamba x: (-x[1], x [0))[0[0]]







