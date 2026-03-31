from model.notes import init_db, get_all_notes, create_note

init_db()

# Create a note
create_note("buy milk")

# Get all notes
notes = get_all_notes()
for note in notes:
    print(note.id, note.content, note.created_at)