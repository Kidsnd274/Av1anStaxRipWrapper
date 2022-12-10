import argparse
import subprocess
import sys

# Command Line Arguments
parser = argparse.ArgumentParser(description="av1an cmd wrapper for StaxRip")
parser.add_argument('-i', dest="input", type=str, required=True, help="Input File")
parser.add_argument('-o', dest="output", type=str, required=True, help="Output File")
parser.add_argument('-t', dest="tempdir", type=str, required=True, help="Temp Directory")
args = parser.parse_args()

input_file = args.input
output_file = args.output
tempdir = args.tempdir

# Assuming av1an is stored in PATH
av1an_exec = "av1an.exe"

args = [av1an_exec,
        "--verbose",
        "-y",
        '-a="-an"',
        '-f="-sn"',
        "-e", "rav1e",
        "-i", input_file,
        "-o", output_file,
        "--temp", tempdir]

sys.stdout.write("Starting av1an... Check new console window for progress\n")
sys.stdout.flush()

process = subprocess.run(args, creationflags=subprocess.CREATE_NEW_CONSOLE)

if process.returncode != 0:
    print(process.stderr)
    print("Error occurred when transcoding with av1an. Check logs")
    exit(1)