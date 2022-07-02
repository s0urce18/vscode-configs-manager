# vscode-configs-manager

<img src="imgs/preview.png" width="300px">

**VSCCM**(VSCode config manager) — program for maganering VSCode configs

VSCode extension: https://marketplace.visualstudio.com/items?itemName=s0urcecom.vscode-configs-manager-extension

## Installation

Extract `base-build.zip` to any folder and add to PATH or extract to work folder. In `base-build.zip` included base configs for **Python**, **NodeJS**, **TypeScript**, **Go**, **G++**, **.NET** and **Rust**

If you don't need base configs download `vsccm.exe` and create your configs

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
