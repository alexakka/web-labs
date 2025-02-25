"""
    Реалізація патерну 'Знімок (Memento)' на прикладі текстового редактора
"""

class Memento:
    """Реалізацію класу Знімок (Memento)."""
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class TextEditor:
    """Реалізація простого текстового редактора."""
    def __init__(self):
        self._text = ""

    def write(self, text):
        self._text = text

    def save(self):
        return Memento(self._text)

    def restore(self, memento):
        self._text = memento.get_saved_state()

    def show_text(self):
        return self._text


class History:
    """Реалізація класу для керування збереженими станами."""
    def __init__(self):
        self._history = []

    def push(self, memento):
        self._history.append(memento)

    def pop(self):
        if self._history:
            return self._history.pop()
        return None



if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello, World!")
    history.push(editor.save())
    print("Current Text:", editor.show_text())

    # Modify Text
    editor.write("Hello, Python!")
    history.push(editor.save())
    print("Updated Text:", editor.show_text())

    # Undo 1
    editor.restore(history.pop())
    print("After Undo:", editor.show_text())

    # Undo 2
    editor.restore(history.pop())
    print("After Second Undo:", editor.show_text())
