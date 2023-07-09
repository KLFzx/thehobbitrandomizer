import tkinter as tk
import tkinter.ttk as ttk
from tktooltip import ToolTip
from tkinter import messagebox
import subprocess
import os
import shutil
import re
import random
import threading

level_short = [ "Ch00_Dre",
   "Ch01_Hob",
   "Ch02_Roa",
   "Ch02a_Tr",
   "Ch4_Over",
   "Ch05_Swo",
   "Mirkwood",
   "Ch07_Bar",
   "CH08_Lak",
   "Ch09_Sma",
   "Ch10_Lon",
   "Ch11_Clo"
]

nameArray = [
    'CH00_DREAMWORLD',
    'CH01_HOBBITON',
    'CH02_ROASTMUTTON',
    'CH02A_TROLLHOLE',
    'CH05_SWORDLIGHT',
    'CH07_BARRELSOUTOFBOND',
    'CH08_LAKETOWN',
    'CH09_SMAUG',
    'CH10_LONELY_MOUNTAIN',
    'CH11_CLOUDSBURST'
    'CH4_OVERHILL',
    'MIRKWOOD'
]

level_dict = {
    'Ch00_Dre': 'CH00_DREAMWORLD',
    'Ch01_Hob': 'CH01_HOBBITON',
    'Ch02_Roa': 'CH02_ROASTMUTTON',
    'Ch02a_Tr': 'CH02A_TROLLHOLE',
    'Ch4_Over': 'CH4_OVERHILL',
    'Ch05_Swo': 'CH05_SWORDLIGHT',
    'Mirkwood': 'MIRKWOOD',
    'Ch07_Bar': 'CH07_BARRELSOUTOFBOND',
    'CH08_Lak': 'CH08_LAKETOWN',
    'Ch09_Sma': 'CH09_SMAUG',
    'Ch10_Lon': 'CH10_LONELY_MOUNTAIN',
    'Ch11_Clo': 'CH11_CLOUDSBURST'
}


def reset_game():
    if not os.path.exists('./snap'):
        messagebox.showinfo("reset_game", "SAVE ORIGINAL FIRST!!!!!!!!")
        return

    copy_files('./snap', '../')
    messagebox.showinfo("Resetting", "Reset is Done!")


def save_levels():
    copy_files('../',  './favourite')
    messagebox.showinfo("Save Levels", "Done")


def modify_rigid_in_file(filename):
    # Read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Regular expression to match the entire object
    pattern = (r'\[\s*RigidInstance\s*:\s*\d+\s*\]\s*'
               r'\{.*?Pos:fff.*?Orient:fff.*?\}\s*'
               r'"[^"]*"\s+"[^"]*"\s+"[^"]*"\s+"[^"]*"\s+'
               r'(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+).*?'
               r'(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)')

    # Function to replace the positions and orientations with random values
    def replace_position_and_orientation(match):
        old_x, old_y, old_z = float(match.group(1)), float(match.group(2)), float(match.group(3))
        old_orientx, old_orienty, old_orientz = float(match.group(4)), float(match.group(5)), float(match.group(6))
        new_x = str(old_x + random.uniform(-int(posx_var.get()), int(posx_var.get())) )
        new_y = str(old_y + random.uniform(-int(posy_var.get()), int(posy_var.get())) )
        new_z = str(old_z + random.uniform(-int(posz_var.get()), int(posz_var.get())) )
        
        new_orientx = str(old_orientx + random.uniform(-int(orientx_var.get()), int(orientx_var.get())) )
        new_orienty = str(old_orienty + random.uniform(-int(orienty_var.get()), int(orienty_var.get())) )
        new_orientz = str(old_orientz + random.uniform(-int(orientz_var.get()), int(orientz_var.get())) )
       
        return (match.group(0).replace(match.group(1), new_x)
                             .replace(match.group(2), new_y)
                             .replace(match.group(3), new_z)
                             .replace(match.group(4), new_orientx)
                             .replace(match.group(5), new_orienty)
                             .replace(match.group(6), new_orientz))

    # Replace all occurrences of the positions and orientations with random values
    modified_content = re.sub(pattern, replace_position_and_orientation, content, flags=re.DOTALL)

    # Save the modified content back to the file
    with open(filename, 'w') as file:
        file.write(modified_content)

    print(f"Positions and orientations modified in {filename}")


def modify_npc_in_file(filename):
    pass

def modify_pickup_in_file(filename):
    pass

def modify_save_in_file(filename):
    pass

def modify_volume_in_file(filename):
    pass


def modify_trigger_in_file(filename):
    pass

def modify_chest_in_file(filename):
    pass

def modify_fx_in_file(filename):
    pass

def modify_rope_in_file(filename):
    pass



def randomize():
    directory = './randomlevels'

    messagebox.showinfo("Randomizing", "This process will take a while. Just be patient and wait.\nPRESS OK TO START\nPOPUP will apear when everything is done!")

    if not os.path.exists('./snap'):
        messagebox.showinfo("Randomizing", "SAVE ORIGINAL FIRST!!!!!!!!")
        return

    j = 0
    for folder in os.listdir(directory):
        if int(lvl[j].get()) == 1:
            for filename in os.listdir(directory + '/' + folder + '/'):
                if filename.endswith('.EXPORT.TXT'):
                    
                    if rigid_instances_var.get() == 1:
                        modify_rigid_in_file(os.path.join(directory, folder, filename))
                    if npc_var.get() == 1:
                        modify_npc_in_file(os.path.join(directory, folder, filename))
                    if pickup_var.get() == 1:
                        modify_pickup_in_file(os.path.join(directory, folder, filename))
                    if save_pedestal_var.get() == 1:
                        modify_save_in_file(os.path.join(directory, folder, filename))
                    if volume_var.get() == 1:
                        modify_volume_in_file(os.path.join(directory, folder, filename))
                    if load_trigger_var.get() == 1:
                        modify_trigger_in_file(os.path.join(directory, folder, filename))
                    if treasure_chest_var.get() == 1:
                        modify_chest_in_file(os.path.join(directory, folder, filename))
                    if fx_object_var.get() == 1:
                        modify_fx_in_file(os.path.join(directory, folder, filename))
                    if rope_var.get() == 1:
                        modify_rope_in_file(os.path.join(directory, folder, filename))
        j+=1

    convert_pack_and_move()
    messagebox.showinfo("Randomizing", "Done!\nYou can now open your game and see results!")


def convert_pack_and_move():

    batch_file = r"pack_dfs_Drag'n'Drop.bat" 
    destination_dir = "../"
    directory = './randomlevels'

    j = 0
    
    print('start')
    for folder in os.listdir(directory):
        if int(lvl[j].get()) == 1:
            for filename in os.listdir(directory + '/' + folder + '/'):
                if filename.endswith(".EXPORT.TXT") and os.path.getsize(directory + '/' + folder + '/' + filename) != 0 :
                    input_file = directory + '/' + folder + '/' + filename
                    
                    try:
                        subprocess.run(["./exporttool.exe", "-c", input_file], capture_output=True)
                        # subprocess.run(["./exportcompile.bat", input_file], shell=True, capture_output=True)
                    except Exception as e:
                        print("Something is wrong, probably you've messed up in" + filename )
                        print(e)
                        return
                    
                    output_file = './randomlevels/' + folder + '/'  + filename 
                    fin_output_file = './levelssnapshot/' + folder + '/LEVELS/' + level_dict[folder] + '/'  + filename.replace('.TXT', '') 
                    output_file = output_file.replace('.TXT', '')
                    print(output_file)

                    shutil.move(output_file, fin_output_file)

            folder_path = './levelssnapshot/' + folder
            folder_name = folder
            try:
                subprocess.run([batch_file, folder_path], shell=True)
            except Exception as e:
                print("Something wrong with packing level")
                print(e)

            generated_files = [folder_name + ".DFS", folder_name + ".000"]

            for file in generated_files:
                try:
                    shutil.move(file, os.path.join(destination_dir, file))
                except Exception as e:
                    print("Couldnt move to game folder")
                    print(e)
                
                print ( file, "moved")
        j+=1            



def copy_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        if not (  filename.startswith('audio') or filename.startswith('boot') or filename.startswith('common') ) and (filename.endswith('.dfs') or filename.endswith('.000') or filename.endswith('.DFS')) :
            # Create the full file paths for the source and destination
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)

            # Copy the file to the destination folder
            shutil.copy2(source_file, destination_file)


def convert_to_txt(input_folder, output_folder):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    for filename in os.listdir(input_folder):
        if filename.endswith(".EXPORT") and os.path.getsize(input_folder + '/' + filename) != 0:
            try: 
                print(filename)
                print()
                input_file = os.path.join(input_folder, filename)
                # Set the output file path in the output folder
                output_file = os.path.join(output_folder, filename + ".TXT")
                
                # Run the command using subprocess
                # subprocess.run(["exporttool.exe", "-d", input_file], capture_output=True)
                subprocess.run(["exportdecompile.bat", input_file], shell=True, capture_output=True)
                
                # Move the output file to the output folder
                shutil.move(input_folder + '/' + filename+".TXT", output_file)
            except Exception as e:
                print("An error occurred:", str(e))


def save_snaphot():
    messagebox.showinfo("Saving snapshot", "This process will take a while. Just be patient and wait.\nPRESS OK TO START\nPOPUP will apear when everything is done!")
    input_folder = "../"

    output_folder = "./snap"
    copy_files(input_folder, output_folder)

    output_folder = "./levelssnapshot"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # undfs_path = os.getcwd() + '\\snap\\undfs.exe'
    undfs_path = os.getcwd() + '\\snap\\unpack.bat'
    print(undfs_path)

    shutil.copy('./undfs.exe', './snap/undfs.exe')
    shutil.copy('./unpack.bat', './snap/unpack.bat')
    for filename in os.listdir('./snap'):
        if not (  filename.startswith('audio') or filename.startswith('boot') or filename.startswith('common') ) and (filename.endswith('.dfs') or filename.endswith('.DFS')) :
            print(filename)
            command = [undfs_path, os.getcwd() + '\\snap\\' + filename]
            print(undfs_path)
            print(os.getcwd() + '\\snap\\' + filename)
            print(subprocess.run(command, shell=True))
            common_source = './COMMON'
            level_source =  './LEVELS'
            shutil.move(common_source, './levelssnapshot/' + filename.split('.')[0] + '/COMMON' )
            shutil.move(level_source,  './levelssnapshot/' + filename.split('.')[0] + '/LEVELS' )
            
    
    output_folder = "./randomlevels"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    unpack_for_random()

    messagebox.showinfo("Saving snapshot", "Done!")
    pass

def unpack_for_random():
    folder = "./randomlevels"

    for filename in os.listdir('./levelssnapshot'): 
        for f in os.listdir('./levelssnapshot/' + filename + '/LEVELS'): 
            convert_to_txt('./levelssnapshot/' + filename + '/LEVELS/' + f , './randomlevels/' + filename + "/" )


def favourite():
    if not os.path.exists('./favourite'):
        messagebox.showinfo("favourite", "save favourite first!!!!")
        return

    copy_files('./favourite' ,  '../')
    messagebox.showinfo("Load favourite", "Done")

def start_game():
    randomize()

def preview():
    messagebox.showinfo("Preview", "Not yet implemented")
    pass

#########################################################################

# Create the main window
window = tk.Tk()
window.title("Hobbit Randomizer by Mr_Kliff v1.1")

# Get the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the window size based on screen dimensions
window_width = int(screen_width * 0.5)  
window_height = int(screen_height * 0.65)  

# Set the window size and position in the center of the screen
window.geometry(f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

window.configure(bg="white")

window.resizable(True, True)

# Set margin for all elements
margin = 10

# Create a separate row for column titles
column_title_row = 0

# Define variables to store tickbox and entry field values
rigid_instances_var = tk.BooleanVar()
npc_var = tk.BooleanVar()
pickup_var = tk.BooleanVar()
save_pedestal_var = tk.BooleanVar()
volume_var = tk.BooleanVar()
load_trigger_var = tk.BooleanVar()
treasure_chest_var = tk.BooleanVar()
fx_object_var = tk.BooleanVar()
rope_var = tk.BooleanVar()

rigid_instances_var.set(True)


posx_var = tk.StringVar(value="300")
posy_var = tk.StringVar(value="400")
posz_var = tk.StringVar(value="200")
orientx_var = tk.StringVar(value="100")
orienty_var = tk.StringVar(value="0")
orientz_var = tk.StringVar(value="0")


#Level list variables
lvl = [tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),
tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar()]
lvl[0].set(True)


# Create checkboxes for RigidInstances and NPC
rigid_instances_checkbox = tk.Checkbutton(window, text="RigidInstances", fg="black", bg="white", anchor="w", justify="left", variable=rigid_instances_var)
rigid_instances_checkbox.grid(row=column_title_row + 1, column=1, padx=margin, pady=margin, sticky="w")

npc_checkbox = tk.Checkbutton(window, text="NPC", fg="black", bg="white", anchor="w", justify="left", variable=npc_var)
npc_checkbox.grid(row=column_title_row + 2, column=1, padx=margin, pady=margin, sticky="w")

pickup_checkbox = tk.Checkbutton(window, text="Pickup", fg="black", bg="white", anchor="w", justify="left", variable=pickup_var)
pickup_checkbox.grid(row=column_title_row + 1, column=2, padx=margin, pady=margin, sticky="w")

save_pedestal_checkbox = tk.Checkbutton(window, text="SavePedestal", fg="black", bg="white", anchor="w", justify="left", variable=save_pedestal_var)
save_pedestal_checkbox.grid(row=column_title_row + 2, column=2, padx=margin, pady=margin, sticky="w")

volume_checkbox = tk.Checkbutton(window, text="Volume", fg="black", bg="white", anchor="w", justify="left", variable=volume_var)
volume_checkbox.grid(row=column_title_row + 3, column=2, padx=margin, pady=margin, sticky="w")

load_trigger_checkbox = tk.Checkbutton(window, text="LoadTrigger", fg="black", bg="white", anchor="w", justify="left", variable=load_trigger_var)
load_trigger_checkbox.grid(row=column_title_row + 4, column=2, padx=margin, pady=margin, sticky="w")

treasure_chest_checkbox = tk.Checkbutton(window, text="TreasureChest", fg="black", bg="white", anchor="w", justify="left", variable=treasure_chest_var)
treasure_chest_checkbox.grid(row=column_title_row + 5, column=2, padx=margin, pady=margin, sticky="w")

fx_object_checkbox = tk.Checkbutton(window, text="FXObject", fg="black", bg="white", anchor="w", justify="left", variable=fx_object_var)
fx_object_checkbox.grid(row=column_title_row + 6, column=2, padx=margin, pady=margin, sticky="w")

rope_checkbox = tk.Checkbutton(window, text="Rope", fg="black", bg="white", anchor="w", justify="left", variable=rope_var)
rope_checkbox.grid(row=column_title_row + 7, column=2, padx=margin, pady=margin, sticky="w")

# Create a "Start" button
start_button = tk.Button(window, text="RANDOMNESS!!!", command=start_game, fg="black", bg="white")
start_button.grid(row=column_title_row + 1, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(start_button, msg="Randomize the game with parameters you made!")

# Create a "Save Snapshot" button
randomize_button = tk.Button(window, text="SAVE ORIGINAL GAME!", command=save_snaphot, fg="black", bg="white")
randomize_button.grid(row=column_title_row + 2, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(randomize_button, msg="You are saving the current state of your game\nIt's a full snapshot of it\nso you can recover later on")

# Create a "Save Favourite" button
save_button = tk.Button(window, text="Save to Favourite", command=save_levels, fg="black", bg="white") 
save_button.grid(row=column_title_row + 3, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(save_button, msg="Save the current state of your levels\nif you like it\n(aka backup of what you have now)")

# Create a "Load Favourite" button
load_your_favorite = tk.Button(window, text="Load your favourite", command=favourite, fg="black", bg="white")
load_your_favorite.grid(row=column_title_row + 4, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(load_your_favorite, msg="Will load the game that you marked as\nyour favorite")

# Create a "Reset" button
reset_button = tk.Button(window, text="Reset", command=reset_game, fg="black", bg="white")
reset_button.grid(row=column_title_row + 5, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(reset_button, msg="Reset the game to the very first state\nthat you saved with ORIGINAL button")

# Create a "Preview" button
preview_button = tk.Button(window, text="Preview", command=preview, fg="black", bg="white")
preview_button.grid(row=column_title_row + 6, column=3, padx=margin, pady=margin, sticky="w")
ToolTip(preview_button, msg="Preview selected levels")

# Create labels and entry fields for the offsets
offsets_label = tk.Label(window, text="A value from -entered to +entered\nwill be randomly added\nto selected  types of objects", fg="black", bg="white")
offsets_label.grid(row=column_title_row + 1, column=6, padx=margin, pady=margin, sticky="w")

pos_label = tk.Label(window, text="Pos:", fg="black", bg="white")
pos_label.grid(row=column_title_row + 2, column=4, padx=margin, pady=margin, sticky="w")

posx_label = tk.Label(window, text="X:", fg="black", bg="white")
posx_label.grid(row=column_title_row + 2, column=5, padx=margin, pady=margin, sticky="w")

posx_entry = tk.Entry(window, textvariable=posx_var)
posx_entry.grid(row=column_title_row + 2, column=6, padx=margin, pady=margin)

posy_label = tk.Label(window, text="Y:", fg="black", bg="white")
posy_label.grid(row=column_title_row + 3, column=5, padx=margin, pady=margin, sticky="w")

posy_entry = tk.Entry(window, textvariable=posy_var)
posy_entry.grid(row=column_title_row + 3, column=6, padx=margin, pady=margin)

posz_label = tk.Label(window, text="Z:", fg="black", bg="white")
posz_label.grid(row=column_title_row + 4, column=5, padx=margin, pady=margin, sticky="w")

posz_entry = tk.Entry(window, textvariable=posz_var)
posz_entry.grid(row=column_title_row + 4, column=6, padx=margin, pady=margin)

rot_label = tk.Label(window, text="Rot:", fg="black", bg="white")
rot_label.grid(row=column_title_row + 5, column=4, padx=margin, pady=margin, sticky="w")

rotx_label = tk.Label(window, text="X:", fg="black", bg="white")
rotx_label.grid(row=column_title_row + 5, column=5, padx=margin, pady=margin, sticky="w")

rotx_entry = tk.Entry(window, textvariable=orientx_var)
rotx_entry.grid(row=column_title_row + 5, column=6, padx=margin, pady=margin)

roty_label = tk.Label(window, text="Y:", fg="black", bg="white")
roty_label.grid(row=column_title_row + 6, column=5, padx=margin, pady=margin, sticky="w")

roty_entry = tk.Entry(window, textvariable=orienty_var)
roty_entry.grid(row=column_title_row + 6, column=6, padx=margin, pady=margin)

rotz_label = tk.Label(window, text="Z:", fg="black", bg="white")
rotz_label.grid(row=column_title_row + 7, column=5, padx=margin, pady=margin, sticky="w")

rotz_entry = tk.Entry(window, textvariable=orientz_var)
rotz_entry.grid(row=column_title_row + 7, column=6, padx=margin, pady=margin)

# Create column titles
options_column_title = tk.Label(window, text="Options\n(only rigids work)", fg="black", bg="white", font=("Arial", 12, "bold"))
options_column_title.grid(row=column_title_row, column=1, padx=margin, pady=margin, sticky="w")

actions_column_title = tk.Label(window, text="Actions", fg="black", bg="white", font=("Arial", 12, "bold"))
actions_column_title.grid(row=column_title_row, column=3, padx=margin, pady=margin, sticky="w")

offsets_column_title = tk.Label(window, text="Offsets", fg="black", bg="white", font=("Arial", 12, "bold"))
offsets_column_title.grid(row=column_title_row, column=4, padx=margin, pady=margin, sticky="w")

levels = tk.Label(window, text="Levels", fg="black", bg="white", font=("Arial", 12, "bold"))
levels.grid(row=9, column=1, padx=margin, pady=margin, sticky="w")


num_levels = 12
levels_per_column = 3

level_checkboxes = []

level_names = [ "Dream World",
   "Hobbiton",
   "Roast Mutton",
   "Troll Hole",
   "Overhill",
   "Swordlight",
   "Mirkwood",
   "Barrels Out Of Bond",
   "Laketown",
   "Smaug",
   "Lonely Mountain",
   "Clouds Burst"]


master_checkbox_var = tk.IntVar()

def toggle_level_checkboxes():
    checkbox_state = master_checkbox_var.get()
    for checkbox in level_checkboxes:
        if checkbox_state:
            checkbox.select()  # Select the checkbox
        else:
            checkbox.deselect()  # Deselect the checkbox


master_checkbox = tk.Checkbutton(
    window, text="Select All", variable=master_checkbox_var,
    command=toggle_level_checkboxes
)
master_checkbox.grid(row=9, column=2, padx=margin, pady=margin, sticky="w")

for i in range(num_levels):
    level_checkbox = tk.Checkbutton(window, text=level_names[i], fg="black", bg="white", variable=lvl[i])
    level_checkbox.grid(row=column_title_row + (i // levels_per_column) + 10, column=(i % levels_per_column) + 1, padx=margin, pady=margin, sticky="w")
    level_checkboxes.append(level_checkbox)


# Create a horizontal line
horizontal_line = tk.Canvas(window, width=700, height=1, bg="black")
horizontal_line.create_line(0, 0, 700, 0, fill="black")
horizontal_line.grid(row=8, column=1, columnspan=6, padx=margin, pady=margin, sticky="w")

# Create a label for the name
name_label = tk.Label(window, text="The Hobbit Randomizer", fg="black", bg="white", font=("Arial", 22, "bold"))
name_label.grid(row=9, column=3, columnspan=3, padx=margin, pady=margin-10)

# Start the Tkinter event loop
window.mainloop()