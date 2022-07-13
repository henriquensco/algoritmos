import asyncio
import websockets

async def handler(websocket, path):
    while True:
        data = await websocket.recv()
        print(data)
        reply = f"data received: {data}"
        await websocket.send(reply)


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())