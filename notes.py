import os

class NotesRepository:
    def __init__(self, filename="notas.txt"):
        self.filename = filename
        # Crea el archivo si no existe
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def create(self, note):
        with open(self.filename, "a") as f:
            f.write(note + "\n")

    def list(self):
        with open(self.filename, "r") as f:
            return [line.strip() for line in f.readlines()]

    def delete(self, note):
        notes = self.list()
        if note in notes:
            notes.remove(note)
            with open(self.filename, "w") as f:
                for n in notes:
                    f.write(n + "\n")
            return True
        return False
