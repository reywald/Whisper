from app.speech_to_text import (
    create_model,
    get_audio_file,
    decode_audio_file
)

from PySimpleGUI import Window


def translate_audio(audio_file: str, model_type: str, window: Window):
    wave = get_audio_file(audio_file)
    window.write_event_value("-LOAD AUDIO-", "Audio file waveform created")

    model = create_model(model_type)
    window.write_event_value("-CREATE MODEL-", f"{model_type} created")

    window.write_event_value("-TRANSLATE AUDIO-", "Translating audio")
    result, lang = decode_audio_file(audio=wave, model=model)
    window.write_event_value("-TRANSLATE AUDIO-", "Audio translated")

    return result, lang
