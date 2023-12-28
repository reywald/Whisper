import pytest
from whisper import Whisper

from app.speech_to_text import create_model
from app.utilities import ModelSelectionError


def test_empty_model():
    """
    Verify that if an empty model is sent to create_model, an error is thrown
    """

    with pytest.raises(TypeError):
        model = create_model()


@pytest.mark.parametrize("model_name", [
    "Bitwolf",
    "Sub-Ex",
    "Fix San",
    "Biodex",
    "Greenlam",
    "Tempsoft",
    "Overhold",
    "Zamit",
    "Bamity",
    "Zoolab"
])
def test_non_existing_model(model_name):
    """
    Verify that if an invalid model is sent to create_model, an error is thrown
    """

    with pytest.raises(ModelSelectionError):
        model = create_model(model_name)


@pytest.mark.parametrize("model_name", [
    "medium",
    "small",
    "base",
    "tiny",
    "medium"
])
def test_valid_model(model_name):
    """
    Verify that if the right model is sent to create_model, a Whisper instance is returned
    """

    model = create_model(model_name)
    assert isinstance(model, Whisper)


# TODO: Add tests for when the model needs to be downloaded the local machine
