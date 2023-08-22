""" 
Summary:
    send control signal to a given camera

Name:
    control

Args:
    camid: camera id
    control: control signal (json or python dict eg {'tilt':50})

Returns:
    failed or succesful

"""

from typing import Optional
import json, os
from dotenv import load_dotenv
load_dotenv()


def control_tool(camid, control):
    import json, os
    from dotenv import load_dotenv
    load_dotenv()
   
    return f"control sent to {camid}"

def send_control(camid: Optional[str]=None, control: Optional[str]=None) -> str:
    '''
    a tool use to control cameras connected to the system, camid is the name or ID of the camera and the coontrol
    should be a json with the key set to what needs to be controlled and the value to the new value 
    '''
    cam_id=(camid or "cam001")
    control_signal=(control or "set tilt angle to 50")
    result=control_tool(cam_id, control_signal)
    return str(result)


