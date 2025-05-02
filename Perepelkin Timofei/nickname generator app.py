import random

prefixes = [
    "Giga", "Nano", "Cyber", "Quantum", "Neo", "Aero", "Hydro", "Pyro", "Astra",
    "Electro", "Zeta", "Omega", "Luna", "Terra", "Glacio", "Helio", "Frost", "Myst"
]

suffixes = [
    "tron", "byte", "blast", "wave", "flux", "spark", "blade", "bolt", "nova", 
    "shadow", "blaze", "quake", "drift", "shade", "flare", "pulse", "strike", "zenith"
]

def generate_name():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return prefix + suffix

middles = [
    "al", "er", "ix", "ar", "on", "ia", "us", "or", "um", "ax"
]

def generate_name_advanced():
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    
    # Randomly decide if we should use a middle part
    use_middle = random.choice([True, False])
    
    if use_middle:
        middle = random.choice(middles)
        return prefix + middle + suffix
    else:
        return prefix + suffix

# Test the basic name generator
for _ in range(5):
    print(generate_name())

print("\nAdvanced Name Generator:")
# Test the advanced name generator
for _ in range(5):
    print(generate_name_advanced())




from tkinter import *  
def clicked():  
    lbl.configure(text=generate_name_advanced())  

window = Tk()  
window.title("Welcome to the nickname generator app ")  
window.geometry('10000x5000')  
lbl = Label(window, text="Do you want a new nickname?", font=("Courier New", 30*2))  
lbl.grid(column=0, row=0)  
btn = Button(window, text="Нажми!", command=clicked)  
btn.grid(column=1, row=0)  
window.mainloop()

  
  
  
 
  
  
