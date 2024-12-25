#!/usr/bin/env python3

import os
import platform
import subprocess
import time
import shutil


def print_logo():
    terminal_width, _ = shutil.get_terminal_size(fallback=(80, 20))
    logo = """
     _______. __  .___________. __    __   _______  _______ .___________.  ______  __    __  
    /       ||  | |           ||  |  |  | |   ____||   ____||           | /      ||  |  |  | 
   |   (----`|  | `---|  |----`|  |__|  | |  |__   |  |__   `---|  |----`|  ,----'|  |__|  | 
    \   \    |  |     |  |     |   __   | |   __|  |   __|      |  |     |  |     |   __   | 
.----)   |   |  |     |  |     |  |  |  | |  |     |  |____     |  |     |  `----.|  |  |  | 
|_______/    |__|     |__|     |__|  |__| |__|     |_______|    |__|      \______||__|  |__| 
                                                                                             
"""
    scaled_logo = "\n".join(line[:terminal_width] for line in logo.splitlines())
    print("\033[1;31m")
    print(scaled_logo)
    print("\033[0m POWER! UNLIMITED POWER!")


def get_info():
    os_name = subprocess.getoutput(
        "grep '^PRETTY_NAME' /etc/os-release | cut -d= -f2- | tr -d '\"'"
    )
    kernel = platform.release()
    uptime = subprocess.getoutput("uptime -p")
    shell = os.environ.get("SHELL", "Unknown Shell")
    cpu = subprocess.getoutput(
        "lscpu | grep 'Model name:' | awk -F: '{print $2}' | sed 's/^[ \t]*//'"
    )
    memory = subprocess.getoutput("free -h | awk '/^Mem:/ {print $3 \"/\" $2}'")

    print(f"\033[1;31mSith OS:\033[0m {os_name}")
    print(f"\033[1;31mDark Kernel:\033[0m {kernel}")
    print(f"\033[1;31mUptime of Darkness:\033[0m {uptime}")
    print(f"\033[1;31mSaber Shell:\033[0m {shell}")
    print(f"\033[1;31mSith CPU:\033[0m {cpu}")
    print(f"\033[1;31mMemory of the Empire:\033[0m {memory}")
    print(f"\033[1;31mStorage of the Death Star:\033[0m")
    get_storage()


def get_storage():
    storage = subprocess.getoutput(
        "df -h --output=source,size,used,avail | grep -E '^/dev/'"
    )
    for line in storage.splitlines():
        print(f"\033[1;90m{line}\033[0m")  # Dim text


def scroll_text():
    messages = [
        "The Dark Side of the terminal awakens...",
        "Through passion, you gain strength.",
        "Through strength, you gain system knowledge.",
    ]
    print("\033[1;31m")  # Red text
    for message in messages:
        print(message)
        time.sleep(1)
    print("\033[0m")  # Reset text color


if __name__ == "__main__":
    scroll_text()
    print_logo()
    get_info()
