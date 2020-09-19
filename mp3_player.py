from tkinter import *

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

def add_song():
    pass

def add_many_songs():
    pass

# Playlist Box using Listbox Widget
playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

# Definition of Button Images
back_btn_img = PhotoImage(file='images/back.png')
forward_btn_img = PhotoImage(file='images/forward.png')
play_btn_img = PhotoImage(file='images/play.png')
pause_btn_img = PhotoImage(file='images/pause.png')
stop_btn_img = PhotoImage(file='images/stop.png')

# Button Wrapper
btn_frame = Frame(root)
btn_frame.pack(pady=20)

# Playlist Control Buttons
back_btn = Button(btn_frame, image=back_btn_img, borderwidth=0)
forward_btn = Button(btn_frame, image=forward_btn_img, borderwidth=0)
play_btn = Button(btn_frame, image=play_btn_img, borderwidth=0)
pause_btn = Button(btn_frame, image=pause_btn_img, borderwidth=0)
stop_btn = Button(btn_frame, image=stop_btn_img, borderwidth=0)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdows
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# Add One Song To Playlist
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
# Add Many Songs to Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

root.mainloop()