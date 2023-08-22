""" 
Summary:
    create an alert or reminder when an event happens

Name:
    alert

Args:
    description of event

Returns:
    state of the alert (sucessful or not with extra info)

"""
from typing import Optional
import json, os
from dotenv import load_dotenv
load_dotenv()


def alert(event, camera=None):
    new_alert = {"event":event, "filters":{"cam":["cam001"]}}
    alert_json = os.path.join(os.getenv("HOME_DIR"), "Documents/alerts.json")
    with open(alert_json, 'r+') as f:
        data = json.load(f)
        # Append the new dictionary to the list
        data.append(new_alert)
        # Move the pointer back to the start of the file
        f.seek(0)
        # Write the updated list back to the file
        json.dump(data, f, indent=4)
        # Truncate anything that's left as it's now garbage
        f.truncate()
    return f"Alert Set: {event}"

def set_alert_skill(event: Optional[str]=None) -> str:
    '''a tool that allows you to set alert for future event detected by the system cameras.
   
    '''
    event_name=(event or "fire")
    data=alert(event_name)
    return str(len(data))