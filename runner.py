#!/usr/bin/env python3

from datetime import datetime
from os import listdir, system
from pathlib import Path
from sys import argv, exit, stderr
from threading import Thread


def log(s):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {s}")


def run_input(command, input_dir, output_dir, filename):
    system_cmd = f"{command} < {input_dir}{filename} > {output_dir}{filename}.out.txt"
    system_ret = system(system_cmd)
    log(system_cmd)
    exit_code = system_ret >> 8
    log(f"run for input file {filename} finished with exit code {exit_code}")


def run_inputs(command, input_dir, output_dir):
    log("starting")
    filenames = listdir(input_dir)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    threads = []
    for filename in filenames:
        thread_args = (command, input_dir, output_dir, filename)
        thread = Thread(target=run_input, args=thread_args)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Error: wrong number of arguments", file=stderr)
        print(f"Usage: {argv[0]} [command] [input_dir] [output_dir]", file=stderr)
        exit(1)
    command, input_dir, output_dir = argv[1:]
    run_inputs(command, input_dir, output_dir)
