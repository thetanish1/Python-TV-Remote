import tkinter as tk
from tkinter import messagebox
import random
import time

class TvRemote:
    def __init__(self):
        self.tv_state = "Off"
        self.tv_voice = 0
        self.channel_list = ["Fox"]
        self.channel = "Fox"

    def tv_open(self):
        if self.tv_state == "On":
            return "TV is already ON."
        self.tv_state = "On"
        return "TV turned ON."

    def tv_close(self):
        if self.tv_state == "Off":
            return "TV is already OFF."
        self.tv_state = "Off"
        return "TV turned OFF."

    def voice_up(self):
        if self.tv_voice < 50:
            self.tv_voice += 1
        return f"Volume: {self.tv_voice}"

    def voice_down(self):
        if self.tv_voice > 0:
            self.tv_voice -= 1
        return f"Volume: {self.tv_voice}"

    def add_channel(self, channel_name):
        if channel_name:
            self.channel_list.append(channel_name)
            return f"Channel '{channel_name}' added."
        return "No channel name entered."

    def random_channel(self):
        if self.channel_list:
            self.channel = random.choice(self.channel_list)
            return f"Switched to: {self.channel}"
        return "No channels available."

    def get_info(self):
        return f"""TV State: {self.tv_state}
Volume: {self.tv_voice}
Channels: {', '.join(self.channel_list)}
Current Channel: {self.channel}"""

# ----------------- GUI ------------------
remote = TvRemote()

root = tk.Tk()
root.title("TV Remote GUI")
root.geometry("400x400")
root.config(bg="lightgray")

# Display box
info_text = tk.StringVar()
info_text.set(remote.get_info())
label = tk.Label(root, textvariable=info_text, justify="left", bg="white", relief="solid", padx=10, pady=10)
label.pack(pady=10, fill="x")

def update_info(msg=""):
    info_text.set(remote.get_info())
    if msg:
        messagebox.showinfo("Update", msg)

# Buttons
frame = tk.Frame(root, bg="lightgray")
frame.pack(pady=10)

btn_on = tk.Button(frame, text="TV ON", command=lambda: update_info(remote.tv_open()), width=12)
btn_on.grid(row=0, column=0, padx=5, pady=5)

btn_off = tk.Button(frame, text="TV OFF", command=lambda: update_info(remote.tv_close()), width=12)
btn_off.grid(row=0, column=1, padx=5, pady=5)

btn_up = tk.Button(frame, text="Volume +", command=lambda: update_info(remote.voice_up()), width=12)
btn_up.grid(row=1, column=0, padx=5, pady=5)

btn_down = tk.Button(frame, text="Volume -", command=lambda: update_info(remote.voice_down()), width=12)
btn_down.grid(row=1, column=1, padx=5, pady=5)

btn_random = tk.Button(frame, text="Random Channel", command=lambda: update_info(remote.random_channel()), width=26)
btn_random.grid(row=2, columnspan=2, padx=5, pady=5)

channel_entry = tk.Entry(root, width=30)
channel_entry.pack(pady=5)
channel_entry.insert(0, "Enter channel name")

def add_channel():
    channel = channel_entry.get().strip()
    msg = remote.add_channel(channel)
    update_info(msg)

btn_add_channel = tk.Button(root, text="Add Channel", command=add_channel, width=30)
btn_add_channel.pack(pady=5)

btn_info = tk.Button(root, text="Refresh Info", command=lambda: update_info(), width=30)
btn_info.pack(pady=5)

root.mainloop()
