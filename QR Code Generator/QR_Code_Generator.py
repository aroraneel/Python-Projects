# Import the qrcode library.
# This library is used to create QR codes.
import qrcode

# Take text or a URL as input from the user.
text = input("Enter text or URL: ")

# Generate a QR code using the entered text or URL.
qr = qrcode.make(text)

# Set the name of the output image file.
filename = "qrcode.png"

# Save the generated QR code as a PNG image.
qr.save(filename)

# Display a success message after saving the file.
print("QR Code saved as", filename)