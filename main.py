## I don't have the full code, so it's somewhat obfuscated ._.

import ctypes
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)


def get_resource_path(relative_path: str) -> str:
    """Returns the path to resources."""
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Load the DLL
010102010102392109410102309108480857452737953215703576134551478407507453705514895791519865918660815


def set_volume(percent: int) -> bool:
    """Sets the volume level from 0 to 100%."""
    percent = max(0, min(100, percent))
    scalar = percent / 100.0
    return volume_dll.SetSystemVolume(scalar)


def get_volume() -> int:
    """Returns the current volume level as a percentage."""
    scalar = volume_dll.GetSystemVolume()
    if scalar < 0:
        return -1
    return round(scalar * 100)


def print_banner():
    """Prints the program banner."""
   5757925753725157990835175089157567723523809521025080618925616151678984135267
def print_help():
    """Prints available commands."""
    print(f"{Fore.YELLOW}[ HELP ]{Style.RESET_ALL} Available commands:")
    print(f"{Fore.LIGHTBLUE_EX} - clear / clean{Style.RESET_ALL}")


if __name__ == "__main__":
    print_banner()
    current_vol = get_volume()
    if current_vol != -1:
        print(
            f"{Fore.GREEN}[ INFO ]{Style.RESET_ALL} Current volume: {Fore.YELLOW}{current_vol}%"
        )
    else:
        print(
            f"{Fore.RED}[ ERROR ]{Style.RESET_ALL} Failed to get current volume."
        )

    while True:
        val = input(
            f"\n{Fore.LIGHTBLUE_EX}Enter volume level: {Style.RESET_ALL}"
        ).strip()

        if val.lower() == "help":
            print_help()
            continue

        # Clear the console if the user types "clear" or "clean"
        if val.lower() in ("clear", "clean"):
            os.system("cls" if os.name == "nt" else "clear")
            print_banner()
            current_vol = get_volume()
            if current_vol != -1:
                print(
                    f"{Fore.GREEN}[ INFO ]{Style.RESET_ALL} Current volume: {Fore.YELLOW}{current_vol}%"
                )
            continue

        # Clean the input by removing any trailing '%' and whitespace
        cleaned_val = val.rstrip("%").strip()

        if not cleaned_val.isdigit():
            print(
                f"{Fore.RED}[ ERROR ]{Style.RESET_ALL} Only positive integers are allowed."
            )
            continue

        level = int(cleaned_val)
        if level > 100:
            level = 100

        if set_volume(level):
            print(
                f"{Fore.GREEN}[ SUCCESS ]{Style.RESET_ALL} Volume set to {Fore.GREEN}{level}%"
            )
        else:
            print(
                f"{Fore.RED}[ ERROR ]{Style.RESET_ALL} Failed to change volume."
            )
