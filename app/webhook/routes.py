from flask import Blueprint, json, request
from schemas import GitHubEvent
from extensions import events_collection
from datetime import datetime

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    try:
        event_data = request.json
        
        # Extract and map data from the GitHub webhook payload
        request_id = event_data.get('request_id', 'unknown')
        author = event_data.get('author', 'unknown')
        from_branch = event_data.get('from_branch', 'unknown')
        to_branch = event_data.get('to_branch', 'unknown')
        action = event_data.get('action', 'unknown')

        # Add timestamp
        timestamp = datetime.utcnow()

        # Create a dictionary to match the schema
        event_dict = {
            "request_id": request_id,
            "author": author,
            "from_branch": from_branch,
            "to_branch": to_branch,
            "timestamp": timestamp,
            "action": action
        }

         # Validate and create the event object
        event = GitHubEvent(**event_dict)

        # Insert the validated data into MongoDB
        events_collection.insert_one(event.dict())

        return jsonify({"message": "Event received and stored!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500
