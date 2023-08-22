import tkinter as tk
from tkinter import ttk, Listbox, Scrollbar, PanedWindow

# Color Palette
colors = {
    "primary": "#013369",
    "secondary": "#FFD700",
    "accent": "#FF4500",
    "neutral": "#C0C0C0",
    "white": "#FFFFFF",
    "error": "#FF0000"
}

# Mockup: Acquire data from another file through HTTP requests
def fetch_matches():
    # to be filled and moved 
    pass

def on_match_select(event):
     # to be filled and moved )
    pass

def close_match():
    # to be filled and moved 
    pass

def add_comment():
     # to be filled and moved 
    pass

root = tk.Tk()
root.title("Match Application")
root.configure(bg=colors["primary"])

# Login and Logo
logo_label = ttk.Label(root, text="LOGIN LOGO", background=colors["primary"], foreground=colors["white"])
logo_label.pack(pady=10)

username_label = ttk.Label(root, text="USERNAME", background=colors["primary"], foreground=colors["white"])
username_label.pack(pady=10)

# Main Window
pane = PanedWindow(root, orient=tk.VERTICAL)
pane.pack(fill=tk.BOTH, expand=1)

# Matches list
matches_frame = ttk.Frame(pane, background=colors["primary"])
matches_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

scrollbar = Scrollbar(matches_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

match_listbox = Listbox(matches_frame, yscrollcommand=scrollbar.set, bg=colors["neutral"], fg=colors["white"])
match_listbox.bind('<<ListboxSelect>>', on_match_select)
match_listbox.pack(fill=tk.BOTH, expand=1)

scrollbar.config(command=match_listbox.yview)

# Match details panel
details_frame = ttk.Frame(pane, background=colors["primary"])
details_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

teams_label = ttk.Label(details_frame, text="", background=colors["primary"], foreground=colors["white"])
teams_label.pack(pady=5)
time_label = ttk.Label(details_frame, text="", background=colors["primary"], foreground=colors["white"])
time_label.pack(pady=5)
# ... Add other labels for the rest of the details with the same styling

close_button = ttk.Button(details_frame, text="Close Match", command=close_match, bg=colors["accent"], fg=colors["white"])
close_button.pack(pady=10)

comment_button = ttk.Button(details_frame, text="Add Comment", command=add_comment, bg=colors["secondary"], fg=colors["primary"])
comment_button.pack(pady=10)

# Populate match listbox
matches = fetch_matches()
for match in matches:
    match_listbox.insert(tk.END, match["team_names"])

root.mainloop()
