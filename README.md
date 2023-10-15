# Av1anStaxRipWrapper
Python wrapper script to use Av1an with StaxRip

[Av1anStaxRipWrapperRav1e](README_RAV1E.md) (rav1e specialized script README)\
[INSTALL AND USAGE GUIDE (YouTube)](https://youtu.be/a7IPQcNVwTY)

## Contents
- [Av1anStaxRipWrapper](#av1anstaxripwrapper)
  - [Contents](#contents)
  - [Usage](#usage)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Portable Installation (Recommended)](#portable-installation-recommended)
    - [Alternative Installation (install tools to system PATH)](#alternative-installation-install-tools-to-system-path)
  - [Command Line Options](#command-line-options)
  - [Automatic Thread Detection](#automatic-thread-detection)
  - [Override Worker Count and Threads Per Local Machine](#override-worker-count-and-threads-per-local-machine)
    - [Setting the override worker count](#setting-the-override-worker-count)
    - [Check to see if it's working](#check-to-see-if-its-working)

## Usage
This script makes use of the Command Line option in StaxRip. There are some required arguments needed in the command that allows Av1an to work with StaxRip. Namely `-i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp"`. `-s "%startup_dir%"` is needed if you want a portable installation. Portable installation is described in more detail at the [Setup](#setup) section.

<img src="https://user-images.githubusercontent.com/1343896/209460663-fa6ac57b-ec77-48d7-b993-ba67bf0d56a1.png" alt="staxrip_image" width="500"/>

A good starting command would be:

```
"%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\VapourSynth\python.exe" "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapper.py" -s "%startup_dir%" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le -e rav1e --photon-noise 2 --chroma-noise --sc-downscale-height 540 -v "--quantizer 60 --speed 6 --tiles 2 --threads 2"
```
Everything after the `-t` parameter will affect the encoding parameters (either Av1an or the selected encoder). Refer to [Command Line Options](#command-line-options) section for more information.

This starting command uses the rav1e encoder and uses the encoding parameters passed in by the argument `-v`.

## Requirements
- [ffmpeg](https://ffmpeg.org/download.html) (with shared libraries) (Av1an requirement)
- [aomenc](https://aomedia.googlesource.com/aom/) or
- [rav1e](https://github.com/xiph/rav1e/releases) or
- [SVT-AV1](https://gitlab.com/AOMediaCodec/SVT-AV1)
- [StaxRip](https://github.com/staxrip/staxrip/releases)

This script also requires the `psutil` module in Python to automatically detect CPU core counts to pass into av1an.
 - You can run with the `--disable-automatic-thread-detection` flag to disable this feature and requirement

## Setup
### Portable Installation (Recommended)
Since Av1an requires `ffmpeg`, `aomenc` or `rav1e` or `SVT-AV1`, `VapourSynth` to be in PATH, this script can automatically help you add important folders (from StaxRip) temporarily to PATH when it's being run (for portable installation). In this way, your actual system PATH is not affected when running Av1an. However, this means that you need to install the tools in specific folders in StaxRip as the wrapper script looks for them there.

Portable mode is enabled when the `-s` flag is used with the StaxRip startup directory.

1. Clone this repository (or download the files) into `StaxRip\Apps\Encoders\Av1anStaxRipWrapper`

2. Ensure encoders, Av1an and the wrapper script are extracted in the right directories
 - Av1an: `StaxRip\Apps\Encoders\Av1an`
 - aomenc: `StaxRip\Apps\Encoders\aomenc`
 - rav1e: `StaxRip\Apps\Encoders\rav1e`
 - SVT-AV1: `StaxRip\Apps\Encoders\SVT-AV1`
 - FFMPEG: `StaxRip\Apps\Encoders\Av1an` (moving it to an `ffmpeg` folder would interfere with StaxRip's own ffmpeg)
 - Wrapper Script: `StaxRip\Apps\Encoders\Av1anStaxRipWrapper`
3. Run the `setup_py_vp_environment.bat` script from the Av1anStaxRipWrapper folder to install required Python modules and VapourSynth plugins
4. Use the **Command Line** encoder profile to create an Av1an Encoder Profile
<img src="https://user-images.githubusercontent.com/1343896/209458682-9e42b62f-22d2-4efb-a84d-47da50c1921f.png" alt="staxrip_image" width="200"/>
<img src="https://user-images.githubusercontent.com/1343896/209460663-fa6ac57b-ec77-48d7-b993-ba67bf0d56a1.png" alt="staxrip_image" width="500"/>

Good starting command: (make sure to change **Output File Type** to `mkv`)
```
"%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\VapourSynth\python.exe" "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapper.py" -s "%startup_dir%" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le -e rav1e --photon-noise 2 --chroma-noise --sc-downscale-height 540 -v "--quantizer 60 --speed 6 --tiles 2 --threads 2"
```

5. Save this Encoder Profile with the name `AV1 | av1an`, and it will appear in the AV1 drop-down menu.
![image](https://user-images.githubusercontent.com/1343896/209458707-bca3edda-36af-4d3d-b4a5-899160a5e8d9.png)


### Alternative Installation (install tools to system PATH)
Basically, just make sure `Av1an`, `ffmpeg`, `aomenc`, `rav1e`, `SVT-AV1`, `Python`, `VapourSynth` are all accessible from PATH and follow the steps above from Step 2.

The command in StaxRip used is\
`python "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapperRav1e.py" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le -e rav1e --photon-noise 2 --chroma-noise --sc-downscale-height 540 -v "--quantizer 60 --speed 6 --tiles 2 --threads 2"`

## Command Line Options
```
options:
Av1an wrapper for StaxRip

optional arguments:
  -h, --help            show this help message and exit
  --version             Print Av1an, ffmpeg and the encoders' versions
  -i INPUT              Input File (for StaxRip)
  -o OUTPUT             Output File (for StaxRip)
  -t TEMPDIR            Temp Directory (for StaxRip)
  -s STAXRIP_STARTUP_DIR, --staxrip-startup-dir STAXRIP_STARTUP_DIR
                        Specify StaxRip Startup Directory so that the wrapper script will automatically add important
                        folders to PATH for av1an to detect (only needed for portable installations)

# Av1an parameters
  -e ENCODER, --encoder ENCODER
                        Video encoder to use. [default: aom][possible values: aom, rav1e, vpx, svt-av1, x264, x265]
  -v ENCODER_ARGS, --video-params ENCODER_ARGS
                        Arguments passed to video encoder
  -a OTHER_ARGS, --other-args OTHER_ARGS
                        Other Av1an arguments
  -f FFMPEG_OPTIONS, --ffmpeg FFMPEG_OPTIONS
                        FFmpeg filter options
  --photon-noise PHOTON_NOISE
                        Generates a photon noise table and applies it using grain synthesis [strength: 0-64] (disabled
                        by default) (Av1an parameter)
  --chroma-noise        Adds chroma grain synthesis to the grain table generated by `--photon-noise`. (Default: false)
                        (Av1an parameter)
  --sc-downscale-height SC_DOWNSCALE_HEIGHT
                        Optional downscaling for scene detection. By default, no downscaling is performed. (Av1an
                        parameter)
  --pix-format PIX_FORMAT
                        FFmpeg pixel format

# Threading parameters (Using any of these would disable the wrapper's Automatic Thread Detection feature)
  --workers WORKERS     Number of workers to spawn [0 = automatic] (Av1an Paramter)
  --set-thread-affinity SET_THREAD_AFFINITY
                        Pin each worker to a specific set of threads of this size (disabled by default) (Av1an
                        parameter)
  --disable-automatic-thread-detection
                        Disable the wrapper's automatic thread detection
  --set-worker-override
                        Set the override workers count and thread affinity count for local computer
```

## Automatic Thread Detection
In my testing, I found that I get the best utilization and encoding speeds when creating the same number of workers as the number of physical cores available in your system. Along with having the number of threads per worker be 2 if your system supports hyperthreading/SMT and 1 if your system does not.

With automatic thread detection, the wrapper script will automatically detect and pass in the relevant parameters to Av1an. For example,

```
Ryzen 7 5800X
  Physical Cores: 8 cores
  Logical Cores: 16 cores
  Hyperthreading/SMT: Enabled
  Threading Parameters: --workers 8 --set-thread--affinity 2
  
Intel i5-6600K
  Physical Cores: 4 cores
  Logical Cores: 4 cores
  Hyperthreading/SMT: Disabled
  Threading Parameters: --workers 4 --set-thread-affinity 1
```

If your system uses an Intel 12th Gen chip and above (with the new hybrid architecture with P-cores and E-cores), this feature is disabled.

If you do not want to use this feature, you can use the `--disable-automatic-thread-detection` flag or any of the Threading parameters under [Command Line Options](#command-line-options). Using any the Threading parameters would disable this feature.

## Override Worker Count and Threads Per Local Machine
When using StaxRip in a networked environment (where multiple computers access the same StaxRip install), you might want to override the Automatic Thread Detection feature for some computers, but not affect other machines. This feature allows you to do so without modifying the command line option, by storing a configuration file in a local computer.

### Setting the override worker count
To set the override feature, run the script with the `--set-worker-override` flag.
```
python Av1anStaxRipWrapper.py --set-worker-override
```
Follow the instructions shown in the cmd window and the script should store a configuration file in this location. `%userprofile%\Av1anStaxRipWrapper\override-workers.json`

### Check to see if it's working
The next time a job is being run, the script will show in its logs that the override file is found. For example:
```
=================================================
Av1anStaxRipWrapper
https://github.com/Kidsnd274/Av1anStaxRipWrapper
=================================================
[INFO] Found override-workers.json
[INFO] Overriding CPU Workers = 4 and CPU Thread Affinity = 2
[INFO] Automatic Thread Detection Disabled
THREADING INFORMATION:
  Automatic Thread Detection: DISABLED
Starting av1an... Check new console window for progress
```