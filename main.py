import datetime
import json
import tkinter as tk
from tkinter import ttk, Listbox, Scrollbar, PanedWindow
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from queries.post_queries import postCommentary, closeMatch
from models.match import allMatches 
from models.bet import  separate_bets_by_team,total_bet_amount
from utils.functions import getClosureData,sanitizeInput
import time


colors = {
    "primary": "#013369",
    "secondary": "#FFD700",
    "accent": "#FF4500",
    "neutral": "#C0C0C0",
    "white": "#FFFFFF",
    "error": "#FF0000"
}


def on_match_select(event):
    selected_index = match_listbox.curselection()[0] # 
    selected_match = matches[selected_index]

    # Conditionally show score label or close button and score modification entry
    if selected_match.match_is_closed:
        
        close_button.pack_forget()  # Hide close button
        comment_entry.pack_forget()  # Hide comment entry
        comment_button.pack_forget()  # Hide comment button
        score_frame.pack()
        score_label.config(text=f"Final Score: {selected_match.score}")
        score_label.pack(pady=5)
        visiting_team_score_label.pack_forget()
        visiting_team_score_entry.pack_forget() 
        receiving_team_score_label.pack_forget() 
        receiving_team_score_entry.pack_forget() 

    else:
        score_label.pack_forget()  # Hide score label
        close_button.pack(pady=10)  # Show close button
        comment_entry.pack(pady=10)  # Show comment entry
        comment_button.pack(pady=10)  # Show comment button
        visiting_team_score_label.pack(pady=5)
        visiting_team_score_label.config(text=f"Score of {selected_match.visiting_team_name}:")
        visiting_team_score_entry.pack(pady=5) 
        receiving_team_score_label.pack(pady=5)
        receiving_team_score_label.config(text=f"Score of {selected_match.receiving_team_name}:")
        receiving_team_score_entry.pack(pady=5)


    teams_label.config(text=f"{selected_match.visiting_team_name} vs {selected_match.receiving_team_name}")
    time_label.config(text=f"{selected_match.match_kickoff} to {selected_match.match_end}")
    bets_vis_list_label.config(text = f"bets on: {selected_match.visiting_team_name}")
    bets_rec_list_label.config(text = f"bets on: {selected_match.receiving_team_name}")

    
    ### populating list logic 

    # Clear the current items in bets_listbox
    visiting_team_bets_listbox.delete(0, tk.END)
    receiving_team_bets_listbox.delete(0, tk.END)

    #split the bets in two 
    visiting_team_bets,receiving_team_bets = separate_bets_by_team(selected_match)
    
    # Add bets from the selected match to bets_listbox
    if visiting_team_bets:
        for bet in visiting_team_bets:
            visiting_team_bets_listbox.insert(tk.END, str(bet))  
    else:
        visiting_team_bets_listbox.insert(tk.END, "No bets available for the selected match.")

    bets_vis_sum_label.config(text = f"sum of bets on {selected_match.visiting_team_name}: {total_bet_amount(visiting_team_bets)}  $") 
    
    # Add bets from the selected match to bets_listbox
    if receiving_team_bets:
        for bet in receiving_team_bets: 
            receiving_team_bets_listbox.insert(tk.END, str(bet))  
    else:
        receiving_team_bets_listbox.insert(tk.END, "No bets available for the selected match.")
    
    bets_rec_sum_label.config(text = f"sum of bets on {selected_match.receiving_team_name}: {total_bet_amount(receiving_team_bets)}  $") 

    try:
        if selected_match.score and ":" in selected_match.score:
            visiting_team_score, receiving_team_score = selected_match.score.split(":")
        else:
            visiting_team_score, receiving_team_score = None, None
    
    except ValueError:
        visiting_team_score, receiving_team_score = None, None


    visiting_team_score_entry.delete(0, tk.END)
    receiving_team_score_entry.delete(0, tk.END)


    commentaries_listbox.delete(0, tk.END)
    for commentary in selected_match.match_commentaries:
        commentaries_listbox.insert(tk.END, commentary)



def get_selected_match():
    selected_index = match_listbox.curselection()
    
    if not selected_index:  # If no match is selected, this is an empty tuple
        return None

    selected_match = matches[selected_index[0]]
    return selected_match



def close_match():
    response = messagebox.askyesno("Confirmation to close a match", "Are you sure you want to close this match?")
    global matches

    if response:

        selected_match = get_selected_match()
        
        if not selected_match:
            messagebox.showwarning("Warning", "No match is selected! First select a match")
            return
        
        
        # Retrieve scores
        visiting_team_score = visiting_team_score_entry.get()
        receiving_team_score = receiving_team_score_entry.get()

        if not (visiting_team_score.isdigit() and receiving_team_score.isdigit()):
            messagebox.showwarning("Invalid Score", "Please provide valid numeric scores for both teams.")
            return

        # Update the score in the format "visiting_team_score:receiving_team_score"
        selected_match.score = f"{visiting_team_score}:{receiving_team_score}"

        visiting_team_score_entry.delete(0, 'end')
        receiving_team_score_entry.delete(0, 'end')

        matchAndBetsData = json.loads(getClosureData(selected_match))
        closeMatch(matchAndBetsData)

        time.sleep(3) # wait for server interaction
        matches =allMatches(); #refresh matches 


def add_commentary():
    response = messagebox.askyesno("Confirmation to a commentary", "Are you sure you want to post this commentary?")
    global matches

    if response:

        ## verify a match is selected
        selected_match = get_selected_match()
        
        if not selected_match:
            messagebox.showwarning("Warning", "No match is selected! First select a match")
            return

         # Retrieve commentary from Entry widget
        commentary_text = comment_entry.get()


        if not commentary_text:
            messagebox.showwarning("Warning", "Please enter a commentary before posting!")
            return
        

        else:
            clean_Commentary=sanitizeInput(commentary_text)
            postCommentary(selected_match.match_id,clean_Commentary)
            time.sleep(3) # wait for server interaction
            matches =allMatches(); #refresh matches 
        
def refresh_matches():
    matches = allMatches()  # Refresh matches
    match_listbox.delete(0, tk.END)  # Clear current matches
    for match in matches:  # Populate matches
        match_listbox.insert(tk.END, str(match))



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
welcome_label = tk.Label(horizontal_frame, text="Welcome to the admin app", background=colors["primary"], foreground=colors["white"], font=custom_font)
welcome_label.pack(side=tk.LEFT, padx=10)

refresh_button = ttk.Button(horizontal_frame, text="Refresh", command=refresh_matches)
refresh_button.pack(side=tk.RIGHT, padx=10) 




# Main Window
pane = PanedWindow(root, orient=tk.HORIZONTAL, height=1000)  # Change to HORIZONTAL
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

teams_label = tk.Label(details_frame, text="teams", background=colors["primary"], foreground=colors["secondary"],)
teams_label.pack(pady=5)


time_label = tk.Label(details_frame, text="kickoff-end", background=colors["primary"], foreground=colors["secondary"],)
time_label.pack(pady=5)


# Horizontal score frame
score_frame = tk.Frame(details_frame, bg=colors['primary'])
score_frame.pack(pady=5, fill=tk.X)

score_label = tk.Label(score_frame, text="score", background=colors["primary"], foreground=colors["secondary"],)
score_label.pack(pady=5)

# Score label and entry for visiting team
visiting_team_score_label = tk.Label(score_frame, text=f"Score", background=colors["primary"], foreground=colors["secondary"])
visiting_team_score_label.pack(side=tk.LEFT, padx=10)
validate_cmd = score_frame.register(lambda value: value.isdigit() or value == "")
visiting_team_score_entry = ttk.Entry(score_frame, validate="key", validatecommand=(validate_cmd, '%P'), width=5)
visiting_team_score_entry.pack(side=tk.LEFT)

# Score label and entry for receiving team
receiving_team_score_label = tk.Label(score_frame, text=f"Score", background=colors["primary"], foreground=colors["secondary"])
receiving_team_score_label.pack(side=tk.RIGHT, padx=10)
receiving_team_score_entry = ttk.Entry(score_frame, validate="key", validatecommand=(validate_cmd, '%P'), width=5)
receiving_team_score_entry.pack(side=tk.RIGHT)

close_button = ttk.Button(score_frame, text="Close Match", command=close_match)
close_button.pack(pady=10)


# Input for placing comments

# Horizontal score frame
comment_frame = tk.Frame(details_frame, bg=colors['primary'])
comment_frame.pack(pady=5, fill=tk.X)

comment_entry = ttk.Entry(comment_frame, width=70, foreground=colors["primary"],font=("Myriad pro",10))
comment_entry.pack(pady=10)

comment_button = tk.Button(comment_frame, text="Add Comment", command=add_commentary)
comment_button.pack(pady=10)


commentaries_listbox = Listbox(details_frame, yscrollcommand=scrollbar.set, bg=colors["primary"], fg=colors["white"],
                        width=30, height=3, font=("Myriad pro", 10))
commentaries_listbox.pack(fill=tk.BOTH, expand=1)



bets_vis_list_label = tk.Label(details_frame, text="list of bets for visiting team", background=colors["primary"], foreground=colors["white"],font=("Myriad pro",12))
bets_vis_list_label.pack(pady=5)

visiting_team_bets_listbox = Listbox(details_frame, yscrollcommand=scrollbar.set, bg=colors["primary"], fg=colors["white"],
                        width=70, height=3, font=("Myriad pro", 10))
visiting_team_bets_listbox.pack(fill=tk.BOTH, expand=1)

bets_vis_sum_label = tk.Label(details_frame, text="sum of bets for visiting team", background=colors["primary"], foreground=colors["white"],font=("Myriad pro",10))
bets_vis_sum_label.pack(pady=5)

bets_rec_list_label = tk.Label(details_frame, text="list of bets for visiting team", background=colors["primary"], foreground=colors["white"],font=("Myriad pro",12))
bets_rec_list_label.pack(pady=5)

receiving_team_bets_listbox = Listbox(details_frame, yscrollcommand=scrollbar.set, bg=colors["primary"], fg=colors["white"],
                        width=70, height=3, font=("Myriad pro", 10))
receiving_team_bets_listbox.pack(fill=tk.BOTH, expand=1)

bets_rec_sum_label = tk.Label(details_frame, text="sum of bets for the receiving team", background=colors["primary"], foreground=colors["white"],font=("Myriad pro",10))
bets_rec_sum_label.pack(pady=5)




## POPULATE Windows
matches = allMatches()
for match in matches:
    match_listbox.insert(tk.END, str(match))



#test
root.mainloop()