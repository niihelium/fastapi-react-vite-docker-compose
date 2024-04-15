import json
import requests as req
from requests import Response

base_url = "https://discordapp.com"


def send_message(token, channelid, message) -> Response:
    headers = {"authorization": token, "Content-Type": "application/json"}
    payload = {"content": message, "tts": False}
    res = req.post(
        base_url + f"/api/v9/channels/{channelid}/messages",
        headers=headers,
        json=payload,
    )
    return res


def get_message_id(res: Response) -> int:
    response_data = json.loads(res.content.decode("utf-8"))
    message_id = response_data["id"]
    return message_id


def deleteMessage(token, channel_id, message_id) -> Response:
    headers = {"authorization": token}
    res = req.delete(
        base_url + f"/api/v9/channels/{channel_id}/messages/{message_id}",
        headers=headers,
    )
    return res
