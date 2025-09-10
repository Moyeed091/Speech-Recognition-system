import os
import speech_recognition as sr
from datetime import datetime

# Paths
AUDIO_DIR = "audio_samples"
OUTPUT_DIR = "transcriptions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(file_path) as source:
            print(f"[INFO] Listening to {file_path}...")
            audio_data = recognizer.record(source)

        print("[INFO] Transcribing...")
        text = recognizer.recognize_google(audio_data)
        print("[SUCCESS] Transcription complete!\n")
        print(">>", text)

        # Save the transcription
        save_transcription(file_path, text)

    except sr.UnknownValueError:
        print("[ERROR] Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"[ERROR] Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"[ERROR] Something went wrong: {e}")

def save_transcription(audio_file, text):
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"{base_name}_{timestamp}.txt")

    with open(output_file, "w") as f:
        f.write(text)

    print(f"[INFO] Transcription saved to: {output_file}")

def main():
    # Choose your audio file
    audio_file = os.path.join(AUDIO_DIR, "sample.wav")

    if not os.path.isfile(audio_file):
        print(f"[ERROR] Audio file not found: {audio_file}")
        return

    transcribe_audio(audio_file)

if __name__ == "__main__":
    main()
