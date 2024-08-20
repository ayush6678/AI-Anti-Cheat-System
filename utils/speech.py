import pyaudio
import numpy as np
import time

# Parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
OUTPUT_FILE = "volume_output.txt"

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording sound levels for 10 seconds...")

# Open file for writing
with open(OUTPUT_FILE, 'w') as f:
    # Record for 10 seconds
    for i in range(RECORD_SECONDS):
        # Read audio data
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        
        # Calculate RMS of the data
        rms = np.sqrt(np.mean(np.square(data)))
        
        # Convert to decibels
        if rms > 0:
            db = 20 * np.log10(rms)
        else:
            db = -np.inf  # Represent silence as negative infinity dB
        
        # Write to file
        if np.isfinite(db):
            f.write(f"Second {i+1}: {db:.2f} dB\n")
        else:
            f.write(f"Second {i+1}: 0 dB (silence)\n")
        
        # Wait for 1 second
        time.sleep(1)

print(f"Sound levels have been saved to {OUTPUT_FILE}")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()