""" Webscoket Connections
"""

from websocket import create_connection


def websocket_connection():
    """A fuinction to create a Websocket connection"""

    ws = create_connection("ws://echo.websocket.events/")
    print(ws.recv())
    print("Sending test message...")
    ws.send("TEST MSG")
    result = ws.recv()
    print(f"Recieved {result}")
    print("Closing connection...")
    ws.close()
    print("Connection closed.")


if __name__ == "__main__":
    websocket_connection()
