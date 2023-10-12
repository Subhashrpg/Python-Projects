import qrcode

# first qr code
# qr = qrcode.make("My first qr code")
# qr.save("user.png")

# making layout
qr1 = qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_M,box_size=10,border=5)

# # adding data
qr1.add_data("https://www.google.com")
qr1.make(fit=True)

# # making image and saving
img = qr1.make_image(fill_color="black",back_color="white")
img.save("google.png")

# # showing qrcode
img.show()