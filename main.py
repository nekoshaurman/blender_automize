import PySimpleGUI as sg
import subprocess
import multiprocessing
import sys

threads = multiprocessing.cpu_count()

layout = [
    [
        sg.Button('Add File', key='_NEWRENDER_'),
        sg.Text("You added maximum files!", key="_ADDWARNING_", visible=False),
    ],
    [
        sg.Text('Blender.exe:'),
        sg.InputText(key='_blender_', size=(25, 1), visible=True),
        sg.FileBrowse(key='_blender_', visible=True, target='_blender_', file_types=(('blender.exe', '*.exe'),)),
        sg.Text('Threads:'),
        sg.InputText(default_text=str(threads), key='_threads_', size=(5, 1), visible=True),
    ],
    [
        sg.Text('#', size=(2, 1)),
        sg.Text('.blend file location', size=(25, 1)),
        sg.Text(' ', size=(3, 1)),
        sg.Text('Folder for result', size=(25, 1)),
        sg.Text(' ', size=(3, 1)),
        sg.Text('First', size=(5, 1)),
        sg.Text('Last', size=(5, 1)),
    ],
    [
        sg.Text('1', key='_string1_', visible=False, size=(2, 1)),
        sg.InputText(key='_text11_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse11_', visible=False, target='_text11_', file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text12_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse12_', visible=False),
        sg.InputText(key='_frame11_', size=(5, 1), visible=False),
        sg.InputText(key='_frame12_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('2', key='_string2_', visible=False, size=(2, 1)),
        sg.InputText(key='_text21_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse21_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text22_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse22_', visible=False),
        sg.InputText(key='_frame21_', size=(5, 1), visible=False),
        sg.InputText(key='_frame22_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('3', key='_string3_', visible=False, size=(2, 1)),
        sg.InputText(key='_text31_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse31_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text32_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse32_', visible=False),
        sg.InputText(key='_frame31_', size=(5, 1), visible=False),
        sg.InputText(key='_frame32_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('4', key='_string4_', visible=False, size=(2, 1)),
        sg.InputText(key='_text41_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse41_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text42_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse42_', visible=False),
        sg.InputText(key='_frame41_', size=(5, 1), visible=False),
        sg.InputText(key='_frame42_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('5', key='_string5_', visible=False, size=(2, 1)),
        sg.InputText(key='_text51_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse51_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text52_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse52_', visible=False),
        sg.InputText(key='_frame51_', size=(5, 1), visible=False),
        sg.InputText(key='_frame52_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('6', key='_string6_', visible=False, size=(2, 1)),
        sg.InputText(key='_text61_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse61_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text62_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse62_', visible=False),
        sg.InputText(key='_frame61_', size=(5, 1), visible=False),
        sg.InputText(key='_frame62_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('7', key='_string7_', visible=False, size=(2, 1)),
        sg.InputText(key='_text71_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse71_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text72_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse72_', visible=False),
        sg.InputText(key='_frame71_', size=(5, 1), visible=False),
        sg.InputText(key='_frame72_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('8', key='_string8_', visible=False, size=(2, 1)),
        sg.InputText(key='_text81_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse81_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text82_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse82_', visible=False),
        sg.InputText(key='_frame81_', size=(5, 1), visible=False),
        sg.InputText(key='_frame82_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('9', key='_string9_', visible=False, size=(2, 1)),
        sg.InputText(key='_text91_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse91_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text92_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse92_', visible=False),
        sg.InputText(key='_frame91_', size=(5, 1), visible=False),
        sg.InputText(key='_frame92_', size=(5, 1), visible=False),
    ],
    [
        sg.Text('10', key='_string10_', visible=False, size=(2, 1)),
        sg.InputText(key='_text101_', size=(25, 1), visible=False),
        sg.FileBrowse(key='_browse101_', visible=False, file_types=(('Blender Files', '*.blend'),)),
        sg.InputText(key='_text102_', size=(25, 1), visible=False),
        sg.FolderBrowse(key='_browse102_', visible=False),
        sg.InputText(key='_frame101_', size=(5, 1), visible=False),
        sg.InputText(key='_frame102_', size=(5, 1), visible=False),
    ],
    [
        sg.Button('Render', key='_RENDER_'),
    ],
    [
        sg.Multiline(size=(100, 15), autoscroll=True, auto_refresh=True, reroute_stdout=True),
    ],
]

window = sg.Window('Blender Automize', layout)
stringscount = 0

while True:  # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    elif '_NEWRENDER_' in event:
        if stringscount < 10:
            stringscount += 1
        else:
            print("No more strings")
            window["_ADDWARNING_"].Update(visible=True)
            window["_string10_"].Update()

        stringkey = "_string" + str(stringscount) + "_"
        text1key = "_text" + str(stringscount) + "1_"
        text2key = "_text" + str(stringscount) + "2_"
        browse1key = "_browse" + str(stringscount) + "1_"
        browse2key = "_browse" + str(stringscount) + "2_"
        frame1key = "_frame" + str(stringscount) + "1_"
        frame2key = "_frame" + str(stringscount) + "2_"

        window[stringkey].Update(visible=True)
        window[text1key].Update(visible=True)
        window[browse1key].Update(visible=True)
        window[text2key].Update(visible=True)
        window[browse2key].Update(visible=True)
        window[frame1key].Update(visible=True)
        window[frame2key].Update(visible=True)

    if '_RENDER_' in event and stringscount:

        # logfile = open("stdout.log", "w")
        threads = values["_threads_"]
        if not threads.isdigit():
            threads = str(multiprocessing.cpu_count())

        for string in range(1, stringscount + 1):
            if values["_blender_"][-11:] == 'blender.exe' and \
                    values["_text" + str(string) + "1_"][-6:] == '.blend' and \
                    values["_text" + str(string) + "2_"] != '' and \
                    values["_frame" + str(string) + "1_"].isdigit() and \
                    values["_frame" + str(string) + "2_"].isdigit():

                # logfile.write("=================================================="
                              # "=================================================="
                              # "================================================\n")

                blenderexe = '"' + values["_blender_"] + '"'

                blenderfile = '"' + values["_text" + str(string) + "1_"] + '"'

                notfound = True
                n = -7
                while notfound:
                    if values["_text" + str(string) + "1_"][n] == "/":
                        notfound = False
                    else:
                        n -= 1
                n = n + 1

                outdirectory = '"' + values["_text" + str(string) + "2_"] + "/" \
                               + "/" + values["_text" + str(string) + "1_"][n:-6] + ".####" + '"'
                         # + values["_text" + str(string) + "1_"][n:-6] \
                         # + "/" + values["_text" + str(string) + "1_"][n:-6] + ".####" + '"'

                commandstr = str(blenderexe + " -b " + blenderfile + " -o " + outdirectory \
                          + " -s " + values["_frame" + str(string) + "1_"] + " -e " \
                          + values["_frame" + str(string) + "2_"] + " -t " + threads + " -a")

                print("File ", string, ": Start rendering...")
                # WORK WITH FILE OUTPUT
                #blender = subprocess.Popen(commandstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                #for line in blender.stdout.readlines():
                    #logfile.write(line)
                #with subprocess.Popen(commandstr, shell=True, stdout=subprocess.PIPE,
                                      #stderr=subprocess.STDOUT, universal_newlines=True) as blender:
                    #for line in blender.stdout:
                        #logfile.write(line)

                # WORK WITH OUTPUT
                p = subprocess.Popen(commandstr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output = ''
                for line in p.stdout:
                    line = line.decode(errors='replace' if (sys.version_info) < (3, 5)
                    else 'backslashreplace').rstrip()
                    output += line
                    print(line)
                    if window:
                        window.refresh()
                print("File ", string, ": End")

            else:
                print("File ", string, ":", end="")
                if values["_blender_"][-11:] != 'blender.exe':
                    print(" blender.exe error")
                elif values["_text" + str(string) + "1_"][-6:] != '.blend':
                    print(" file.blend error")
                elif values["_text" + str(string) + "2_"] == '':
                    print(" output directory error")
                else:
                    print(" frames error")

        # logfile.close()

window.close()

