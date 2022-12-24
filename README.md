# Av1anStaxRipWrapper
Python wrapper script to use Av1an with StaxRip
 - Currently only the rav1e script is working

## Contents
- [Usage](#usage)
- [Requirements](#requirements)
- [Setup](#setup)
- [Command Line Options](#command-line-options)

## Usage
This script makes use of the Command Line option in StaxRip. There are some required arguments needed in the command that allows Av1an to work with StaxRip. Namely `-i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp"`. `-s "%startup_dir%"` is needed if you want a portable installation. Portable installation is described in more detail at the [Setup](#setup) section.

<img src="https://user-images.githubusercontent.com/1343896/209447195-c6ffb08c-bb6c-4792-a1cd-a09422c01156.png" alt="staxrip_image" width="500"/>

A good starting command would be:

```
"%app_path:python%" "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapperRav1e.py" -s "%startup_dir%" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --quantizer 60 --speed 6 --tiles 2 --threads 2 --photon-noise 2 --chroma-noise --sc-downscale-height 540
```
Everything after the `-t` parameter will affect the encoding parameters (either Av1an or rav1e). Refer to [Command Line Options](#command-line-options) section for more information.

## Requirements
- ffmpeg (with shared libraries) (Av1an requirement)
- [rav1e](https://github.com/xiph/rav1e/releases)
- StaxRip

Since Av1an requires `ffmpeg`, `rav1e` to be in PATH, this script can automatically help you add important folders to PATH when it's being run (for a more portable installation).

This script also requires the `psutil` module in Python to automatically detect CPU core counts to pass into av1an.
 - You can run with the `--disable-automatic-thread-detection` flag to disable this

## Setup

## Command Line Options
