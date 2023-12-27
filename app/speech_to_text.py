import whisper
from whisper import Whisper
from pathlib import Path


def create_model(model: str) -> Whisper:
    """ Load a whisper model

        Parameters
        ---------- 
        model: str
            The selected model to be used or downloaded by whisper

        Returns
        -------
        :Whisper
            The Whisper instances selected/downloaded
    """

    return whisper.load_model(model)


def get_audio_file(filename: str):
    """
        Load an audio file using the supplied path. Ensure the file exists, 
        and the file is an mp3 file

        Parameters
        ----------
        filename: str
            The path to the audio file

        Returns
        -------
        audio:
            The audio waveform as a Numpy array
    """

    fp = Path(filename)

    if fp.exists():
        if fp.suffix == ".mp3":
            audio = whisper.load_audio(file=filename)
            audio = whisper.pad_or_trim(audio)
        
        else:
            raise Exception(f"{fp.name} should be an mp3 file")

    else:
        raise FileNotFoundError(f"{fp.name} not found")

    return audio


def decode_audio_file(audio, model: Whisper):
    """
        Make a spectrogram and use it to decode the audio and language

        Parameters
        ----------
        audio: NDArray
            The audio waveform as a Numpy array

        model: Whisper
            An instance of the whisper model

        Returns
        -------
        result: DecodingResult
            The decoded result dataclass containing text and language

        language: str
            The language string based on getting the maximum of the language probabilities
    """

    # Make log-Mel spectrogram and move to the same device as the model
    log_mel = whisper.log_mel_spectrogram(audio=audio).to(model.device)

    # Detect the spoken languagne
    _, language_probs = model.detect_language(mel=log_mel)
    language = max(language_probs, key=language_probs.get)

    # Decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model=model, mel=log_mel, options=options)

    # Return the text and detected language
    return result, language