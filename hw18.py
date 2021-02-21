from PIL import Image


class Miniature:

    def __init__(self, image):
        self.image = image

    def create(self, size):
        with Image.open(self.image) as img:
            img.thumbnail(size)
            img_name = self.image.split('/')[-1]
            img.save(f'files/photos/minis/mini_{img_name}')


def main():
    mini = Miniature("files/photos/8.jpg")
    mini.create((200, 200))


if __name__ == '__main__':
    main()
