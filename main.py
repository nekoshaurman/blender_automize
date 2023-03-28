import subprocess
from PySimpleGUI import WINDOW_CLOSED, WIN_CLOSED
from multiprocessing import cpu_count
from gui import make_window, show_string, resource_path
from sys import version_info


def check_data(window_values, string):
    if window_values["_blender_"][-11:] == 'blender.exe' and \
            window_values["_text" + str(string) + "1_"][-6:] == '.blend' and \
            window_values["_text" + str(string) + "2_"] != '' and \
            window_values["_frame" + str(string) + "1_"].isdigit() and \
            window_values["_frame" + str(string) + "2_"].isdigit():
        return True
    else:
        return False


if __name__ == '__main__':
    strings_count = 0
    window = make_window()

    while True:  # The Event Loop
        event, values = window.read()
        if event in (None, 'Exit', 'Cancel'):
            break

        elif '_NEWRENDER_' in event:
            if strings_count < 20:
                show_string(window, strings_count + 1)
                strings_count += 1

            elif strings_count == 20:
                print("Max Rows")
                window["_ADDWARNING_"].Update(visible=True)

        elif '_RENDER_' in event and strings_count:
            threads = values["_threads_"]
            if not threads.isdigit():
                threads = str(cpu_count())

            for string in range(1, strings_count + 1):
                if check_data(values, string):
                    blenderexe = f"{values['_blender_']}"

                    blenderfile = f"{values[f'_text{string}1_']}"

                    notfound = True
                    n = -7
                    while notfound:
                        if values[f"_text{string}1_"][n] == "/":
                            notfound = False
                        else:
                            n -= 1
                    n = n + 1

                    outdirectory = f'{values[f"_text{string}2_"]}/{values[f"_text{string}1_"][n:-6]}.####'

                    from_frame = f"{values[f'_frame{string}1_']}"
                    to_frame = f"{values[f'_frame{string}2_']}"

                    commandstr = [blenderexe, '-b', blenderfile, '-o', outdirectory, '-s', from_frame, '-e',
                                  to_frame, '-t', threads, '-a']

                    print("File ", string, ": Start rendering...")

                    with subprocess.Popen(args=commandstr, shell=True, stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL) as p:
                        output = ''
                        for line in p.stdout:
                            line = line.decode(errors='replace' if version_info < (3, 5)
                                                                else 'backslashreplace').rstrip()
                            output += line
                            print(line)
                            if window:
                                window.refresh()
                                event, values = window.read(timeout=0)

                                if event == '_STOP_':
                                    p = subprocess.Popen("taskkill /f /im blender.exe", shell=True,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.STDOUT,
                                                         stdin=subprocess.DEVNULL)
                                    print('STOPPED')
                                    break

                                elif event == WINDOW_CLOSED or event == WIN_CLOSED:
                                    p = subprocess.Popen("taskkill /f /im blender.exe", shell=True,
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.STDOUT,
                                                         stdin=subprocess.DEVNULL)
                                    break

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

        file = open('data.log', 'w')
        file.write(str(values["_blender_"]))
        file.close()
    window.close()
