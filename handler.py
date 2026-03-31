import json
import service


def lambda_handler(event, context):
    route_key = event.get("routeKey", "")
    body = event.get("body", "")
    path_params = event.get("pathParameters") or {}

    if route_key == "GET /notes":
        return service.list_notes()

    elif route_key == "GET /notes/{id}":
        note_id = int(path_params.get("id"))
        return service.get_note(note_id)

    elif route_key == "POST /notes":
        return service.create_note(body)

    elif route_key == "DELETE /notes/{id}":
        note_id = int(path_params.get("id"))
        return service.delete_note(note_id)

    else:
        return {"statusCode": 404, "body": json.dumps({"error": "Route not found"})}
