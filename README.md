# vscode-configs-manager

<img src="imgs/preview.png" width="300px">

**VSCCM**(VSCode config manager) — program for maganering VSCode configs

VSCode extension: https://marketplace.visualstudio.com/items?itemName=s0urcecom.vscode-configs-manager-extension

## Installation

All builds are in folder `builds`. There you can choose your OS and get application file, configs or base build zip archive

In base build archive are included configs(from folder `configs`) and application file

If you need base build, you need to extract archive where you need and add this folder to PATH variable

If you don't need base build, you can use application file singly

## Creating configs

Create folder in `config` folder with name of your config and paste there files that your config need

## Using

`install` — install configs from `vsccm.json` file

`install --configfile={local path to vsccm.json file}` — install configs from `vsccm.json` file with giving path to it

`install --workfolder={path to workfolder}` — install configs from `vsccm.json` file with giving path to workfolder

`install {config name}` — install config

`install --workfolder={path to workfolder} {config name}` — install config in given workfolder

`install list` — show list of configs which you can install

`list` — list of installed configs

`list --workfolder={path to workfolder}` — list of installed configs in workfolder

`remove` — remove .vscode folder

`remove --workfolder={path to workfolder}` — remove .vscode folder in workfolder

`clear` — clear configs

`clear --workfolder={path to workfolder}` — clear configs in workfolder
