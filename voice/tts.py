import subprocess
import threading
import queue
import tempfile
import os
import time
import re

from playsound import playsound

MODEL_PATH = "en_US-ryan-high.onnx"

speech_queue = queue.Queue()
stop_event = threading.Event()


def clean_response(text):
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`.*?`', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'[#*_~<>|]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def _generate_audio(text, wav_file):
    result = subprocess.run(
        [
            "piper",
            "--model",
            MODEL_PATH,
            "--output_file",
            wav_file
        ],
        input=text,
        text=True,
        capture_output=True
    )

    return result.returncode == 0


def _voice_worker():
    while True:
        text = speech_queue.get()

        if text is None:
            break

        if stop_event.is_set():
            stop_event.clear()
            speech_queue.task_done()
            continue

        try:
            with tempfile.NamedTemporaryFile(
                suffix=".wav",
                delete=False
            ) as temp_file:

                wav_file = temp_file.name

            success = _generate_audio(text, wav_file)

            if success and not stop_event.is_set():
                playsound(wav_file)

            try:
                os.remove(wav_file)
            except:
                pass

        except Exception as e:
            print("TTS Error:", e)

        speech_queue.task_done()


worker_thread = threading.Thread(
    target=_voice_worker,
    daemon=True
)

worker_thread.start()


def speak(text):
    text = clean_response(text)

    if not text.strip():
        return

    speech_queue.put("............" + text)


def stop_speaking():
    stop_event.set()

    while not speech_queue.empty():
        try:
            speech_queue.get_nowait()
            speech_queue.task_done()
        except:
            break