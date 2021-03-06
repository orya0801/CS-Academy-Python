from PIL import Image
import os


class Miniature:

    def __init__(self, image):
        self.image = image
        self.default_path = 'files/photos/minis'

    def create(self, size):
        with Image.open(self.image) as img:
            img.thumbnail(size)
            img_name = self.image.split('/')[-1]

            if not os.path.exists(self.default_path):
                os.makedirs(self.default_path)

            img.save(f'{self.default_path}/mini_{img_name}')


def main():
    mini = Miniature("files/photos/8.jpg")
    mini.create((200, 200))


if __name__ == '__main__':
    main()
