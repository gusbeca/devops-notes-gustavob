class NotesRepository:
  def __init__(self):
      # Esta lista guardará las notas
      self._notes = []

  def create(self, note):
      # Agrega una nota nueva
      self._notes.append(note)

  def list(self):
      # Devuelve todas las notas
      return self._notes

  def delete(self, note):
      # Borra una nota si existe
      if note in self._notes:
          self._notes.remove(note)
          return True
      # Si la nota no existe, devuelve False
      return False
