"""
@author Merlin von der Weide
@version 1.1.0-beta
@date 06.08.2024

"""
import sys

from colorama import Fore


def print_error(message, fatal=True):
    print(Fore.RED, "[!] ERROR: %s" % message)
    if fatal:
        sys.exit(1)


def print_warning(message):
    print(Fore.YELLOW, "[-] WARN: %s" % message)


def print_info(message):
    print(Fore.LIGHTBLUE_EX, "[+] INFO: %s" % message)

def print_success(message):
    print(Fore.GREEN, "%s" % message)