def open_ws_server(port, message=None):
    import asyncio
    import websockets
    from datetime import datetime
    from random import random

    async def sendMsg(websocket, path):
        while True:
            try:
                if message == None:
                    message = "message: {}".format(random())
                await websocket.send(message)
                print('send message:', message)
            except Exception:
                pass
            finally:
                await asyncio.sleep(1)

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(sendMsg, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
