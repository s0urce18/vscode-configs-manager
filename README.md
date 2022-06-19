# vscode-configs-manager

<img src="imgs/preview.png" width="300px">

**VSCCM**(VSCode config manager) — program for maganering VSCode configs

## Installation

Extract `base-build.zip` to any folder and add to PATH or extract to work folder. In `base-build.zip` included base configs for **Python**, **NodeJS**, **TypeScript**, **Go**, **G++**, **.NET** and **Rust**

If you don't need base configs download `vsccm.exe` and create your configs

## Creating configs

Create folder in `config` folder with name of your config and paste there files that your config need

## Using

`install` — install configs from `vsccm.json` file

`install --configfile={local path to vsccm.json file}` — install configs from `vsccm.json` file with giving path to it

`install {config name}` — install config

`install list` — show list of configs which you can install

`list` — list of installed configs

`remove` — remove .vscode folder

`clear` — clear configs
