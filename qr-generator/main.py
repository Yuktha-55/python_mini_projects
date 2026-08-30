import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


# Function to generate and display QR code
def generateCode():

    data = text.get().strip()

    # Check if input is empty
    if data == "":
        messagebox.showerror(
            "Error",
            "Please enter a URL or text."
        )
        return

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create QR image
    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    # Convert image for Tkinter
    qr_image = ImageTk.PhotoImage(img)

    # Display image
    qrLabel.config(image=qr_image)
    qrLabel.image = qr_image


# Create window
wn = Tk()

wn.title("QR Code Generator")
wn.geometry("700x650")
wn.config(bg="light blue")


# Heading
headingLabel = Label(
    wn,
    text="QR Code Generator",
    bg="light blue",
    fg="black",
    font=("Times", 22, "bold")
)

headingLabel.pack(pady=20)


# Input label
label1 = Label(
    wn,
    text="Enter Text or URL:",
    bg="light blue",
    fg="black",
    font=("Courier", 13, "bold")
)

label1.pack(pady=10)


# Input box
text = Entry(
    wn,
    font=("Century", 14),
    width=50
)

text.pack(pady=10)


# Generate button
button = Button(
    wn,
    text="Generate QR Code",
    font=("Courier", 14, "bold"),
    command=generateCode
)

button.pack(pady=20)


# Label to display QR code
qrLabel = Label(
    wn,
    bg="light blue"
)

qrLabel.pack(pady=10)


# Run window
wn.mainloop()