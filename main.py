# imports ------------------------------------------------------
import sys
import json
import os
import shutil
# --------------------------------------------------------------

# getting pathes -----------------------------------------------
if getattr(sys, 'frozen', False):
    app_path: str = os.path.dirname(sys.executable)
elif __file__:
    app_path: str = os.path.dirname(__file__)
app_path = app_path.replace("\\", "/")
call_path: str = os.getcwd().replace("\\", "/")
# --------------------------------------------------------------

# additional ---------------------------------------------------
def isempty(path: str) -> bool: # is the file empty
    with open(path, 'r') as file:
        if file.read() == '':
           return True
    return False
# --------------------------------------------------------------

# file types ---------------------------------------------------
def launch(path: str, workfolder: str = call_path) -> None: # installing launch.json
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{workfolder}/.vscode/launch.json"):
        with open(f"{workfolder}/.vscode/launch.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"version": "2.0.0", "configurations": []}')
    if isempty(f"{workfolder}/.vscode/launch.json"):
        with open(f"{workfolder}/.vscode/launch.json", 'w') as vsccm:
            vsccm.write('{"version": "2.0.0", "configurations": []}')
    with open(f"{workfolder}/.vscode/launch.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict: dict = json.loads(vsc_file.read())
    try:
        for c in file_dict["configurations"]:
            vsc_file_dict["configurations"].append(c)
    except Exception:
        print("Something wrong with a file")
        return
    vsc_config_list: list = []
    for x in vsc_file_dict["configurations"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["configurations"] = vsc_config_list
    with open(f"{workfolder}/.vscode/launch.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def tasks(path: str, workfolder: str = call_path) -> None: # installing tasks.json
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{workfolder}/.vscode/tasks.json"):
        with open(f"{workfolder}/.vscode/tasks.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"version": "2.0.0", "tasks": []}')
    with open(f"{workfolder}/.vscode/tasks.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict: dict = json.loads(vsc_file.read())
    if isempty(f"{workfolder}/.vscode/tasks.json"):
        with open(f"{workfolder}/.vscode/tasks.json", 'w') as vsccm:
            vsccm.write('{"version": "2.0.0", "tasks": []}')
    try:
        for c in file_dict["tasks"]:
            vsc_file_dict["tasks"].append(c)
    except Exception:
        print("Something wrong with a file")
        return
    vsc_config_list: list = []
    for x in vsc_file_dict["tasks"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["tasks"] = vsc_config_list
    with open(f"{workfolder}/.vscode/tasks.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def settings(path: str, workfolder: str = call_path) -> None: # installing settings.json
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{workfolder}/.vscode/settings.json"):
        with open(f"{workfolder}/.vscode/settings.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{}')
    with open(f"{workfolder}/.vscode/settings.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict: dict = json.loads(vsc_file.read())
    if isempty(f"{workfolder}/.vscode/settings.json"):
        with open(f"{workfolder}/.vscode/settings.json", 'w') as vsccm:
            vsccm.write('{}')
    try:
        for c in file_dict:
            vsc_file_dict[c] = file_dict[c]
    except Exception:
        print("Something wrong with a file")
        return
    with open(f"{workfolder}/.vscode/settings.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def c_cpp_properties(path: str, workfolder: str = call_path): # installing c_cpp_properties.json
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{workfolder}/.vscode/c_cpp_properties.json"):
        with open(f"{workfolder}/.vscode/c_cpp_properties.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"configurations": []}')
    if isempty(f"{workfolder}/.vscode/c_cpp_properties.json"):
        with open(f"{workfolder}/.vscode/c_cpp_properties.json", 'w') as vsccm:
            vsccm.write('{"configurations": []}')
    with open(f"{workfolder}/.vscode/c_cpp_properties.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict: dict = json.loads(vsc_file.read())
    try:
        for c in file_dict["configurations"]:
            vsc_file_dict["configurations"].append(c)
    except Exception:
        print("Something wrong with a file")
        return
    vsc_config_list: list = []
    for x in vsc_file_dict["configurations"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["configurations"] = vsc_config_list
    with open(f"{workfolder}/.vscode/c_cpp_properties.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))
# --------------------------------------------------------------

# commands -----------------------------------------------------
def list_command(path: str) -> None: # command 'vsccm list'
    if not os.path.exists(f"{path}/.vscode") or not os.path.exists(f"{path}/vsccm-lock.json"):
        print("You haven't installed any configs")
    else:
        with open(f"{path}/vsccm-lock.json") as vsccm:
            vsccm_dict: dict = json.loads(vsccm.read())
        print("Installed configs:")
        for cfg in vsccm_dict["configs"]:
            print(f"|-{cfg}")

def remove_command(path: str) -> None: # command 'vsccm remove'
    if os.path.exists(f"{path}/.vscode"):
        shutil.rmtree(f"{path}/.vscode")
    if os.path.exists(f"{path}/vsccm-lock.json"):
        os.remove(f"{path}/vsccm-lock.json")
    print("Directory configs removed")

def clear_command(path: str) -> None: # command 'vsccm clear'
    if os.path.exists(f"{path}/.vscode"):
        shutil.rmtree(f"{path}/.vscode")
        os.mkdir(f"{path}/.vscode")
    if os.path.exists(f"{path}/vsccm-lock.json"):
        vsccm = open(f"{path}/vsccm-lock.json", 'w')
        vsccm.write('{"configs": []}')
        vsccm.close()
    print("Directory configs cleared")

def install_list_command() -> None: # command 'vsccm install list'
    global app_path
    print("Your configs:")
    for config in os.listdir(f"{app_path}/configs/"):
        if os.path.isdir(f"{app_path}/configs/{config}"):
            print(f"|-{config}")
            for file in os.listdir(f"{app_path}/configs/{config}"):
                if os.path.isfile(f"{app_path}/configs/{config}/{file}"):
                    print(f"  |-{file}")

def install_args_command(path: str, config_name: str) -> None: # command 'vsccm install' with arguments
    global app_path, call_path
    if not os.path.exists(f"{path}"):
        os.mkdir(f"{path}")
    if not os.path.exists(f"{path}/.vscode"):
        os.mkdir(f"{path}/.vscode")
    if not os.path.exists(f"{path}/vsccm-lock.json"):
        with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
            vsccm.write('{"configs": []}')
    if isempty(f"{path}/vsccm-lock.json"):
        with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
            vsccm.write('{"configs": []}')
    with open(f"{path}/vsccm-lock.json", 'r') as vsccm:
        configs: dict = json.loads(vsccm.read()) 
    try:
        configs_list: list = []
        with open(f"{call_path}/{config_name + ('.json' if config_name[-5:] != '.json' else '')}", 'r') as vsccm:
            configs_list = json.loads(vsccm.read())["configs"]
        if len(configs_list) > 0:
            for config in configs_list:
                try:
                    files: list = list(filter(lambda file: os.path.isfile(f"{app_path}/configs/{config}/{file}"), os.listdir(f"{app_path}/configs/{config}")))
                    for f in files:
                        if f == "launch.json":
                            launch(f"{app_path}/configs/{config}/launch.json", path)
                            print(f"'{config}' launch.json successfully installed")
                        elif f == "tasks.json":
                            tasks(f"{app_path}/configs/{config}/tasks.json", path)
                            print(f"'{config}' tasks.json successfully installed")
                        elif f == "settings.json":
                            settings(f"{app_path}/configs/{config}/settings.json", path)
                            print(f"'{config}' settings.json successfully installed")
                        elif f == "c_cpp_properties.json":
                            c_cpp_properties(f"{app_path}/configs/{config}/c_cpp_properties.json", path)
                            print(f"'{config}' c_cpp_properties.json successfully installed")
                    configs["configs"].append(config)
                    with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
                        vsccm.write(json.dumps(configs, ensure_ascii=False, indent=4))
                    print(f"'{config}' SUCCESSFULLY INSTALLED")
                except Exception:
                    print(f"'{config}' NOT FOUND")
    except Exception:
        print("Uncorrect arguments")

def install_config(path: str, i: int) -> None: # install config
    with open(f"{path}/vsccm-lock.json", 'r') as vsccm:
        configs: dict = json.loads(vsccm.read()) 
    files: list = list(filter(lambda file: os.path.isfile(f"{app_path}/configs/{sys.argv[i]}/{file}"), os.listdir(f"{app_path}/configs/{sys.argv[i]}")))
    for f in files:
        if f == "launch.json":
            launch(f"{app_path}/configs/{sys.argv[i]}/launch.json", path)
            print(f"'{sys.argv[i]}' launch.json successfully installed")
        elif f == "tasks.json":
            tasks(f"{app_path}/configs/{sys.argv[i]}/tasks.json")
            print(f"'{sys.argv[i]}' tasks.json successfully installed", path)
        elif f == "settings.json":
            settings(f"{app_path}/configs/{sys.argv[i]}/settings.json", path)
            print(f"'{sys.argv[i]}' settings.json successfully installed")
        elif f == "c_cpp_properties.json":
            c_cpp_properties(f"{app_path}/configs/{sys.argv[i]}/c_cpp_properties.json", path)
            print(f"'{sys.argv[i]}' c_cpp_properties.json successfully installed")
    configs["configs"].append(sys.argv[i])
    with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
        vsccm.write(json.dumps(configs, ensure_ascii=False, indent=4))
    print(f"'{sys.argv[i]}' SUCCESSFULLY INSTALLED")

def install_configs_command(path: str, start: int) -> None: # command 'vsccm install {config_name}'
    if not os.path.exists(f"{path}"):
        os.mkdir(f"{path}")
    if not os.path.exists(f"{path}/.vscode"):
        os.mkdir(f"{path}/.vscode")
    if not os.path.exists(f"{path}/vsccm-lock.json"):
        with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
            vsccm.write('{"configs": []}')
    if isempty(f"{path}/vsccm-lock.json"):
        with open(f"{path}/vsccm-lock.json", 'w') as vsccm:
            vsccm.write('{"configs": []}')
    with open(f"{path}/vsccm-lock.json", 'r') as vsccm:
        configs: dict = json.loads(vsccm.read()) 
    for i in range(start, len(sys.argv)):
        if sys.argv[i].lower() not in configs["configs"]:  
            install_config(path, i)
        else:
            print(f"'{sys.argv[i]}' has already been installed")

def install_command(path: str) -> None: # command 'vsccm install'
    global app_path
    if os.path.exists(f"{path}/vsccm-lock.json"):
        if not os.path.exists(f"{path}/.vscode"):
            os.mkdir(f"{path}/.vscode")
        configs_list: list = []
        with open(f"{path}/vsccm-lock.json", 'r') as vsccm:
            configs_list = json.loads(vsccm.read())["configs"]
        if len(configs_list) > 0:
            for config in configs_list:
                try: 
                    files: list = list(filter(lambda file: os.path.isfile(f"{app_path}/configs/{config}/{file}"), os.listdir(f"{app_path}/configs/{config}")))
                    for f in files:
                        if f == "launch.json":
                            launch(f"{app_path}/configs/{config}/launch.json", path)
                            print(f"'{config}' launch.json successfully installed")
                        elif f == "tasks.json":
                            tasks(f"{app_path}/configs/{config}/tasks.json", path)
                            print(f"'{config}' tasks.json successfully installed")
                        elif f == "settings.json":
                            settings(f"{app_path}/configs/{config}/settings.json", path)
                            print(f"'{config}' settings.json successfully installed")
                        elif f == "c_cpp_properties.json":
                            c_cpp_properties(f"{app_path}/configs/{config}/c_cpp_properties.json", path)
                            print(f"'{config}' c_cpp_properties.json successfully installed")
                    print(f"'{config}' SUCCESSFULLY INSTALLED")
                except Exception:
                    print(f"'{config}' NOT FOUND")   
        else:
            print("There is no configs in you vsccm config file")
    else:
        print("There is no folder or vsccm config file")
# --------------------------------------------------------------

# main part ----------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) == 1: # 'vsccm'
        print("install — install config\nlist — list of installed configs\nremove — remove .vscode folder\nclear — clear configs")
    elif sys.argv[1] == "list" or sys.argv[1] == "l": 
        if len(sys.argv) > 2 and sys.argv[2][:13] == "--workfolder=": # 'vsccm list --workfolder='
            list_command(sys.argv[2][13:])
        elif len(sys.argv) > 2 and sys.argv[2][:12] == "-workfolder=": # 'vsccm list -workfolder='
            list_command(sys.argv[2][12:])
        else: # 'vsccm list'
            list_command(call_path)
    elif sys.argv[1] == "remove" or sys.argv[1] == "r": 
        if len(sys.argv) > 2 and sys.argv[2][:13] == "--workfolder=": # 'vsccm remove --workfolder='
            remove_command(sys.argv[2][13:])
        elif len(sys.argv) > 2 and sys.argv[2][:12] == "-workfolder=": # 'vsccm remove -workfolder='
            remove_command(sys.argv[2][12:])
        else: # 'vsccm remove'
            remove_command(call_path)
    elif sys.argv[1] == "clear" or sys.argv[1] == "c":
        if len(sys.argv) > 2 and sys.argv[2][:13] == "--workfolder=": # 'vsccm clear --workfolder='
            clear_command(sys.argv[2][13:])
        elif len(sys.argv) > 2 and sys.argv[2][:12] == "-workfolder=": # 'vsccm clear -workfolder='
            clear_command(sys.argv[2][12:])
        else: # 'vsccm clear'
            clear_command(call_path)
    elif sys.argv[1] == "install" or sys.argv[1] == "i": # 'vsccm install'
        if len(sys.argv) == 3:
            if sys.argv[2] == "list" or sys.argv[2] == "l": # 'vsccm install list'
                install_list_command()
            elif sys.argv[2][:13] == "--configfile=": # 'vsccm install --configfile='
                install_args_command(call_path, sys.argv[2][13:])
            elif sys.argv[2][:12] == "-configfile=": # 'vsccm install -configfile='
                install_args_command(call_path, sys.argv[2][12:])
            elif sys.argv[2][:13] == "--workfolder=": # 'vsccm install --workfolder='
                install_command(sys.argv[2][13:])
            elif sys.argv[2][:12] == "-workfolder=": # 'vsccm install -workfolder='
                install_command(sys.argv[2][12:])
            else: # 'vsccm install {config_name}'
                install_configs_command(call_path, 2)
        elif len(sys.argv) == 4:
            if sys.argv[2][:13] == "--workfolder=" and sys.argv[3][:13] == "--configfile=": # 'vsccm install --workfolder= --configfile='
                install_args_command(sys.argv[2][13:], sys.argv[3][13:])
            elif sys.argv[2][:12] == "-workfolder=" and sys.argv[3][:12] == "-configfile=": # 'vsccm install -workfolder= -configfile='
                install_args_command(sys.argv[2][12:], sys.argv[3][12:])
            elif sys.argv[3][:13] == "--workfolder=" and sys.argv[2][:13] == "--configfile=": # 'vsccm install --configfile= --workfolder='
                install_args_command(sys.argv[3][13:], sys.argv[2][13:])
            elif sys.argv[3][:13] == "-workfolder=" and sys.argv[2][:13] == "-configfile=": # 'vsccm install -configfile= -workfolder='
                install_args_command(sys.argv[3][12:], sys.argv[2][12:])
            else:
                if sys.argv[2][:13] == "--workfolder=": # 'vsccm install --workfolder= {config_name}'
                    install_configs_command(sys.argv[2][13:], 3)
                elif sys.argv[2][:12] == "-workfolder=": # 'vsccm install -workfolder= {config_name}'
                    install_configs_command(sys.argv[2][12:], 3)
                else: # 'vsccm install {config_name} {config_name}'
                    install_configs_command(call_path, 2)
        elif len(sys.argv) > 4:
            if sys.argv[2][:13] == "--workfolder=": # 'vsccm install --workfolder= {config_name}...'
                install_configs_command(sys.argv[2][13:], 3)
            elif sys.argv[2][:12] == "-workfolder=": # 'vsccm install -workfolder= {config_name}...'
                install_configs_command(sys.argv[2][12:], 3)
            else: # 'vsccm install {config_name}...'
                install_configs_command(call_path, 2)
        else: # 'vsccm install'
            install_command(call_path)
    else: # something went wrong
        print("Uncorrect arguments")
# --------------------------------------------------------------