import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os

# STEP 1: Load Whisper model (Tiny version for low-end PCs)
model = whisper.load_model("tiny")  # Use "base" if you have more RAM

# STEP 2: Record audio from microphone
def record_audio(duration=5, sample_rate=16000):
    print("\nRecording... Speak now! (Ctrl+C to stop)")
    try:
        audio = sd.rec(int(duration * sample_rate), 
                      samplerate=sample_rate, 
                      channels=1, 
                      dtype='float32')
        sd.wait()  # Wait until recording finishes
        print("Recording complete.")
        return audio.flatten()
    except Exception as e:
        print(f"Recording error: {e}")
        return None

# STEP 3: Save audio to a temporary WAV file
def save_audio(audio, filename="temp_audio.wav", sample_rate=16000):
    try:
        scaled = np.int16(audio * 32767)  # Convert to 16-bit PCM
        write(filename, sample_rate, scaled)
        print(f"Audio saved to {filename}")
        return True
    except Exception as e:
        print(f"Save error: {e}")
        return False

# STEP 4: Transcribe audio to text
def transcribe_audio(filename="temp_audio.wav"):
    try:
        if not os.path.exists(filename):
            print("Error: Audio file not found!")
            return None
            
        result = model.transcribe(filename, fp16=False)
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
            
        # Save audio
        if not save_audio(audio):
            return
            
        # Transcribe audio
        text = transcribe_audio()
        if text:
            print(f"\nTranscription: {text}")
            
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    print("=== Sentinel S0 - STT Module ===")
    main()