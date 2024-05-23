import qrcode
import os

# URL to be encoded in the QR code
url = "https://www.jmaquatics.com/"

# Generate QR code
img = qrcode.make(url)

# Save the image to a file
# Use a directory where you have write permissions
save_directory = os.path.expanduser("~")  # This points to the user's home directory
img_path = os.path.join(save_directory, "jmaquatics_qr.png")

# Save the QR code image
img.save(img_path)

print(f"QR code generated and saved to {img_path}")
