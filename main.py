import argparse
import requests
import os
import time
import meshtastic
import meshtastic.serial_interface
from pubsub import pub


def make_on_receive(discord_webhook_url):
    def on_receive(packet, interface):
        if (
            packet["toId"] != "^all"
            or packet["decoded"]["portnum"] != "TEXT_MESSAGE_APP"
        ):
            return None

        from_id = packet["fromId"][1:]
        message = packet["decoded"]["payload"].decode("utf-8")

        data = {"username": from_id, "content": message}
        print(data)
        requests.post(discord_webhook_url, json=data)

    return on_receive


def main():
    parser = argparse.ArgumentParser(
        prog="Meshtastic2Discord",
        description="Small script that forwards Meshtastic primary channel messages to Discord by using a webhook.",
    )
    parser.add_argument("-p", "--port")
    args = parser.parse_args()

    interface = meshtastic.serial_interface.SerialInterface(devPath=args.port)

    discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    on_receive = make_on_receive(discord_webhook_url)
    pub.subscribe(on_receive, "meshtastic.receive")

    while True:
        time.sleep(1000)

    interface.close()


if __name__ == "__main__":
    main()
