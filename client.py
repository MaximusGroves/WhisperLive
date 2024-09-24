from whisper_live.client import TranscriptionClient

# Initialize the client to connect to your running server
client = TranscriptionClient(
    "localhost",    # Server address (your server is running locally)
    9090,           # Port (the same port you used for the server)
    lang="en",      # Specify language (e.g., "en" for English)
    translate=False, # Set to True if you want translation
    model="base",   # Whisper model size (choose from "tiny", "base", "small", etc.)
    use_vad=True,   # Voice Activity Detection (can be set to True if desired)
    save_output_recording=False,  # Do not save microphone input
    relay_host="localhost",
    relay_port=9091
)

# Start live transcription from the microphone
client()