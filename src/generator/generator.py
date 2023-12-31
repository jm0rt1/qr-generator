import qrcode
from PIL import Image


class QRCodeGenerator:
    def __init__(self, data):
        self.data = data

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        self.qr_image = qr.make_image(fill_color="black", back_color="white")

    def add_logo(self, logo_path):

        logo = Image.open(logo_path)
        logo.show()
        # Calculate logo size, keeping aspect ratio
        max_size = min(self.qr_image.size) // 3
        aspect_ratio = logo.size[0] / logo.size[1]
        if logo.size[0] > logo.size[1]:
            logo_size = (max_size, int(max_size / aspect_ratio))
        else:
            logo_size = (int(max_size * aspect_ratio), max_size)

        logo = logo.resize(logo_size, Image.BICUBIC)
        logo.show()
        img_w, img_h = self.qr_image.size
        logo_w, logo_h = logo.size
        offset = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
        self.qr_image = self.qr_image.convert(logo.mode)

        self.qr_image.paste(logo, offset)

    def save_qr_code(self):
        self.qr_image.save("./output/qr_code.png")

    def display_qr_code(self):
        self.qr_image.show()


def generate():
    input_data = input("Enter data to encode: ")
    qr_generator = QRCodeGenerator(input_data)
    qr_generator.generate_qr_code()
    qr_generator.add_logo("./input/logo.png")
    qr_generator.save_qr_code()
    qr_generator.display_qr_code()
