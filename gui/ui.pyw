import PySimpleGUI as sg

from app.app_settings import WHISPER_MODELS
from .code import translate_audio

layout = [
    [
        sg.FileBrowse("Select audio file", size=(15, 2)),
        sg.Text(
            size=(50, 1),
            font=("Segoe UI", 14, "bold"),
            background_color="white", text_color="grey")
    ],
    [
        sg.Button("Translate", disabled=True, size=(15, 2), key="-PROCESS-"),
        sg.Combo(values=WHISPER_MODELS,
                 #  default_value=WHISPER_MODELS[2],
                 size=(10, len(WHISPER_MODELS)),
                 font=("Segoe UI", 12),
                 enable_events=True,
                 readonly=True,
                 key="-MODEL-"),
        sg.Text("", size=(30)),
        sg.Push(),
        sg.Button("Copy")
    ],
    [
        sg.Multiline("Translation result", disabled=True,
                     autoscroll=True,
                     expand_x=True,
                     enable_events=True,
                     size=(80, 10),
                     key="-TEXT-")
    ]
]

window = sg.Window("Text To Speech Converter", layout=layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    elif event == "-MODEL-":
        window["-PROCESS-"].update(disabled=False)

    elif event == "-PROCESS-":
        translate_results = translate_audio(
            values["Select audio file"], values["-MODEL-"], window)
        window["-TEXT-"].update(translate_results[0].text)

window.close()
