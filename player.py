import os
import pygame
import tkinter as tk
from tkinter import filedialog
import win32gui
import win32con

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.paused = False
        self.paused_position = 0
        self.current_music = None
        
    def play_music(self, music_file):
        pygame.mixer.music.stop()
        self.current_music = music_file
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        self.paused = False
        
    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None
        self.paused = False
        
    def pause_resume_music(self):
        if self.current_music:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True

def select_music_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        player.play_music(file_path)
        update_status_label(os.path.basename(file_path))

def stop_music():
    player.stop_music()
    update_status_label("")

def pause_resume_music():
    player.pause_resume_music()

def set_volume(volume):
    volume = int(volume)
    pygame.mixer.music.set_volume(volume / 100)

def update_status_label(status_text):
    status_label.config(text=status_text)

if __name__ == "__main__":
    player = MusicPlayer()
    
    root = tk.Tk()
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
    root.title("Mp3 Player")

    root.configure(bg="#333333")
    window_width = 400
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    title_label = tk.Label(root, text="Mp3 Player", font=("Helvetica", 20), fg="white", bg="#333333")
    title_label.pack(pady=10)
    button_frame = tk.Frame(root, bg="#333333")
    button_frame.pack(pady=20)
    ui_font = ("Helvetica", 14)
    play_button = tk.Button(button_frame, text="Play", font=ui_font, command=select_music_file)
    play_button.pack(side="left", padx=10)
    pause_button = tk.Button(button_frame, text="Pause/Resume", font=ui_font, command=pause_resume_music)
    pause_button.pack(side="left", padx=10)
    stop_button = tk.Button(button_frame, text="Stop", font=ui_font, command=stop_music)
    stop_button.pack(side="left", padx=10)
    volume_label = tk.Label(root, text="Volume:", font=("Helvetica", 12), fg="white", bg="#333333")
    volume_label.pack()
    volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume, length=200)  # Adjust the length
    volume_slider.set(50)
    volume_slider.pack()
    status_label = tk.Label(root, text="", font=("Helvetica", 12), fg="white", bg="#333333")
    status_label.pack(pady=10)

    root.mainloop()
    pygame.quit()
