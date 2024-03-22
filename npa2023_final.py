#######################################################################################
# Yourname: pornpinit nongna
# Your student ID: 64070195
# Your GitHub Repo: https://github.com/mackxss/NPA2023-Final-pronpinit

#######################################################################################
# 1. Import libraries for API requests, JSON formatting, time, and (restconf_final or netconf_final).

import json
import time
import requests
from netconf_final import create, delete, enable, disable
#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.

accessToken = "MzhiN2Y5ZjQtMTYwNS00NDNkLTliZjUtZDY2OGVhMmZmMDhlY2FlZTE2MmUtN2Jk_P0A1_f5dcacf5-03ac-4089-bc01-c8b97092db9a"

#######################################################################################
# 3. Prepare parameters get the latest message for messages API.

# Defines a variable that will hold the roomId
roomIdToGetMessages = (
    "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMTAzZDk3OTAtZTgyNS0xMWVlLWI3OTQtY2QyNjA0MGM5YzYz"
)

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    getParameters = {"roomId": roomIdToGetMessages, "max": 1}

    # the Webex Teams HTTP header, including the Authoriztion
    getHTTPHeader = {'Authorization': 'Bearer {}'.format(accessToken)}

# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get(
        "https://api.ciscospark.com/v1/messages",
        params={"max": 1},
        headers={"Authorization": "MzhiN2Y5ZjQtMTYwNS00NDNkLTliZjUtZDY2OGVhMmZmMDhlY2FlZTE2MmUtN2Jk_P0A1_f5dcacf5-03ac-4089-bc01-c8b97092db9a"},
    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception(
            "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
        )

    # get the JSON formatted returned data
    json_data = r.json()

    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")

    # store the array of messages
    messages = json_data["items"]
    
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)

    # check if the text of the message starts with the magic character "/" followed by your studentID and a space and followed by a command name
    #  e.g.  "/66070123 create"
    if message.find("/64070195 create") == 0:

        # extract the command
        command = message.split(" ")[2]
        print(command)

# 5. Complete the logic for each command

        if command == "create":
            create()
        elif command == "delete":
            delete()
        elif command == "enable":
            enable()
        elif command == "disable":
            disable()
        # elif command == "status":
        #     status()
        else:
            responseMessage = "Error: No command or unknown command"
        
# 6. Complete the code to post the message to the Webex Teams room.
        
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        postHTTPHeaders = HTTPHeaders = {"Authorization": "MzhiN2Y5ZjQtMTYwNS00NDNkLTliZjUtZDY2OGVhMmZmMDhlY2FlZTE2MmUtN2Jk_P0A1_f5dcacf5-03ac-4089-bc01-c8b97092db9a", "Content-Type": "application/json"}

        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        postData = {"roomId": "0e46c900779f103cbb9dc616b2e9c7a1", "text": responseMessage}

        # Post the call to the Webex Teams message API.
        r = requests.post(
            "https://api.ciscospark.com/v1/messages",
            data=json.dumps(postData),
            headers= postHTTPHeaders,
        )
        if not r.status_code == 200:
            raise Exception(
                "Incorrect reply from Webex Teams API. Status code: {}".format(r.status_code)
            )
