import tkinter as tk
from tkinter import ttk, Listbox, Scrollbar, PanedWindow
import tkinter.font as tkFont
from PIL import Image, ImageTk
import functions
from models.match import allMatches 

colors = {
    "primary": "#013369",
    "secondary": "#FFD700",
    "accent": "#FF4500",
    "neutral": "#C0C0C0",
    "white": "#FFFFFF",
    "error": "#FF0000"
}


def on_match_select(event):
    selected_index = match_listbox.curselection()[0] # Get selected index
    selected_match = matches[selected_index] # Get the Match object based on index

    # Now, you can use the attributes of selected_match to display details
    visiting_team_label.config(text=selected_match.visiting_team_name)
    # You can do similar updates for other labels/details you wish to show
    receiving_team_label.config(text=f"{selected_match.visiting_team_name} vs {selected_match.receiving_team_name}")
    time_label.config(text=f"{selected_match.match_kickoff} to {selected_match.match_end}")
    # Add any other details as needed




root = tk.Tk()
root.title("NFL BETS admin only desktop app ")
root.configure(bg=colors["primary"])
root.option_add('*Font', 'MyriadPro 14')


custom_font = ('Myriad Pro', 20)



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
horizontal_frame = tk.Frame(root, bg=colors['primary'])
horizontal_frame.pack(pady=10)

# Display the image in a label, inside the horizontal frame.
logo_label = tk.Label(horizontal_frame, image=logo_image, bg=colors['primary'])
logo_label.pack(side=tk.LEFT, padx=10)  # Pack on the left side of the horizontal frame.

# Display the text label, also inside the horizontal frame.
username_label = ttk.Label(horizontal_frame, text="Welcome to the admin app", background=colors["primary"], foreground=colors["white"], font=custom_font)
username_label.pack(side=tk.LEFT, padx=10)


# Main Window
pane = PanedWindow(root, orient=tk.HORIZONTAL)  # Change to HORIZONTAL
pane.pack(fill=tk.BOTH, expand=1)

# Matches list
matches_frame = tk.Frame(pane)
pane.add(matches_frame)

scrollbar = Scrollbar(matches_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Assuming you want to show about 10 items at once, and setting the font size to make each item approx. 50px in height.
match_listbox = Listbox(matches_frame, yscrollcommand=scrollbar.set, bg=colors["primary"], fg=colors["white"],
                        width=70, height=10, font=("Myriad pro", 10))
match_listbox.bind('<<ListboxSelect>>', on_match_select)
match_listbox.pack(fill=tk.BOTH, expand=1)

scrollbar.config(command=match_listbox.yview, bg=colors["primary"])




# Match details panel
details_frame = tk.Frame(pane, bg=colors['primary'])
pane.add(details_frame)

# Set a minimum width of 500 for the details_frame
pane.paneconfigure(details_frame, minsize=500)

visiting_team_label = ttk.Label(details_frame, text="Team names go here", background=colors["primary"], foreground=colors["white"],)
visiting_team_label.pack(pady=5)

receiving_team_label = ttk.Label(details_frame, text="Team names go here", background=colors["primary"], foreground=colors["white"],)
receiving_team_label.pack(pady=5)



time_label = ttk.Label(details_frame, text="Time info goes here", background=colors["primary"], foreground=colors["white"],)
time_label.pack(pady=5)

# Input for placing comments
comment_entry = ttk.Entry(details_frame)
comment_entry.pack(pady=10)

close_button = ttk.Button(details_frame, text="Close Match", command=functions.close_match)
close_button.pack(pady=10)

comment_button = ttk.Button(details_frame, text="Add Comment", command=functions.add_comment)
comment_button.pack(pady=10)



## POPULATE Windows

matches = allMatches()
for match in matches:
    match_listbox.insert(tk.END, str(match))



#test
root.mainloop()