import websocket
import threading
import time
import json

def on_message(ws, message):
    data = json.loads(message)
    text = data.get('text', '')
    print(f"Received Text: {text}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed: {close_status_code} - {close_msg}")

def on_open(ws):
    print("Connected to relay server")

if __name__ == "__main__":
    # Replace with the actual host and port of your relay server
    relay_host = 'localhost'  # Use 'localhost' if connecting from the same machine
    relay_port = 9091
    ws_url = f"ws://{relay_host}:{relay_port}"

    # Enable WebSocket debug trace output (optional)
    # websocket.enableTrace(True)

    ws = websocket.WebSocketApp(
        ws_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    # Run the WebSocket client in a separate thread
    ws_thread = threading.Thread(target=ws.run_forever)
    ws_thread.daemon = True
    ws_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Closing connection")
        ws.close()
        ws_thread.join()
