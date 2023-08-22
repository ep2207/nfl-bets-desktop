import tkinter as tk
from tkinter import ttk, Listbox, Scrollbar, PanedWindow
from PIL import Image, ImageTk
import functions

colors = {
    "primary": "#013369",
    "secondary": "#FFD700",
    "accent": "#FF4500",
    "neutral": "#C0C0C0",
    "white": "#FFFFFF",
    "error": "#FF0000"
}

def on_match_select(event):
    selected_match = match_listbox.get(match_listbox.curselection())
    print(selected_match)


root = tk.Tk()
root.title("Match Application")
root.configure(bg=colors["primary"])

# import file image 

image_path = "assets/logo/logo-horizontal.png"
raw_image = Image.open(image_path)
logo_image = ImageTk.PhotoImage(raw_image)

desired_width = 100  # Change as per your requirements
aspect_ratio = raw_image.height / raw_image.width
desired_height = int(desired_width * aspect_ratio)

resized_image = raw_image.resize((desired_width, desired_height))

# Convert the resized image for tkinter
logo_image = ImageTk.PhotoImage(resized_image)

# Display the image in a label
label = tk.Label(root, image=logo_image, background=colors['primary'], foreground=colors['white'])
label.pack()

username_label = ttk.Label(root, text="Welcome to the admin app")
username_label.pack(pady=10)

# test


# Main Window
pane = PanedWindow(root, orient=tk.HORIZONTAL)  # Change to HORIZONTAL
pane.pack(fill=tk.BOTH, expand=1)

# Matches list
# Matches list
matches_frame = tk.Frame(pane)
pane.add(matches_frame)

scrollbar = Scrollbar(matches_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Assuming you want to show about 10 items at once, and setting the font size to make each item approx. 50px in height.
match_listbox = Listbox(matches_frame, yscrollcommand=scrollbar.set, bg=colors["primary"], fg=colors["white"],
                        width=20, height=10, font=("Arial", 20))
match_listbox.bind('<<ListboxSelect>>', on_match_select)
match_listbox.pack(fill=tk.BOTH, expand=1)

scrollbar.config(command=match_listbox.yview)


# Match details panel
details_frame = tk.Frame(pane, bg=colors["primary"])
pane.add(details_frame)

teams_label = ttk.Label(details_frame, text="Team names go here")
teams_label.pack(pady=5)

time_label = ttk.Label(details_frame, text="Time info goes here")
time_label.pack(pady=5)

# Input for placing comments
comment_entry = ttk.Entry(details_frame)
comment_entry.pack(pady=10)

close_button = ttk.Button(details_frame, text="Close Match", command=functions.close_match)
close_button.pack(pady=10)

comment_button = ttk.Button(details_frame, text="Add Comment", command=functions.add_comment)
comment_button.pack(pady=10)



#test
root.mainloop()