# Owner: Nangulu Hezron Wekesa
# Phone: +254714415034
import subprocess
import os
import tkinter as tk
import webbrowser
import requests
import ctypes as ct
import threading
from datetime import datetime
global PATH_ENTRY, STATUS, TIME_INTERVAL, app, bat_file_c, seconds_intervals, stop_process, TERMINAL_WIDGET
result = None
git_commit_push_count = 1



def show_about():
    webbrowser.open('https://github.com/Hezron26/Auto_git_commit_push')


def support_info():
    webbrowser.open('https://www.buymeacoffee.com/hezronna')


def change_bg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))


def change_fg_OnHover(button, colorOnHover, colorOnLeave):  # Color change on Mouse Hover
    button.bind("<Enter>", func=lambda e: button.config(fg=colorOnHover))
    button.bind("<Leave>", func=lambda e: button.config(fg=colorOnLeave))


def validate_int(input):
    if input.isdigit():
        return True
    elif input == "" or input.startswith("-") and input[1:].isdigit():
        return True
    else:
        return False


def git_comit_push():
    global stop_process, result
    if stop_process != 'yes':
        global TERMINAL_WIDGET, git_commit_push_count, STATUS, app, app
        try:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            subprocess.run(["git", "add", "--all"], check=True)
            subprocess.run(["git", "commit", "-m", f"Committed {formatted_datetime}"], check=True)
            subprocess.run(["git", "push"], check=True)



            STATUS.config(text=f'Committed and Pushed made: {git_commit_push_count} ')
            git_commit_push_count += 1
            print(seconds_intervals)
        except:
            pass
        Terminal_feed()
        app.after(seconds_intervals, git_comit_push)



def stop():
    global stop_process
    stop_process = 'yes'
    STATUS_2.config(text="Process Stopped....", fg='blue')


def start():
    global app, bat_file_c, seconds_intervals, stop_process
    stop_process = 'no'
    if PATH_ENTRY.get() != "" and TIME_INTERVAL.get() != "":
        STATUS.config(text='')
        # C:/Users/HEZRON WEKESA/Desktop/python Project/Compiler Build/Compiler
        file_path = "C:/Users/HEZRON WEKESA/Desktop/python Project/Compiler Build/Compiler"
        #file_path = PATH_ENTRY.get()
        if os.path.exists(file_path):
            time = int(TIME_INTERVAL.get())
            STATUS.config(fg='green', text=f'Will auto comit and push after Every {time} minute')
            seconds_intervals = time * 60 * 1000
            app.after(1000, git_comit_push)
        else:
            STATUS.config(text='ERROR : directory does not exist, check the path ')
    else:
        STATUS.config(text="ERROR: fill both entry's, (git directory path) and (time interval in minutes)", fg='red')


def download_app_icon():
    url = "https://raw.githubusercontent.com/Hezron26/assets/main/panda.ico"
    filename = 'panda.ico'
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
def Terminal_feed():
    global TERMINAL_WIDGET
    result = subprocess.run(["python", "your_script.py"], capture_output=True, text=True, check=True)
    TERMINAL_WIDGET.insert(tk.END, result.stdout)
    TERMINAL_WIDGET.insert(tk.END, result.stderr)

    self.text_widget.see(tk.END)  # Scroll to the end of the text widget
def main():
    global PATH_ENTRY, STATUS, TIME_INTERVAL, app, STATUS_2, TERMINAL_WIDGET
    bg_color = "#1B1B1B"
    bg_color = "#212122"
    bg_color = "#1F201F"
    app = tk.Tk()
    app.config(bg=bg_color)
    app.maxsize(950, 500)
    app.minsize(950, 500)
    app.title('Auto - Git')
    # app.attributes("-toolwindow", 1)
    # app.attributes("-topmost", 1)
    dark_title_bar(app)
    try:
        app.iconbitmap("panda.ico")
    except:
        download_app_icon()
        try:
             app.iconbitmap("panda.ico")
        except:
            pass

    on_c = '#2B3230'
    of_c = '#2B2B2C'
    fg_color = 'gray'
    PATH_lABALE = tk.Label(app, text='PATH :', fg=fg_color, bg=bg_color, font=("Courier New", 13), anchor='e', borderwidth=0, border=0)
    PATH_lABALE.place(relx=0.01, rely=0.05, relheight=0.07, relwidth=0.15)

    PATH_ENTRY = tk.Entry(app, bg=of_c, fg=fg_color, insertbackground='white', font=("Calibri", 12, "italic"), borderwidth=0, border=0)
    PATH_ENTRY.place(relx=0.17, rely=0.05, relheight=0.07, relwidth=0.8)
    change_bg_OnHover(PATH_ENTRY, on_c, of_c)

    TIME_RANGE = tk.Label(app, text='TIME(min):', fg=fg_color,  bg=bg_color, font=("Courier New", 13), anchor='e', borderwidth=0, border=0)
    TIME_RANGE.place(relx=0.01, rely=0.14, relheight=0.07, relwidth=0.15)

    validation = app.register(validate_int)  # create a validation function that only allows integers
    TIME_INTERVAL = tk.Entry(app, bg=of_c, fg=fg_color, insertbackground='white', borderwidth=0, border=0, validate="key", font=("Calibri", 12, "italic"), validatecommand=(validation, "%P"))
    TIME_INTERVAL.place(relx=0.17, rely=0.14, relheight=0.07, relwidth=0.8)
    change_bg_OnHover(TIME_INTERVAL, on_c, of_c)

    STATUS = tk.Label(app, bg=bg_color, font=("Calibri", 10), anchor='w', borderwidth=0, border=0)
    STATUS.place(relx=0.17, rely=0.3, relheight=0.04, relwidth=0.8)




    START_BTN = tk.Button(app, text='START', bg='#354230', borderwidth=0, border=0, command=start, font=("Courier New", 10))
    START_BTN.place(relx=0.4, rely=0.24, relheight=0.04, relwidth=0.12)
    change_bg_OnHover(START_BTN, '#2F4F4F', '#354230')

    STOP_BTN = tk.Button(app, text='STOP', bg='#354230', borderwidth=0, border=0, command=stop, font=("Courier New", 10))
    STOP_BTN.place(relx=0.53, rely=0.24, relheight=0.04, relwidth=0.12)
    change_bg_OnHover(STOP_BTN, '#2F4F4F', '#354230')

    SUPPORT = tk.Button(app, text='support', bg=bg_color, activebackground=bg_color, fg="gray", activeforeground='red',  font=("Courier New italic", 8), borderwidth=0, border=0, command=support_info)
    SUPPORT.place(relx=0.274, rely=0.968, relheight=0.03, relwidth=0.12)
    change_fg_OnHover(SUPPORT, '#2F4F4F', fg_color)




    TERMINAL = tk.Button(app, text='terminal',  bg=bg_color,  activebackground=bg_color, fg="gray", activeforeground='red', font=("Courier New italic", 8), borderwidth=0, border=0)
    TERMINAL.place(relx=0.14, rely=0.968, relheight=0.03, relwidth=0.12)
    change_fg_OnHover(TERMINAL, '#2F4F4F', fg_color)

    ABOUT = tk.Button(app, text='about',  bg=bg_color, activebackground=bg_color, fg="gray", activeforeground='red', font=("Courier New italic", 8), borderwidth=0, border=0, command=show_about)
    ABOUT.place(relx=0.01, rely=0.968, relheight=0.03, relwidth=0.12)
    change_fg_OnHover(ABOUT, '#2F4F4F', fg_color)

    TERMINAL_WIDGET = tk.Text(app, bg='white', fg="gray", font=("Courier New", 8), borderwidth=0, border=0)
    TERMINAL_WIDGET.place(relx=0.0, rely=0.668, relheight=0.3, relwidth=1)

    app.mainloop()


if __name__ == "__main__":
    main()
