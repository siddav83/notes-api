import handler

# List notes (should be empty)
print(handler.lambda_handler({"routeKey": "GET /notes"}, None))

# Create a note
print(handler.lambda_handler({"routeKey": "POST /notes", "body": "buy milk"}, None))

# List notes again (should show the note)
print(handler.lambda_handler({"routeKey": "GET /notes"}, None))