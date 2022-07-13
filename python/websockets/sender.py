import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:80") as websocket:
        await websocket.send("Hello world")
        await websocket.recv()

asyncio.run(hello())

