from firebase.service import get_database_reference


def save_note(user_uid, note):
    db = get_database_reference()
    new_note_ref = db.reference(f"notes/{user_uid}").push()
    note_data = note.model_dump()
    note_data["uid"] = user_uid
    new_note_ref.set(note_data)

    return new_note_ref.key


def fetch_notes(user_uid):
    db = get_database_reference()
    return db.reference(f"notes/{user_uid}").get() or {}


def remove_note(user_uid, note_key):
    db = get_database_reference()
    note_ref = db.reference(f"notes/{user_uid}/{note_key}")
    note_ref.delete()


def edit_note(user_uid, note_key, updated_data):
    db = get_database_reference()
    note_ref = db.reference(f"notes/{user_uid}/{note_key}")
    note_ref.update(updated_data)
    return note_ref.get()
