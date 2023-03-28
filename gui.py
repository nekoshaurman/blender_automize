import PySimpleGUI as sg
from PySimpleGUI import Button, Text, InputText, FileBrowse, FolderBrowse, Multiline, Window
from multiprocessing import cpu_count
from os import path
import sys


def show_string(window: Window, number: int):
    window[f'_string{number}_'].update(visible=True)
    window[f'_text{number}1_'].update(visible=True)
    window[f'_browse{number}1_'].update(visible=True)
    window[f'_text{number}2_'].update(visible=True)
    window[f'_browse{number}2_'].update(visible=True)
    window[f'_frame{number}1_'].update(visible=True)
    window[f'_frame{number}2_'].update(visible=True)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = path.abspath(".")

    return path.join(base_path, relative_path)


def make_window():
    try:
        file = open('data.log', 'r')
        blender_exe = file.readline()
        file.close()
    except:
        blender_exe = ''
    layout = [
        [
            Button('Add Row', key='_NEWRENDER_'),
            Text("You added maximum files!", key="_ADDWARNING_", visible=False),
        ],
        [
            Text('Blender.exe:'),
            InputText(default_text=blender_exe, key='_blender_', size=(25, 1), visible=True),
            FileBrowse(key='_blender2_', visible=True, target='_blender_', file_types=(('blender.exe', '*.exe'),)),
            Text('Threads:'),
            InputText(default_text=str(cpu_count()), key='_threads_', size=(5, 1), visible=True),
        ],
        [
            Text('#', size=(2, 1)),
            Text('.blend file location', size=(25, 1)),
            Text(' ', size=(3, 1)),
            Text('Folder for result', size=(25, 1)),
            Text(' ', size=(3, 1)),
            Text('First', size=(5, 1)),
            Text('Last', size=(5, 1)),
        ],
    ]

    for i in range(1, 21):
        row = [
            Text(str(i), key=f'_string{i}_', visible=False, size=(2, 1)),
            InputText(key=f'_text{i}1_', size=(25, 1), visible=False),
            FileBrowse(key=f'_browse{i}1_', visible=False,
                       target=f'_text{i}1_', file_types=(('Blender Files', '*.blend'),)),
            InputText(key=f'_text{i}2_', size=(25, 1), visible=False),
            FolderBrowse(key=f'_browse{i}2_', visible=False),
            InputText(key=f'_frame{i}1_', size=(5, 1), visible=False),
            InputText(key=f'_frame{i}2_', size=(5, 1), visible=False),
        ]
        layout.append(row)

    lower_buttons = [Button('Render', key='_RENDER_'), sg.Button('Stop', key='_STOP_'), ],
    layout.append(lower_buttons)
    output_window = [Multiline(size=(100, 15), autoscroll=True, auto_refresh=True, reroute_stdout=True), ]
    layout.append(output_window)

    window = Window(title='Blender Automize', layout=layout, icon=resource_path('blender.ico'))
    return window
