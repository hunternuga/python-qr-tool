from flask import Flask, request, send_file, render_template
import qrcode
from io import BytesIO
from datetime import date
import base64
import os

app = Flask(__name__)
app.template_folder = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["GET", "POST"])
def generate_qr():
    qr_img_url = None
    url = None
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill="black", back_color="white")
            
            # Save image to BytesIO for preview
            img_io = BytesIO()
            img.save(img_io, "PNG")
            img_io.seek(0)
            
            qr_img_url = "data:image/png;base64," + base64.b64encode(img_io.getvalue()).decode()

    return render_template('app.html', qr_img=qr_img_url, url=url)

@app.route("/download")
def download_qr():
    url = request.args.get("url")
    if not url:
        return "Missing URL parameter", 400
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)
    
    today = date.today().isoformat()
    filename = f"qr-{today}.png"
    
    return send_file(img_io, mimetype="image/png", download_name=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
