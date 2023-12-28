from app.speech_to_text import (
    create_model,
    get_audio_file,
    decode_audio_file
)


wave = get_audio_file("audio.mp3")
model = create_model("base")
result, lang = decode_audio_file(audio=wave, model=model)

print(result.text)
print(f"Language: {lang}")
