#imports used
import pyttsx3
import webcolors
import webcolors
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

#TEXT TO SPEACH
# initalize
engine = pyttsx3.init()
# set properties speed and volume
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)  
# text on screen
text = "Color Accessibility. Filter. Red green friendly on. Blue yellow friendly off. High contrast mode off. Customize Color Pallet on. Font. Dyslexic font off. Large font off. Flash freese mode off."
engine.say(text)
engine.runAndWait()
#HCI PRINCIPAL: Here, I followed the ideas of anthropomorphism by trying to make the screen reader's speech match that of a human's. I did this by including natural pauses between sections. To achieve this, I put a period after each option available to the user to mimic how a human would read off the options, pausing in between each to signal to the listener that they are separate and therefore separate options. I also made sure the tone and speed of the speech being read were natural to a human—not too slow and not too fast, not too loud and not too quiet.

#COLOR CONTRAST CHECKER
#converts a HEX color to RGB
def hex_to_rgb(hex_color):
    return webcolors.hex_to_rgb(hex_color)
#luminace of color + color correction
def luminance(rgb):
    r, g, b = [x / 255.0 for x in rgb]
    
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

    return 0.2126 * r + 0.7152 * g + 0.0722 * b

#OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. https://chat.openai.com/chat
#I used AI to help me with the logic for the def luminance method and how to implement this aspect into my code. 

#contrast between colors for LIGHT MODE
def contrast_ratio(color1, color2):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    luminance1 = luminance(rgb1)
    luminance2 = luminance(rgb2)
    # note that luminance1 should be lighter
    if luminance1 < luminance2:
        luminance1, luminance2 = luminance2, luminance1
    return (luminance1 + 0.05) / (luminance2 + 0.05)
#contrast ratio
def is_accessible(color1, color2):
    ratio = contrast_ratio(color1, color2)
    print("Light Mode")
    print(f"Contrast ratio: {ratio:.2f}")
    if ratio >= 7.0:
        return "Accessible (AAA)"
    elif ratio >= 4.5:
        return "Accessible (AA)"
    else:
        return "Not Accessible"
#colors for light mode (as seen in prototype)
color1 = "#FFFFFF"  #backgound (white)
color2 = "#000000"  #text (black)

#contrast between colors for DARK MODE
def contrast_ratio2(color3, color4):
    rgb3 = hex_to_rgb(color3)
    rgb4 = hex_to_rgb(color4)

    luminance3 = luminance(rgb3)
    luminance4 = luminance(rgb4)

    # luminance1 should be lighter
    if luminance3 < luminance4:
        luminance3, luminance4 = luminance4, luminance3
    return (luminance3 + 0.05) / (luminance4 + 0.05)
#contrast ratio
def is_accessible2(color3, color4):
    ratio = contrast_ratio2(color3, color4)
    print("Dark Mode")
    print(f"Contrast ratio: {ratio:.2f}")
    
    #HCI PRINICPAL:Here, I followed the Web Content Accessibility Guidelines (WCAG) regarding the contrast needed. Although there is no perfect ratio, it states that we should strive for a minimum of 4.5, but 7 is better and preferred. The three levels of WCAG conformance are A, AA, and AAA. They are used to rank conformance to guidelines. These ratios both receive a AAA, the best possible result, as they have the highest level of conformance and are exceptionally accessible. They meet the minimum contrast ratio for text to background at 7:1.
    #Cite: I used W3Schools to learn about WCAG and get the WCAG values 
    #Accessibility Color Alone as Meaning. (n.d.). W3Schools. Retrieved February 24, 2025, from https://www.w3schools.com/accessibility/accessibility_color_meaning.php
    if ratio >= 7.0:
        return "Accessible (AAA)"
    elif ratio >= 4.5:
        return "Accessible (AA)"
    else:
        return "Not Accessible"
#colors for dark mode (as seen in figma)
color3 = "#1E1E1E"  # backgound (darkgrey)
color4 = "#FFFFFF"  # text (white)

result = is_accessible(color1, color2)
print(f"Accessibility result : {result}")
print(" ")

result = is_accessible2(color3, color4)
print(f"Accessibility result : {result}")

#PROTOTYPE
#button state on and off
def toggle_state(button_name):
    if button_name.get():
        print(f"{button_name} is ON")
    else:
        print(f"{button_name} is OFF")

#color picker for Customize Color Pallet
def open_color_picker(color_label):
    color = askcolor()[1]  
    if color: 
        color_label.config(bg=color)  
#title in general
root = tk.Tk()
root.title("Color Accessibility")

# the visable title
title_label = tk.Label(root, text="Color Accessibility", font=("Arial", 16, "bold"))
title_label.pack(pady=10, anchor="center")

# all options for users
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
var5 = tk.BooleanVar()
var6 = tk.BooleanVar()
var7 = tk.BooleanVar()

# title for options that can be filtered
title_label = tk.Label(root, text="     Filter", font=("Arial", 10, "bold"))
title_label.pack(pady=10, anchor="w")

toggle1 = ttk.Checkbutton(root, text="Red-Green Friendly", variable=var1, command=lambda: toggle_state("Red-Green Friendly"))
toggle1.pack(pady=5, anchor="w")

toggle2 = ttk.Checkbutton(root, text="Blue-Yellow Friendly", variable=var2, command=lambda: toggle_state("Blue-Yellow Friendly"))
toggle2.pack(pady=5, anchor="w")

toggle3 = ttk.Checkbutton(root, text="High Contrast Mode", variable=var3, command=lambda: toggle_state("High Contrast Mode"))
toggle3.pack(pady=5, anchor="w")

toggle4 = ttk.Checkbutton(root, text="Customize Color Pallet", variable=var4, command=lambda: toggle_state("Customize Color Pallet"))
toggle4.pack(pady=5, anchor="w")

#box around 5 include colors
color_pallet_frame = tk.Frame(root, relief="solid", borderwidth=2)
color_pallet_frame.pack(pady=10, anchor="w")

# color box opener and make clickable
def make_color_box_clickable(color_label):
    color_label.bind("<Button-1>", lambda event: open_color_picker(color_label))

# 5 include colors
sections = []
for i in range(5):
    section_label = tk.Label(color_pallet_frame, width=7, height=2, relief="solid", anchor="center", bg="lightgray")
    section_label.grid(row=0, column=i, padx=5, pady=5)
    make_color_box_clickable(section_label)  # Make each section clickable
    sections.append(section_label)

#OpenAI. (2023). ChatGPT (Mar 14 version) [Large language model]. https://chat.openai.com/chat
#I used AI to help me figure out how to make the boxes clickable and open up the color picker the method make_color_box_clickable.

# title for include
color_pallet_title = tk.Label(root, text="Include", font=("Arial", 10))
color_pallet_title.pack(pady=5, anchor="center")

# exclude pallet
color_pallet_frame_2 = tk.Frame(root, relief="solid", borderwidth=2)
color_pallet_frame_2.pack(pady=10, anchor="w")

# 5 colors to exclude
sections_2 = []
for i in range(5):
    section_label_2 = tk.Label(color_pallet_frame_2, width=7, height=2, relief="solid", anchor="center", bg="lightgray")
    section_label_2.grid(row=0, column=i, padx=5, pady=5)
    make_color_box_clickable(section_label_2)  # Make each section clickable
    sections_2.append(section_label_2)

#title the excude pallet
color_pallet_title_2 = tk.Label(root, text="Avoid", font=("Arial", 10))
color_pallet_title_2.pack(pady=5, anchor="center")

#title for font options
title_label = tk.Label(root, text="     Font", font=("Arial", 10, "bold"))
title_label.pack(pady=10, anchor="w")

toggle5 = ttk.Checkbutton(root, text="Dyslexic Font", variable=var5, command=lambda: toggle_state("Dyslexic Font"))
toggle5.pack(pady=5, anchor="w")

toggle6 = ttk.Checkbutton(root, text="Large Font", variable=var6, command=lambda: toggle_state("Large Font"))
toggle6.pack(pady=5, anchor="w")

toggle7 = ttk.Checkbutton(root, text="Flash Freeze / No Strobe", variable=var7, command=lambda: toggle_state("Flash Freeze / No Strobe"))
toggle7.pack(pady=5, anchor="w")

#run the whole
root.mainloop()
