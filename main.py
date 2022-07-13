from tkinter import *
from tkinter import messagebox
import random

def save():
    name = entry_name.get()
    level = spin_level.get()

    race = radio_race.get()
    if race == 1:
        race = "Human"
    elif race == 2:
        race = "Dwarf"
    elif race == 3:
        race = "Elf"

    classes = []
    if is_fighter.get():
        classes.append("Fighter")
    if is_wizard.get():
        classes.append("Wizard")
    if is_ranger.get():
        classes.append("Ranger")
    if is_rogue.get():
        classes.append("Rogue")
    if is_sorcerer.get():
        classes.append("Sorcerer")
    if is_druid.get():
        classes.append("Druid")

    classes_string = ""
    if len(classes) == 1:
        classes_string = classes[0]
    else:
        for a_class in classes:
            classes_string += a_class + "/"

    classes_string = classes_string.rstrip("/")


    str = spin_str.get()
    dex = spin_dex.get()
    con = spin_con.get()
    int = spin_int.get()
    wis = spin_wis.get()
    char = spin_char.get()
    hp = spin_hp.get()
    ac = spin_ac.get()
    xp = spin_xp.get()

    background = text_background.get("1.0", END)

    data = f"Name: {name}\n\n" \
        f"Level: {level}\n\n" \
        f"Race: {race}\n" \
        f"Class: {classes_string}\n\n" \
        f"Strength: {str}\n" \
        f"Dexterity: {dex}\n" \
        f"Constitution: {con}\n" \
        f"Intelligence: {int}\n" \
        f"Wisdom: {wis}\n" \
        f"Charisma: {char}\n" \
        f"HP: {hp}\n\n" \
        f"AC: {ac}\n" \
        f"EXP: {xp}\n\n" \
        f"Background: \n{background}"

    print(data)

    with open(f"Saved/character_sheet_{name}.txt", "w") as f:
        f.write(data)

    messagebox.showinfo(title="Export Complete", message=f"Character has been exported to character_sheet_{name}.txt")

def generate():

    entry_name.delete(0, END)

    first_name = random.choice(open("random_names.txt").readlines()).strip()
    second_name = random.choice(open("random_names.txt").readlines()).strip()

    name = first_name + " " + second_name

    entry_name.insert(0, name)

NUMERICAL_WIDTH = 3

window = Tk()
window.title("D&D Character Sheet")
window.minsize(width=400, height=600)
window.config(padx=50, pady=50)

### CANVAS FOR IMAGE

canvas = Canvas(width=200, height=200)
img_logo = PhotoImage(file="d&d_small.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=1, column=5, columnspan=5, rowspan=5)

### ROW 0 - Name and Level ###

# NAME LABEL
label_name = Label(text="Name:")
label_name.grid(row=0, column=0, sticky="W")

# NAME ENTRY
entry_name = Entry(width=20)
entry_name.grid(row=0, column=1, sticky="W", columnspan=2)

# LEVEL LABEL
label_level = Label(text="Level:")
label_level.grid(row=0, column=3, sticky="W")

# LEVEL ENTRY
spin_level = Spinbox(from_=1, to=99, width=NUMERICAL_WIDTH)
spin_level.grid(row=0, column=4, sticky="W")

### ROW 1 - Race ###

# RACE LABEL
label_race = Label(text="Race:")
label_race.grid(row=1, column=0, sticky="W", pady=10)

# RACE OPTIONS
radio_race = IntVar()
radio_race_human = Radiobutton(text="Human", value=1, variable=radio_race)
radio_race_human.grid(row=1, column=1, sticky="W")

radio_race_dwarf = Radiobutton(text="Dwarf", value=2, variable=radio_race)
radio_race_dwarf.grid(row=1, column=2, sticky="W")

radio_race_elf = Radiobutton(text="Elf", value=3, variable=radio_race)
radio_race_elf.grid(row=1, column=3, sticky="W")

### ROW 2/3 - Class

label_class = Label(text="Class:")
label_class.grid(row=2, column=0, sticky="W", columnspan=2)

is_fighter = IntVar()
check_class_fighter = Checkbutton(text="Fighter", variable=is_fighter)
check_class_fighter.grid(row=2, column=1, sticky="W")

is_wizard = IntVar()
check_class_wizard = Checkbutton(text="Wizard", variable=is_wizard)
check_class_wizard.grid(row=2, column=2, sticky="W")

is_ranger = IntVar()
check_class_ranger = Checkbutton(text="Ranger", variable=is_ranger)
check_class_ranger.grid(row=2, column=3, sticky="W")

is_rogue = IntVar()
check_class_rogue = Checkbutton(text="Rogue", variable=is_rogue)
check_class_rogue.grid(row=3, column=1, sticky="W")

is_sorcerer = IntVar()
check_class_sorcerer = Checkbutton(text="Sorcerer", variable=is_sorcerer)
check_class_sorcerer.grid(row=3, column=2, sticky="W")

is_druid = IntVar()
check_class_druid = Checkbutton(text="Druid", variable=is_druid)
check_class_druid.grid(row=3, column=3, sticky="W")

### ROW 4 - Allignment Slider

### ROW 5+ - Attributes

label_str = Label(text="Strength:")
label_str.grid(row=5, column=0, sticky="W")
spin_str = Spinbox(from_=0, to=30, width=3)
spin_str.grid(row=5, column=1, sticky="W")

label_dex = Label(text="Dexterity:")
label_dex.grid(row=6, column=0, sticky="W")
spin_dex = Spinbox(from_=0, to=30, width=3)
spin_dex.grid(row=6, column=1, sticky="W")

label_con = Label(text="Constitution:")
label_con.grid(row=7, column=0, sticky="W")
spin_con = Spinbox(from_=0, to=30, width=3)
spin_con.grid(row=7, column=1, sticky="W")

label_int = Label(text="Intelligence:")
label_int.grid(row=8, column=0, sticky="W")
spin_int = Spinbox(from_=0, to=30, width=3)
spin_int.grid(row=8, column=1, sticky="W")

label_wis = Label(text="Wisdom:")
label_wis.grid(row=9, column=0, sticky="W")
spin_wis = Spinbox(from_=0, to=30, width=3)
spin_wis.grid(row=9, column=1, sticky="W")

label_char = Label(text="Charisma:")
label_char.grid(row=10, column=0, sticky="W")
spin_char = Spinbox(from_=0, to=30, width=3)
spin_char.grid(row=10, column=1, sticky="W")

label_hp = Label(text="HP:")
label_hp.grid(row=5, column=3, sticky="W")
spin_hp = Spinbox(from_=0, to=999, width=4)
spin_hp.grid(row=5, column=4, sticky="W")

label_ac = Label(text="AC:")
label_ac.grid(row=6, column=3, sticky="W")
spin_ac = Spinbox(from_=0, to=99, width=4)
spin_ac.grid(row=6, column=4, sticky="W")

label_xp = Label(text="EXP:")
label_xp.grid(row=8, column=3, sticky="W")
spin_xp = Spinbox(from_=0, to=9999, width=4)
spin_xp.grid(row=8, column=4, sticky="W")

### ROW 11 - Items
label_equipment = Label(text="Equipment:")
label_equipment.grid(row=11, column=0, sticky="W")

list_equipment = Listbox(height=10)
equipment = ["Sword", "Shield", "Armour", "Rope", "Lamp", "Bag"]
for item in equipment:
    list_equipment.insert(equipment.index(item), item)
#list_equipment.bind("<<ListboxSelect>>", list_items_used)
list_equipment.grid(row=11, column=1, sticky="W", columnspan=2)

### ROW 11 - Generate and Save
but_save = Button(text="Save", width=10, height=5, command=save, bg="red")
but_save.grid(row=11, column=4, padx=20)

but_generate = Button(text="Generate", width=10, height=5, command=generate, bg="green")
but_generate.grid(row=11, column=5)


### ROW 12 - Background
label_background = Label(text="Background:")
label_background.grid(row=12, column=0, sticky="W")

text_background = Text(height=10, width=40)
text_background.grid(row=12, column=1, columnspan=10, sticky="W")

window.mainloop()