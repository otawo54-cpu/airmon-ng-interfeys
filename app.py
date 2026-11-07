#!/usr/bin/env python3
"""Kali Linux wireless interface diagnostics dashboard (read-only)."""
import json
import os
import shutil
import subprocess
import sys
import tkinter as tk
from tkinter import ttk, messagebox

COMMANDS = {
    "Wi-Fi interfeyslar": ["iw", "dev"],
    "Interfeys holati": ["ip", "-brief", "link"],
    "USB qurilmalar": ["lsusb"],
    "USB port tezligi": ["lsusb", "-t"],
    "Airmon-ng qurilmalar": ["airmon-ng"],
    "RFKill holati": ["rfkill", "list"],
    "NetworkManager holati": ["nmcli", "device", "status"],
}
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Airmon-ng Interfeys | Kali Diagnostics")
        self.geometry("940x620")
        self.minsize(700, 460)
        self.configure(bg="#101827")
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#101827")
        style.configure("TLabel", background="#101827", foreground="#e2e8f0", font=("DejaVu Sans", 11))
        style.configure("TButton", padding=(12, 9), font=("DejaVu Sans", 10))
        header = ttk.Frame(self)
        header.pack(fill="x", padx=22, pady=(20, 10))
        ttk.Label(header, text="AIRMON-NG  |  DIAGNOSTICS", font=("DejaVu Sans", 19, "bold")).pack(anchor="w")
        ttk.Label(header, text="Kali Live USB uchun xavfsiz, faqat o‘qiydigan Wi-Fi diagnostika paneli").pack(anchor="w", pady=(4, 0))
        body = ttk.Frame(self)
        body.pack(fill="both", expand=True, padx=22, pady=12)
        menu = ttk.Frame(body)
        menu.pack(side="left", fill="y", padx=(0, 16))
        for label in COMMANDS:
            ttk.Button(menu, text=label, width=24, command=lambda item=label: self.run_command(item)).pack(fill="x", pady=5)
        ttk.Button(menu, text="Natijani tozalash", command=self.clear).pack(fill="x", pady=(20, 5))
        result = ttk.Frame(body)
        result.pack(side="left", fill="both", expand=True)
        self.text = tk.Text(result, bg="#0b1220", fg="#d4e5ee", insertbackground="white", relief="flat", wrap="word", font=("DejaVu Sans Mono", 10), padx=14, pady=14)
        scroll = ttk.Scrollbar(result, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
        self.write("Tayyor. Chapdan diagnostika tugmasini tanlang.\n\nBu versiya monitor mode, deauth yoki handshake capture'ni ishga tushirmaydi.\n")
    def write(self, value):
        self.text.insert("end", value)
        self.text.see("end")
    def clear(self):
        self.text.delete("1.0", "end")
    def run_command(self, label):
        argv = COMMANDS[label]
        self.write(f"\n$ {' '.join(argv)}\n" + "-" * 48 + "\n")
        if not shutil.which(argv[0]):
            self.write(f"'{argv[0]}' topilmadi. Kali paketlari va PATH ni tekshiring.\n")
            return
        self.update_idletasks()
        try:
            result = subprocess.run(argv, capture_output=True, text=True, timeout=12, check=False, env={**os.environ, "LC_ALL": "C"})
            self.write((result.stdout or "") + (result.stderr or "") + f"\nExit code: {result.returncode}\n")
        except subprocess.TimeoutExpired:
            self.write("Buyruq 12 soniyada yakunlanmadi.\n")
        except OSError as error:
            self.write(f"Xatolik: {error}\n")
if __name__ == "__main__":
    if sys.platform != "linux":
        print("Bu ilova Linux uchun mo‘ljallangan.", file=sys.stderr)
        sys.exit(1)
    App().mainloop()
