import qrcode
from datetime import date

google_doc_url = "paste_link_here"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(google_doc_url)
qr.make(fit=True)
today = date.today()
print(today)

img = qr.make_image(fill="black", back_color="white")
img.save(f"program-{today}.png")
img.show()