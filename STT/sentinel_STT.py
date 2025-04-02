import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
from pathlib import Path

# STEP 1: Load Whisper model
model = whisper.load_model("tiny")

# STEP 2: Create UTILS directory if it doesn't exist
os.makedirs("UTILS", exist_ok=True)

# STEP 3: Record audio
def record_audio(duration=5, sample_rate=16000):
    print("\nRecording... Speak now! (Waiting", duration, "seconds)")
    try:
        audio = sd.rec(int(duration * sample_rate),
                      samplerate=sample_rate,
                      channels=1,
                      dtype='int16')
        sd.wait()
        return audio
    except Exception as e:
        print("Recording failed:", e)
        return None

# STEP 4: Save audio with absolute path handling
def save_audio(audio, filename="temp_audio.wav", sample_rate=16000):
    try:
        # Create full path
        full_path = os.path.join("UTILS", filename)
        write(full_path, sample_rate, audio)
        print("Audio saved to:", os.path.abspath(full_path))
        return full_path  # Return the full path
    except Exception as e:
        print("Save failed:", e)
        return None

# STEP 5: Transcribe audio with path verification
def transcribe_audio(filepath):
    try:
        if not os.path.exists(filepath):
            print(f"Error: File not found at {filepath}")
            return None
            
        print(f"Attempting to transcribe from: {filepath}")
        result = model.transcribe(filepath, fp16=False)
        return result["text"]
    except Exception as e:
        print(f"Transcription error: {e}")
        return None

# MAIN FUNCTION
def main():
    try:
        # Record audio
        audio = record_audio(duration=5)
        if audio is None:
            return
            
        # Save audio and get full path
        audio_path = save_audio(audio)
        if not audio_path:
            return
            
        # Verify file exists and has content
        if os.path.getsize(audio_path) == 0:
            print("Error: Audio file is empty!")
            return
            
        # Transcribe audio
        text = transcribe_audio(audio_path)
        if text:
            print(f"\nTranscription: {text}")
        else:
            print("No transcription returned")
            
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    print("=== Sentinel S0 - STT Module ===")
    main()