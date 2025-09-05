import qrcode

data = input("Enter the data or URL to encode in the QR code: ").strip()
filename = input("Enter the filename to save the QR code: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}") 


# remember to activate the virtual environment (venv) before running the scriptdeactde
# use the below commande to activate the env:
#   pythone1 git:(main) ✗ source venv/bin/activate
# (venv) ➜  pythone1 git:(main) ✗ python qr_code_generator.py
# when you are done, remember to deactivate the venv using the command: deactivate