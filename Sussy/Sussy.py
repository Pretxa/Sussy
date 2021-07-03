import os

safeguard = input("Enter the safeguard password: ")

if safeguard != "sus":
    quit()

print("Injecting very dangerous and illegal malware...")
encrypted_extensions = ('.txt',)

file_paths = []

for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_extensions:
            file_paths.append(root+'\\'+file)

for item in file_paths:
    print(item)

x = input("""

 __   __                     _     _ _     _                 _                           _        _                _     __  __    _    ___   
 \ \ / /__  _   _ _ __   ___| |__ (_) |_  | |__   __ _ ___  | |__   ___  ___ _ __    ___| |_ ___ | | ___ _ __     | |   |  \/  |  / \  / _ \  
  \ V / _ \| | | | '__| / __| '_ \| | __| | '_ \ / _` / __| | '_ \ / _ \/ _ \ '_ \  / __| __/ _ \| |/ _ \ '_ \    | |   | |\/| | / _ \| | | | 
   | | (_) | |_| | |    \__ \ | | | | |_  | | | | (_| \__ \ | |_) |  __/  __/ | | | \__ \ || (_) | |  __/ | | |_  | |___| |  | |/ ___ \ |_| | 
   |_|\___/ \__,_|_|    |___/_| |_|_|\__| |_| |_|\__,_|___/ |_.__/ \___|\___|_| |_| |___/\__\___/|_|\___|_| |_(_) |_____|_|  |_/_/   \_\___(_)
                                                                                                                                              
""")
