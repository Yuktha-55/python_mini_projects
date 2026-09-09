import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


# ---------------- QR GENERATOR FUNCTION ----------------

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    qr_image = ImageTk.PhotoImage(img)

    qrLabel.config(image=qr_image)
    qrLabel.image = qr_image


# ---------------- URL QR ----------------

def generate_url():
    url = text.get().strip()

    if url == "":
        messagebox.showerror("Error", "Please enter a URL.")
        return

    generate_qr(url)


# ---------------- TEXT QR ----------------

def generate_text():
    data = text.get().strip()

    if data == "":
        messagebox.showerror("Error", "Please enter some text.")
        return

    generate_qr(data)


# ---------------- WIFI QR ----------------

def generate_wifi():

    wifi_name = ssid.get().strip()
    wifi_password = password.get().strip()
    security = security_type.get()

    if wifi_name == "":
        messagebox.showerror(
            "Error",
            "Please enter the Wi-Fi name."
        )
        return

    if security != "nopass" and wifi_password == "":
        messagebox.showerror(
            "Error",
            "Please enter the Wi-Fi password."
        )
        return

    # Standard Wi-Fi QR format
    wifi_data = f"WIFI:T:{security};S:{wifi_name};P:{wifi_password};;"

    generate_qr(wifi_data)


# ---------------- CHANGE INPUT FIELDS ----------------

def select_option():

    choice = option.get()

    # Hide everything first
    textFrame.pack_forget()
    wifiFrame.pack_forget()

    if choice == "URL" or choice == "Text":

        textFrame.pack(pady=10)

        if choice == "URL":
            inputLabel.config(text="Enter URL:")
        else:
            inputLabel.config(text="Enter Text:")

        generateButton.config(
            command=generate_url if choice == "URL"
            else generate_text
        )

        generateButton.pack(pady=15)

    elif choice == "WiFi":

        wifiFrame.pack(pady=10)

        generateButton.config(command=generate_wifi)

        generateButton.pack(pady=15)


# ---------------- MAIN WINDOW ----------------

wn = Tk()

wn.title("QR Code Generator")
wn.geometry("700x750")
wn.config(bg="light blue")
wn.resizable(False, False)


# ---------------- HEADING ----------------

headingLabel = Label(
    wn,
    text="QR Code Generator",
    bg="light blue",
    fg="black",
    font=("Times", 22, "bold")
)

headingLabel.pack(pady=20)


# ---------------- OPTION MENU ----------------

choiceLabel = Label(
    wn,
    text="Select QR Type:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

choiceLabel.pack(pady=5)


option = StringVar()
option.set("URL")


optionMenu = OptionMenu(
    wn,
    option,
    "URL",
    "Text",
    "WiFi",
    command=lambda x: select_option()
)

optionMenu.config(
    font=("Courier", 12),
    width=15
)

optionMenu.pack(pady=5)


# ---------------- TEXT / URL FRAME ----------------

textFrame = Frame(
    wn,
    bg="light blue"
)

inputLabel = Label(
    textFrame,
    text="Enter URL:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

inputLabel.pack(pady=5)


text = Entry(
    textFrame,
    font=("Century", 14),
    width=45
)

text.pack(pady=5)


# ---------------- WIFI FRAME ----------------

wifiFrame = Frame(
    wn,
    bg="light blue"
)


# Wi-Fi name

ssidLabel = Label(
    wifiFrame,
    text="Wi-Fi Name:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

ssidLabel.pack(pady=5)


ssid = Entry(
    wifiFrame,
    font=("Century", 14),
    width=35
)

ssid.pack(pady=5)


# Wi-Fi password

passwordLabel = Label(
    wifiFrame,
    text="Wi-Fi Password:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

passwordLabel.pack(pady=5)


password = Entry(
    wifiFrame,
    font=("Century", 14),
    width=35,
    show="*"
)

password.pack(pady=5)


# Security type

securityLabel = Label(
    wifiFrame,
    text="Security:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

securityLabel.pack(pady=5)


security_type = StringVar()
security_type.set("WPA")


securityMenu = OptionMenu(
    wifiFrame,
    security_type,
    "WPA",
    "WEP",
    "nopass"
)

securityMenu.config(
    font=("Courier", 12),
    width=15
)

securityMenu.pack(pady=5)


# ---------------- GENERATE BUTTON ----------------

generateButton = Button(
    wn,
    text="Generate QR Code",
    font=("Courier", 14, "bold"),
    command=generate_url
)

generateButton.pack(pady=15)


# ---------------- QR DISPLAY ----------------

qrLabel = Label(
    wn,
    bg="light blue"
)

qrLabel.pack(pady=10)


# ---------------- START ----------------

wn.mainloop()