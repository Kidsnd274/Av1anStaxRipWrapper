import argparse
import os
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

# This script allows the usage of any encoders supported by Av1an.
# Use the -e flag to specify the encoder and make sure .exe is in the specific folders. https://github.com/Kidsnd274/Av1anStaxRipWrapper


# Developer Notes:
# Add a check to see what encoders are available. Make a nice opening message saying
# Av1anStaxRip, Supported Encoders....
# FileNotFoundError is the error when using subprocess.run
# TODO: Allow separate override for workers and affinity
# TODO: Force close av1an when StaxRip terminates the script


# Functions
def add_argument(curr, new):
    return_string = curr
    if curr == "":
        return_string = new
    else:
        return_string += (" " + new)
    return return_string

def set_path(path):
    staxrip_path = pathlib.Path(path)
    av1an_path = staxrip_path / "Apps" / "Encoders" / "Av1an"
    aomenc_path = staxrip_path / "Apps" / "Encoders" / "aomenc"
    rav1e_path = staxrip_path / "Apps" / "Encoders" / "rav1e"
    svtav1_path = staxrip_path / "Apps" / "Encoders" / "SVT-AV1"
    svtav1_path2 = staxrip_path / "Apps" / "Encoders" / "SvtAv1EncApp"
    x264_path = staxrip_path / "Apps" / "Encoders" / "x264"
    x265_path = staxrip_path / "Apps" / "Encoders" / "x265"
    vp_path = staxrip_path / "Apps" / "Encoders" / "Av1anStaxRipWrapper" / "VapourSynth"
    mkvmerge_path = staxrip_path / "Apps" / "Support" / "MKVToolNix"
    environ = os.environ
    environ["PATH"] = f"{str(av1an_path)};{str(aomenc_path)};{str(rav1e_path)};{str(svtav1_path)};{str(svtav1_path2)};{str(x264_path)};{str(x265_path)};{str(vp_path)};{str(mkvmerge_path)};{environ['PATH']}"
    return environ

def print_welcome():
    print("=================================================")
    print("Av1anStaxRipWrapper")
    print("https://github.com/Kidsnd274/Av1anStaxRipWrapper")
    print("=================================================")
    print("")

def print_version(parser_args):
    if parser_args.staxrip_startup_dir is not None:
        my_env = set_path(parser_args.staxrip_startup_dir)
    else:
        my_env = os.environ
    try:
        subprocess.run("ffmpeg -version", shell=False, env=my_env)
    except FileNotFoundError:
        print("ffmpeg not found!")
    print("\n--------------------------------\n")
    try:
        subprocess.run("av1an --version", shell=False, env=my_env)
    except FileNotFoundError:
        print("Av1an not found!")
    print("\n--------------------------------\n")
    try:
        aomenc_process = subprocess.Popen("aomenc --help", shell=False, stdout=subprocess.PIPE)
        out, err = aomenc_process.communicate()
        out = out.decode("utf-8")
        for line in out.splitlines()[-6:-3]:
            print(line)
    except FileNotFoundError:
        print("aomenc not found!")
    print("\n--------------------------------\n")
    try:
        subprocess.run("rav1e --version", shell=False, env=my_env)
    except FileNotFoundError:
        print("rav1e not found!")
    print("\n--------------------------------\n")
    try:
        subprocess.run("SvtAv1EncApp", shell=False, env=my_env)
    except FileNotFoundError:
        print("SvtAv1EncApp not found!")
    print("\n--------------------------------\n")
    exit(0)
    
def get_worker_override():
    # Check for override-workers.json
    # eg. cpu_workers = 2, cpu_thread_affinity = 2
    local_app_data_path = pathlib.Path(str(os.getenv('LOCALAPPDATA')))
    config_path = local_app_data_path / "Av1anStaxRipWrapper" / "override-workers.json"
    if config_path.is_file():
        print("[INFO] Found override-workers.json")
        import json
        try:
            with config_path.open() as f:
                config = json.load(f)
                workers = config.get('cpu_workers')
                affinity = config.get('cpu_thread_affinity')
                if workers is None or affinity is None:
                    raise KeyError("[ERROR] override-workers.json is does not contain cpu_workers or cpu_thread_affinity")
                if not isinstance(workers, int) or not isinstance(affinity, int):
                    raise ValueError("[ERROR] override-workers.json is not formatted correctly")
                print(f"[INFO] Overriding CPU Workers = {str(workers)} and CPU Thread Affinity = {str(affinity)}")
                return (True, workers, affinity)
        except Exception as error:
            print("[ERROR] Failed to read override-workers.json. Skipping...")
            print(error)
    return (False, 0, 0)

def set_worker_override(): # Function to create override-workers.json
    print("Setting override workers and thread affinity for local computer...")
    print("")
    print("How many workers do you want to spawn? (Put 0 for disabled)")
    while True:
        workers = input("cpu_workers = ")
        try:
            workers_int = int(workers)
            if workers_int < 0:
                raise ValueError
        except ValueError:
            print("Invalid input, please enter a positive number")
            continue
        else:
            break
    print("How many threads do you want to pin each worker to? (Put 0 for disabled)")
    while True:
        affinity = input("cpu_thread_affinity = ")
        try:
            affinity_int = int(affinity)
            if affinity_int < 0:
                raise ValueError
        except ValueError:
            print("Invalid input, please enter a positive number")
            continue
        else:
            break
    
    config = {}
    if workers_int != 0:
        config['cpu_workers'] = workers_int
    if affinity_int != 0:
        config['cpu_thread_affinity'] = affinity_int
    
    import json
    local_app_data_path = pathlib.Path(str(os.getenv('LOCALAPPDATA')))
    config_path = local_app_data_path / "Av1anStaxRipWrapper" / "override-workers.json"
    
    # Creating proper folders and files
    config_path.parent.mkdir(parents=False, exist_ok=True)
    config_path.touch(exist_ok=True)
    with config_path.open('w') as f:
        json.dump(config, f, indent=4)
    print(f"Successfully written to {str(config_path)}")
    exit()

# Command Line Arguments
parser = argparse.ArgumentParser(description="Av1an wrapper for StaxRip")

parser.add_argument('--version', action='store_true', help="Print Av1an, ffmpeg and the encoders' versions")
parser.add_argument('-i', dest="input", type=str, help="Input File (for StaxRip)")
parser.add_argument('-o', dest="output", type=str, help="Output File (for StaxRip)")
parser.add_argument('-t', dest="tempdir", type=str, help="Temp Directory (for StaxRip)")
parser.add_argument('-s', '--staxrip-startup-dir', dest="staxrip_startup_dir", type=str, required=False, help="Specify StaxRip Startup Directory so that the wrapper script will automatically add important folders to PATH for av1an to detect (only needed for portable installations)")
parser.add_argument('-e', '--encoder', type=str, required=False, help="Video encoder to use. [default: aom][possible values: aom, rav1e, vpx, svt-av1, x264, x265]")
parser.add_argument('-v', '--video-params', dest="encoder_args", type=str, required=False, help="Arguments passed to video encoder")
parser.add_argument('-a', '--other-args', dest="other_args", type=str, required=False, help="Other Av1an arguments")
parser.add_argument('-f', '--ffmpeg', dest="ffmpeg_options", type=str, required=False, help="FFmpeg filter options")
parser.add_argument('--photon-noise', dest="photon_noise", type=str, required=False, help="Generates a photon noise table and applies it using grain synthesis [strength: 0-64] (disabled by default) (Av1an parameter)")
parser.add_argument('--chroma-noise', dest="chroma_noise", action='store_true', help="Adds chroma grain synthesis to the grain table generated by `--photon-noise`. (Default: false) (Av1an parameter)")
parser.add_argument('--sc-downscale-height', dest="sc_downscale_height", type=str, required=False, help="Optional downscaling for scene detection. By default, no downscaling is performed. (Av1an parameter)")
parser.add_argument('--pix-format', dest="pix_format", type=str, required=False, help="FFmpeg pixel format")
# Threading Arguments (do not specify these commands if you want to use Automatic Thread Detection)
parser.add_argument('--workers', type=str, required=False, help="Number of workers to spawn [0 = automatic] (Av1an Paramter)")
parser.add_argument('--set-thread-affinity', dest="set_thread_affinity", type=str, required=False, help="Pin each worker to a specific set of threads of this size (disabled by default) (Av1an parameter)")
parser.add_argument('--disable-automatic-thread-detection', dest="disable_automatic_thread_detection", action='store_true', help="Disable the wrapper's automatic thread detection")
parser.add_argument('--set-worker-override', dest="override_mode", action='store_true', help="Set the override workers count and thread affinity count for local computer")
parser_args = parser.parse_args()

print_welcome()

if parser_args.override_mode:
    set_worker_override()
    exit()

if parser_args.version:
    print_version(parser_args)

if parser_args.input is None or parser_args.output is None or parser_args.tempdir is None:
    print("The arguments, -i, -o, -t are required to work!")
    print("Run --help for more information")
    exit(1)

input_file = parser_args.input
output_file = parser_args.output
tempdir = parser_args.tempdir

# Automatic Thread Detection
thread_detection = False
override_workers, cpu_workers, cpu_thread_affinity = get_worker_override()

if not parser_args.disable_automatic_thread_detection and parser_args.workers is None and parser_args.set_thread_affinity is None and not override_workers:
    thread_detection = True
else:
    print("[INFO] Automatic Thread Detection Disabled")

if thread_detection: # Checking for new Intel architecture
    import psutil
    logical_count = psutil.cpu_count(logical = True)
    physical_count = psutil.cpu_count(logical = False)
    if (logical_count / physical_count) % 1 != 0:
        thread_detection = False  # Intel CPU detected
        print("[INFO] New Intel CPU architecture with P and E cores detected! Not passing thread detection to av1an...\n")
        print("[INFO] Automatic Thread Detection Disabled")
    
if thread_detection: # Checking for Hyperthreading or SMT
    import psutil
    logical_count = psutil.cpu_count(logical = True)
    physical_count = psutil.cpu_count(logical = False)
    if (logical_count / physical_count) == 2:
        hyperthreading = True
    else:
        hyperthreading = False
        
if thread_detection: # Setting values
    if hyperthreading:
        cpu_workers = physical_count
        cpu_thread_affinity = 2
    else:
        cpu_workers = physical_count
        cpu_thread_affinity = 1
    print(f"THREADING INFORMATION:\n  Hyperthreading / SMT: {hyperthreading}\n  Workers: {cpu_workers}\n  Thread Affinity: {cpu_thread_affinity}\n\n")
else:
    print("THREADING INFORMATION:\n  Automatic Thread Detection: DISABLED\n\n")

# If StaxRip path given, automatically add important folders to PATH
if parser_args.staxrip_startup_dir is not None:
    my_env = set_path(parser_args.staxrip_startup_dir)

av1an_exec = "av1an.exe"

command = av1an_exec
command = add_argument(command, "--verbose -y --resume -a=\"-an\"")

# Thread arguments
if thread_detection or override_workers:
    command = add_argument(command, f"--workers {cpu_workers} --set-thread-affinity {cpu_thread_affinity}")
else:
    if parser_args.workers is not None:
        command = add_argument(command, f"--workers {parser_args.workers}")
    if parser_args.set_thread_affinity is not None:
        command = add_argument(command, f"--set-thread-affinity {parser_args.set_thread_affinity}")

if parser_args.encoder is not None:
    command = add_argument(command, f"--encoder {parser_args.encoder}")
if parser_args.encoder_args is not None:
    command = add_argument(command, f"-v \"{parser_args.encoder_args}\"")
if parser_args.photon_noise is not None:
    command = add_argument(command, f"--photon-noise {parser_args.photon_noise}")
if parser_args.chroma_noise:
    command = add_argument(command, f"--chroma-noise")
if parser_args.sc_downscale_height is not None:
    command = add_argument(command, f"--sc-downscale-height {parser_args.sc_downscale_height}")
if parser_args.pix_format is not None:
    command = add_argument(command, f"--pix-format {parser_args.pix_format}")
if parser_args.other_args is not None:
    command = add_argument(command, f"{parser_args.other_args}")
if parser_args.ffmpeg_options is not None:
    command = add_argument(command, f"-f \"{parser_args.ffmpeg_options}\"")

command = add_argument(command, f"-i \"{input_file}\" -o \"{output_file}\" --temp \"{tempdir}\"")
       
sys.stdout.write("Starting av1an... Check new console window for progress\n")
sys.stdout.write("Command: " + str(command) + "\n")
sys.stdout.flush()

if parser_args.staxrip_startup_dir is not None:
    process = subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE, env=my_env)
else:
    process = subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE) # Assume everything is in PATH

if process.returncode != 0:
    print(process.stderr)
    print("[ERROR] Error occurred when transcoding with av1an. Check logs")
    exit(1)
