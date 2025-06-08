import asyncio
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

HELP_TEXT = """
NATS Help Auto-Responder
-----------------------
Send a message to the 'Help' subject to receive this help info.
This responder is running in Docker Swarm and demonstrates basic NATS request/reply.
"""

async def main():
    nc = NATS()
    await nc.connect(servers=["nats://nats:4222"])

    async def help_handler(msg):
        await nc.publish(msg.reply, HELP_TEXT.encode())

    await nc.subscribe("Help", cb=help_handler)
    print("[Responder] Listening on 'Help' subject...")
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
