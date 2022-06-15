import sys
import json
import os
import shutil

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
elif __file__:
    app_path = os.path.dirname(__file__)
app_path = app_path.replace("\\", "/")
call_path = os.getcwd().replace("\\", "/")

def launch(path: str) -> None:
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{call_path}/.vscode/launch.json"):
        with open(f"{call_path}/.vscode/launch.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"version": "2.0.0", "configurations": []}')
    k = False
    with open(f"{call_path}/.vscode/launch.json", 'r') as vsccm:
        if vsccm.read() == '':
           k = True
    if k:
        with open(f"{call_path}/.vscode/launch.json", 'w') as vsccm:
            vsccm.write('{"version": "2.0.0", "configurations": []}')
    with open(f"{call_path}/.vscode/launch.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict = json.loads(vsc_file.read())
    try:
        for c in file_dict["configurations"]:
            vsc_file_dict["configurations"].append(c)
    except:
        print("Something wrong with a file")
        return
    vsc_config_list = []
    for x in vsc_file_dict["configurations"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["configurations"] = vsc_config_list
    with open(f"{call_path}/.vscode/launch.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def tasks(path: str) -> None:
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{call_path}/.vscode/tasks.json"):
        with open(f"{call_path}/.vscode/tasks.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"version": "2.0.0", "tasks": []}')
    with open(f"{call_path}/.vscode/tasks.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict = json.loads(vsc_file.read())
    k = False
    with open(f"{call_path}/.vscode/tasks.json", 'r') as vsccm:
        if vsccm.read() == '':
           k = True
    if k:
        with open(f"{call_path}/.vscode/tasks.json", 'w') as vsccm:
            vsccm.write('{"version": "2.0.0", "tasks": []}')
    try:
        for c in file_dict["tasks"]:
            vsc_file_dict["tasks"].append(c)
    except:
        print("Something wrong with a file")
        return
    vsc_config_list = []
    for x in vsc_file_dict["tasks"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["tasks"] = vsc_config_list
    with open(f"{call_path}/.vscode/tasks.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def settings(path: str) -> None:
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{call_path}/.vscode/settings.json"):
        with open(f"{call_path}/.vscode/settings.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{}')
    with open(f"{call_path}/.vscode/settings.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict = json.loads(vsc_file.read())
    k = False
    with open(f"{call_path}/.vscode/settings.json", 'r') as vsccm:
        if vsccm.read() == '':
           k = True
    if k:
        with open(f"{call_path}/.vscode/settings.json", 'w') as vsccm:
            vsccm.write('{}')
    try:
        for c in file_dict:
            vsc_file_dict[c] = file_dict[c]
    except:
        print("Something wrong with a file")
        return
    with open(f"{call_path}/.vscode/settings.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

def c_cpp_properties(path: str):
    with open(path, 'r', encoding="utf-8") as file:
        file_dict: dict = json.loads(file.read())
    if not os.path.exists(f"{call_path}/.vscode/c_cpp_properties.json"):
        with open(f"{call_path}/.vscode/c_cpp_properties.json", 'w', encoding="utf-8") as vsccm:
            vsccm.write('{"configurations": []}')
    k = False
    with open(f"{call_path}/.vscode/c_cpp_properties.json", 'r') as vsccm:
        if vsccm.read() == '':
           k = True
    if k:
        with open(f"{call_path}/.vscode/c_cpp_properties.json", 'w') as vsccm:
            vsccm.write('{"configurations": []}')
    with open(f"{call_path}/.vscode/c_cpp_properties.json", 'r', encoding="utf-8") as vsc_file:
        vsc_file_dict = json.loads(vsc_file.read())
    try:
        for c in file_dict["configurations"]:
            vsc_file_dict["configurations"].append(c)
    except:
        print("Something wrong with a file")
        return
    vsc_config_list = []
    for x in vsc_file_dict["configurations"]:
        if x not in vsc_config_list:
            vsc_config_list.append(x)
    vsc_file_dict["configurations"] = vsc_config_list
    with open(f"{call_path}/.vscode/c_cpp_properties.json", 'w', encoding="utf-8") as vsc_file:
        vsc_file.write(json.dumps(vsc_file_dict, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("install — install config\nlist — list of installed configs\nremove — remove .vscode folder\nclear — clear configs")
    elif sys.argv[1] == "list" or sys.argv[1] == "l":
        if not os.path.exists(f"{call_path}/.vscode") or not os.path.exists(f"{call_path}/.vscode/vsccm.json"):
            print("You haven't installed any configs")
        else:
            with open(f"{call_path}/.vscode/vsccm.json") as vsccm:
                vsccm_dict: dict = json.loads(vsccm.read())
            print("Installed configs:")
            for cfg in vsccm_dict["configs"]:
                print(f"|-{cfg}")
    elif sys.argv[1] == "remove" or sys.argv[1] == "r":
        if os.path.exists(f"{call_path}/.vscode"):
            shutil.rmtree(f"{call_path}/.vscode")
        print("Directory configs removed")
    elif sys.argv[1] == "clear" or sys.argv[1] == "c":
        if os.path.exists(f"{call_path}/.vscode"):
            shutil.rmtree(f"{call_path}/.vscode")
            os.mkdir(f"{call_path}/.vscode")
        if os.path.exists(f"{call_path}/.vscode/vsccm.json"):
            vsccm = open(f"{call_path}/.vscode/vsccm.json", 'w')
            vsccm.close()
        print("Directory configs cleared")
    elif sys.argv[1] == "install" or sys.argv[1] == "i":
        if len(sys.argv) > 2:
            if sys.argv[2] == "list" or sys.argv[2] == "l":
                print("Your configs:")
                for config in os.listdir(f"{app_path}/configs/"):
                    if os.path.isdir(f"{app_path}/configs/{config}"):
                        print(f"|-{config}")
                        for file in os.listdir(f"{app_path}/configs/{config}"):
                            if os.path.isfile(f"{app_path}/configs/{config}/{file}"):
                                print(f"  |-{file}")
            else:
                if not os.path.exists(f"{call_path}/.vscode"):
                    os.mkdir(f"{call_path}/.vscode")
                if not os.path.exists(f"{call_path}/.vscode/vsccm.json"):
                    with open(f"{call_path}/.vscode/vsccm.json", 'w') as vsccm:
                        vsccm.write('{"configs": []}')
                k = False
                with open(f"{call_path}/.vscode/vsccm.json", 'r') as vsccm:
                    if vsccm.read() == '':
                        k = True
                if k:
                    with open(f"{call_path}/.vscode/vsccm.json", 'w') as vsccm:
                        vsccm.write('{"configs": []}')
                with open(f"{call_path}/.vscode/vsccm.json", 'r') as vsccm:
                    configs: dict = json.loads(vsccm.read()) 
                for i in range(2, len(sys.argv)):
                    if sys.argv[i].lower() not in configs["configs"]:  
                        files: list = list(filter(lambda file: os.path.isfile(f"{app_path}/configs/{sys.argv[i]}/{file}"), os.listdir(f"{app_path}/configs/{sys.argv[i]}")))
                        for f in files:
                            if f == "launch.json":
                                launch(f"{app_path}/configs/{sys.argv[i]}/launch.json")
                                print(f"'{sys.argv[i]}' launch.json successfully installed")
                            elif f == "tasks.json":
                                tasks(f"{app_path}/configs/{sys.argv[i]}/tasks.json")
                                print(f"'{sys.argv[i]}' tasks.json successfully installed")
                            elif f == "settings.json":
                                settings(f"{app_path}/configs/{sys.argv[i]}/settings.json")
                                print(f"'{sys.argv[i]}' settings.json successfully installed")
                            elif f == "c_cpp_properties.json":
                                c_cpp_properties(f"{app_path}/configs/{sys.argv[i]}/c_cpp_properties.json")
                                print(f"'{sys.argv[i]}' c_cpp_properties.json successfully installed")
                        configs["configs"].append(sys.argv[i])
                        with open(f"{call_path}/.vscode/vsccm.json", 'w') as vsccm:
                            vsccm.write(json.dumps(configs, ensure_ascii=False, indent=4))
                        print(f"'{sys.argv[i]}' SUCCESSFULLY INSTALLED")
                    else:
                        print(f"'{sys.argv[i]}' has already been installed")
        else:
            if os.path.exists(f"{call_path}/.vscode") and os.path.exists(f"{call_path}/.vscode/vsccm.json"):
                configs_list = []
                with open(f"{call_path}/.vscode/vsccm.json", 'r') as vsccm:
                    configs_list = json.loads(vsccm.read())["configs"]
                if len(configs_list) > 0:
                    for config in configs_list:
                        try:
                            with open(f"{call_path}/.vscode/vsccm.json", 'r') as vsccm:
                                figs: dict = json.loads(vsccm.read())   
                            files: list = list(filter(lambda file: os.path.isfile(f"{app_path}/configs/{config}/{file}"), os.listdir(f"{app_path}/configs/{config}")))
                            for f in files:
                                if f == "launch.json":
                                    launch(f"{app_path}/configs/{config}/launch.json")
                                    print(f"'{config}' launch.json successfully installed")
                                elif f == "tasks.json":
                                    tasks(f"{app_path}/configs/{config}/tasks.json")
                                    print(f"'{config}' tasks.json successfully installed")
                                elif f == "settings.json":
                                    settings(f"{app_path}/configs/{config}/settings.json")
                                    print(f"'{config}' settings.json successfully installed")
                                elif f == "c_cpp_properties.json":
                                    c_cpp_properties(f"{app_path}/configs/{config}/c_cpp_properties.json")
                                    print(f"'{config}' c_cpp_properties.json successfully installed")
                            print(f"'{config}' SUCCESSFULLY INSTALLED")
                        except:
                            print(f"'{config}' NOT FOUND")   
                else:
                    print("There is no configs in you vsccm config file")
            else:
                print("There is no folder or vsccm config file")
    else:
        print("Uncorrect arguments")