import argparse
import subprocess
import sys

# Command Line Arguments
parser = argparse.ArgumentParser(description="av1an cmd wrapper for StaxRip")
parser.add_argument('-i', dest="input", type=str, required=True, help="Input File")
parser.add_argument('-o', dest="output", type=str, required=True, help="Output File")
parser.add_argument('-t', dest="tempdir", type=str, required=True, help="Temp Directory")
parser.add_argument('--quantizer', type=str, required=False, help="Quantizer argument for rav1e") # Quantizer (0-255), smaller values are higher quality (default: 100)
parser.add_argument('--speed', type=str, required=False, help="Speed argument for rav1e") # Speed level 0-10 (0 is best quality, 10 is fastest) (default: 6)
parser.add_argument('--workers', type=str, required=False, help="Number of workers to spawn [0 = automatic]")
parser.add_argument('--tiles', type=str, required=False, help="Number of tiles (to rav1e)")
parser.add_argument('--threads', type=str, required=False, help="Number of threads (to rav1e)")
parser_args = parser.parse_args()

input_file = parser_args.input
output_file = parser_args.output
tempdir = parser_args.tempdir

# # Parsing rav1e arguments
rav1e_argument_string = ""

def add_argument(curr, new):
    return_string = curr
    if curr == "":
        return_string = new
    else:
        return_string += (" " + new)
    return return_string
    
if parser_args.speed is not None:
    rav1e_argument_string = add_argument(rav1e_argument_string, f"--speed {parser_args.speed}")
if parser_args.quantizer is not None:
    rav1e_argument_string = add_argument(rav1e_argument_string, f"--quantizer {parser_args.quantizer}")
if parser_args.tiles is not None:
    rav1e_argument_string = add_argument(rav1e_argument_string, f"--tiles {parser_args.tiles}")
if parser_args.threads is not None:
    rav1e_argument_string = add_argument(rav1e_argument_string, f"--threads {parser_args.threads}")


# Assuming av1an is stored in PATH
av1an_exec = "av1an.exe"

command = av1an_exec
command = add_argument(command, "--verbose -y --resume -a=\"-an\" -e rav1e --pix-format yuv420p10le")

if parser_args.workers is not None:
    command = add_argument(command, f"--workers {parser_args.workers}")

if rav1e_argument_string != "":
    command = add_argument(command, f"-v=\"{rav1e_argument_string} --no-scene-detection\"")

command = add_argument(command, f"-i \"{input_file}\" -o \"{output_file}\" --temp \"{tempdir}\"")
       

sys.stdout.write("Starting av1an... Check new console window for progress\n")
sys.stdout.write("Arguments: " + str(command) + "\n")
sys.stdout.flush()

process = subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)

if process.returncode != 0:
    print(process.stderr)
    print("Error occurred when transcoding with av1an. Check logs")
    exit(1)
    
# args = [av1an_exec,
#         "--verbose",
#         "-y",
#         "-a='-an'",
#         # '-f="-sn"',
#         "-e", "rav1e",
#         "--pix-format", "yuv420p10le"]

# Parsing rav1e arguments
# if parser_args.quantizer is not None:
#     args.append("--quantizer")
#     args.append(parser_args.quantizer)

# if rav1e_argument_string != "":
#     args.append(f"-v='{rav1e_argument_string} --no-scene-detection --tiles 2'")


# necessary_args = ["-i", input_file,
#                   "-o", output_file,
#                   "--temp", tempdir]
# args.extend(necessary_args)    