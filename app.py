import qrcode
import sys
from datetime import date

if len(sys.argv) < 2:
    print("Usage: python app.py <url>")
    sys.exit(1)

google_doc_url = sys.argv[1]

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(google_doc_url)
qr.make(fit=True)

today = date.today()
img = qr.make_image(fill="black", back_color="white")
img.save(f"qr-{today}.png")
