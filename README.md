# Av1anStaxRipWrapper
Python wrapper script to use Av1an with StaxRip
 - Currently only the rav1e script is working

[INSTALL AND USAGE GUIDE (YouTube)](https://www.youtube.com/watch?v=lMfTwd0qDC8)

## Contents
- [Av1anStaxRipWrapper](#av1anstaxripwrapper)
  - [Contents](#contents)
  - [Usage](#usage)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Portable Installation](#portable-installation)
    - [Alternative Installation (install tools to system PATH)](#alternative-installation-install-tools-to-system-path)
  - [Command Line Options](#command-line-options)
  - [Automatic Thread Detection](#automatic-thread-detection)

## Usage
This script makes use of the Command Line option in StaxRip. There are some required arguments needed in the command that allows Av1an to work with StaxRip. Namely `-i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp"`. `-s "%startup_dir%"` is needed if you want a portable installation. Portable installation is described in more detail at the [Setup](#setup) section.

<img src="https://user-images.githubusercontent.com/1343896/209460663-fa6ac57b-ec77-48d7-b993-ba67bf0d56a1.png" alt="staxrip_image" width="500"/>

A good starting command would be:

```
"%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\VapourSynth\python.exe" "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapperRav1e.py" -s "%startup_dir%" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le --quantizer 60 --speed 6 --tiles 2 --threads 2 --photon-noise 2 --chroma-noise --sc-downscale-height 540
```
Everything after the `-t` parameter will affect the encoding parameters (either Av1an or rav1e). Refer to [Command Line Options](#command-line-options) section for more information.

## Requirements
- [ffmpeg](https://ffmpeg.org/download.html) (with shared libraries) (Av1an requirement)
- [rav1e](https://github.com/xiph/rav1e/releases)
- [StaxRip](https://github.com/staxrip/staxrip/releases)

This script also requires the `psutil` module in Python to automatically detect CPU core counts to pass into av1an.
 - You can run with the `--disable-automatic-thread-detection` flag to disable this feature and requirement

## Setup
### Portable Installation
Since Av1an requires `ffmpeg`, `rav1e`, `VapourSynth` to be in PATH, this script can automatically help you add important folders (from StaxRip) temporarily to PATH when it's being run (for portable installation). In this way, your actual system PATH is not affected when running Av1an. However, this means that you need to install the tools in specific folders in StaxRip as the wrapper script looks for them there.

Portable mode is enabled when the `-s` flag is used with the StaxRip startup directory.

1. Ensure encoders, Av1an and the wrapper script are extracted in the right directories
 - Av1an: `StaxRip\Apps\Encoders\Av1an`
 - rav1e: `StaxRip\Apps\Encoders\rav1e`
 - FFMPEG: `StaxRip\Apps\Encoders\Av1an` (moving it to an `ffmpeg` folder would interfere with StaxRip's own ffmpeg)
 - Wrapper Script: `StaxRip\Apps\Encoders\Av1anStaxRipWrapper`
2. Run the `setup_py_vp_environment.bat` script from the Av1anStaxRipWrapper folder to install required Python modules and VapourSynth plugins
3. Use the **Command Line** encoder profile to create an Av1an Encoder Profile
<img src="https://user-images.githubusercontent.com/1343896/209458682-9e42b62f-22d2-4efb-a84d-47da50c1921f.png" alt="staxrip_image" width="200"/>
<img src="https://user-images.githubusercontent.com/1343896/209460663-fa6ac57b-ec77-48d7-b993-ba67bf0d56a1.png" alt="staxrip_image" width="500"/>

Good starting command: (make sure to change **Output File Type** to `mkv`)
```
"%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\VapourSynth\python.exe" "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapperRav1e.py" -s "%startup_dir%" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le --quantizer 60 --speed 6 --tiles 2 --threads 2 --photon-noise 2 --chroma-noise --sc-downscale-height 540
```

4. Save this Encoder Profile with the name `AV1 | av1an rav1e`, and it will appear in the AV1 drop-down menu.
![image](https://user-images.githubusercontent.com/1343896/209458707-bca3edda-36af-4d3d-b4a5-899160a5e8d9.png)


### Alternative Installation (install tools to system PATH)
Basically, just make sure `Av1an`, `ffmpeg`, `rav1e`, `Python`, `VapourSynth` are all accessible from PATH and follow the steps above from Step 2.

The command in StaxRip used is\
`python "%startup_dir%\Apps\Encoders\Av1anStaxRipWrapper\Av1anStaxRipWrapperRav1e.py" -i "%source_file%" -o "%encoder_out_file%" -t "%temp_dir%av1an_temp" --pix-format yuv420p10le --quantizer 60 --speed 6 --tiles 2 --threads 2 --photon-noise 2 --chroma-noise --sc-downscale-height 540`

## Command Line Options
```

options:
  -h, --help            show this help message and exit
  -i INPUT              Input File (for StaxRip)
  -o OUTPUT             Output File (for StaxRip)
  -t TEMPDIR            Temp Directory (for StaxRip)
  -s STAXRIP_STARTUP_DIR, --staxrip-startup-dir STAXRIP_STARTUP_DIR
                        Specify StaxRip Startup Directory so that the wrapper script will automatically 
                        add important folders to PATH for av1an to detect (only needed for portable installations)

# Av1an parameters
  --photon-noise PHOTON_NOISE
                        Generates a photon noise table and applies it using grain synthesis 
                        [strength: 0-64] (disabled by default) (Av1an parameter)
  --chroma-noise        Adds chroma grain synthesis to the grain table generated by `--photon-noise`. 
                        (Default: false) (Av1an parameter)
  --sc-downscale-height SC_DOWNSCALE_HEIGHT
                        Optional downscaling for scene detection. By default, no downscaling is performed. (Av1an parameter)

# Threading parameters (Using any of these would disable the wrapper's Automatic Thread Detection feature)
  --workers WORKERS     Number of workers to spawn [0 = automatic] (Av1an Paramter)
  --set-thread-affinity SET_THREAD_AFFINITY
                        Pin each worker to a specific set of threads of this size (disabled by default) (Av1an parameter)
  --disable-automatic-thread-detection
                        Disable the wrapper's automatic thread detection (Wrapper script flag)

# rav1e parameters
  --quantizer QUANTIZER
                        Quantizer (0-255), smaller values are higher quality (default: 100) (rav1e parameter)
  --speed SPEED         Speed level (0 is best quality, 10 is fastest) Speeds 10 and 0 are extremes and are generally 
                        not recommended [default: 6] (rav1e parameter)
  --tiles TILES         Number of tiles. Tile-cols and tile-rows are overridden so that the video has at least this 
                        many tiles (rav1e parameter)
  --threads THREADS     Set the threadpool size. If 0, will use the number of logical CPUs. rav1e will use up to this 
                        many threads. Additional tiles may be needed to increase thread utilization
                        [default: 0] (rav1e parameter)
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
