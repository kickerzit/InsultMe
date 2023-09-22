import requests
from tkinter import *

# Okno
window = Tk()
window.minsize(300, 300)
window.resizable(False, False)
window.title("Aplikace na urážky")
window.config(bg="#172026")

# Funkce
def insult_me():
    user_language = drop_down_lang.get()
    my_parameters = {
        "lang": user_language,
        "type": "json"
    }

    response = requests.get("https://evilinsult.com/generate_insult.php", params=my_parameters) # za otazníkem jsou parametry: nazev_parametru=hodnota_parametru&nazev=hodnota
    response.raise_for_status()
    data = response.json()
    insult_label.config(text=data["insult"])

# Roletka - jazyk urážek
drop_down_lang = StringVar(window)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(window, drop_down_lang, "en", "es", "fr", "cs")
drop_down_lang_options.config(bg="#04BFAD", fg="white", font=("Arial", 12))
drop_down_lang_options.pack(pady=10)


# Tlačítko
insult_button = Button(text="Chci urazit", command=insult_me, bg="#027373", fg="white", font=("Arial", 12))
insult_button.pack(pady=10)

# padx, pady - vnější okraje od rámečku/hrany směrem dál
# ipadx, ipady - vnitřní okraje  

# Label
insult_label = Label(wraplength=250, bg="#172026", fg="#5FCDD9", font=("Arial", 14)) # wraplength=250 - zalomení po 250. znacích
insult_label.pack()


# Hlavní cyklus
window.mainloop()









# evilinsult.com/api
# import requests

# lang = en, es, fr, cs
# Jak zadávat parametry:
# 1. ruční zadání

# 2. pomocí proměnné = "en"
# language = "en"
# přidáme do url requestu místo lang=en => {language}

# 3. pomocí dictionary (nejvíce používaný, nejelegantnější)


""" my_parameters = {
    "lang": "en",
    "type": "json"
}
# přidat do url , params=my_parameters

response = requests.get("https://evilinsult.com/generate_insult.php", params=my_parameters) # za otazníkem jsou parametry: nazev_parametru=hodnota_parametru&nazev=hodnota
response.raise_for_status()
data = response.json()

print(data["insult"]) """