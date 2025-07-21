import requests
from plyer import notification

# Function to fetch live cricket scores using CricAPI
def fetch_live_cricket_scores(api_key):
    live_matches = []
    offset = 0
    max_offset = 1

    while offset < max_offset:
        url = f'https://api.cricapi.com/v1/currentMatches?apikey={api_key}&offset={offset}'
        response = requests.get(url)
        
        if response.status_code != 200:
            return [f"Failed to fetch cricket scores. Status code: {response.status_code}"]

        data = response.json()

        if data.get("status") != "success":
            return ["FAILED TO GET A SUCCESS RESULT"]

        max_offset = data["info"]["totalRows"]
        offset += len(data["data"])
        live_matches.extend(data["data"])

    return live_matches

# Function to get and notify live cricket scores
def get_cricket_scores():
    api_key = '***REMOVED***'  # Replace with your CricAPI key
    cricket_scores = fetch_live_cricket_scores(api_key)

    if cricket_scores:
        for match in cricket_scores:
            match_desc = match.get("name", "Unknown Match")
            status = match.get("status", "No Status Available")
            winner_team = match.get("winner_team", "")
            
            if winner_team and "won by" in status:
                notification_message = f"{winner_team} {status.split(winner_team)[-1].strip()}"
            else:
                notification_message = f"{match_desc}\nStatus: {status}"
            
            notification.notify(
                title="Live Cricket Score",
                message=notification_message,
                timeout=10
            )
    else:
        notification.notify(
            title="Live Cricket Score",
            message="No live cricket matches found.",
            timeout=10
        )


