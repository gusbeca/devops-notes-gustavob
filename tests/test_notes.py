import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from notes import NotesRepository


from notes import NotesRepository

def test_create_note():
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")
    repo = NotesRepository()
    repo.create("Comprar leche")
    assert "Comprar leche" in repo.list()

def test_delete_note():
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")
    repo = NotesRepository()
    repo.create("Tarea A")
    repo.delete("Tarea A")
    assert "Tarea A" not in repo.list()

def test_list_is_empty_initially():
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")
    repo = NotesRepository()
    assert repo.list() == []

def test_multiple_notes():
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")
    repo = NotesRepository()
    repo.create("A")
    repo.create("B")
    assert len(repo.list()) == 2

def test_cannot_delete_nonexistent_note():
    if os.path.exists("notas.txt"):
        os.remove("notas.txt")
    repo = NotesRepository()
    result = repo.delete("Inexistente")
    assert result is False
