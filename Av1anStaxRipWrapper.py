import argparse
import subprocess
import sys

# Generic Version to pass in any argument to av1an

# Command Line Arguments
parser = argparse.ArgumentParser(description="av1an cmd wrapper for StaxRip")
parser.add_argument('-i', dest="input", type=str, required=True, help="Input File")
parser.add_argument('-o', dest="output", type=str, required=True, help="Output File")
parser.add_argument('-t', dest="tempdir", type=str, required=True, help="Temp Directory")
parser.add_argument('--args', dest="arguments", type=str, required=False, help="Arguments to pass to av1an")
parser_args = parser.parse_args()

input_file = parser_args.input
output_file = parser_args.output
tempdir = parser_args.tempdir

def add_argument(curr, new):
    return_string = curr
    if curr == "":
        return_string = new
    else:
        return_string += (" " + new)
    return return_string


# Assuming av1an is stored in PATH
av1an_exec = "av1an.exe"

command = av1an_exec
command = add_argument(command, "--verbose -y --resume -a=\"-an\" --pix-format yuv420p10le")
if parser_args.args is not None:
    command = add_argument(command, parser_args.args)
command = add_argument(command, f"-i \"{input_file}\" -o \"{output_file}\" --temp \"{tempdir}\"")

sys.stdout.write("Starting av1an... Check new console window for progress\n")
sys.stdout.write("Arguments: " + str(command) + "\n")
sys.stdout.flush()

process = subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)

if process.returncode != 0:
    print(process.stderr)
    print("Error occurred when transcoding with av1an. Check logs")
    exit(1)
