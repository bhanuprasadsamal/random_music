import os
import random
import pygame


folder_path = "give the path of your music folder "

pygame.mixer.init()

music_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]

if len(music_files) == 0:
    print("No music files found in the folder.")
else:
   
    random_music = random.choice(music_files)

    music_path = os.path.join(folder_path, random_music)
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
