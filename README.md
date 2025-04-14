# Installation

## Node preparation

This is just a suggestion on how to prepare the node dedicated to this usage.

```bash
meshtastic --port /dev/ttyUSB0 \
           --set lora.region EU_868 \
           --set-owner-short '🤖' \
           --set-owner "I'm the Discord bot !" \
           --setlat 48.58392 \
           --setlon 7.74553 \
           --set bluetooth.enabled false \
           --set device.led_heartbeat_disabled true
```

## Discord

1. Create a channel
2. Create a webhook on the created channel

## Launch the script

```bash
export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/...'
uv run main.py --port /dev/ttyUSB0
```
