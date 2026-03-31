import json
import model.notes as model


def list_notes():
    notes = model.get_all_notes()
    return {"statusCode": 200, "body": json.dumps(notes)}


def get_note(note_id):
    note = model.get_note(note_id)
    if note is None:
        return {"statusCode": 404, "body": json.dumps({"error": "Note not found"})}
    return {"statusCode": 200, "body": json.dumps(note)}


def create_note(body):
    # body arrives as a raw JSON string from API Gateway — parse it first
    try:
        data = json.loads(body) if isinstance(body, str) else body
        content = data["content"]
    except (json.JSONDecodeError, KeyError):
        return {"statusCode": 400, "body": json.dumps({"error": "Missing 'content' field"})}

    note = model.create_note(content)
    return {"statusCode": 201, "body": json.dumps(note)}


def delete_note(note_id):
    deleted = model.delete_note(note_id)
    if not deleted:
        return {"statusCode": 404, "body": json.dumps({"error": "Note not found"})}
    return {"statusCode": 200, "body": json.dumps({"message": f"Note {note_id} deleted"})}
