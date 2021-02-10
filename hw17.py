import exifread


def convert_ratio_to_number(ratio):
    try:
        number = eval(str(ratio))
    except ZeroDivisionError:
        number = 0
    finally:
        return number


def write_coordinates_to_csv(file, coordinates):
    with open(file, 'a') as csv:
        csv.write(";".join(str(x) for x in coordinates))


def read_exif(path_to_image):
    with open(path_to_image, "rb") as file:
        return exifread.process_file(file)


def get_coordinates(exif):
    if 'GPS GPSLatitude' and 'GPS GPSLongitude' in exif.keys():
        latitude = [convert_ratio_to_number(x) for x in exif['GPS GPSLatitude'].values]
        longitude = [convert_ratio_to_number(x) for x in exif['GPS GPSLongitude'].values]

        lat_dec_format = latitude[0] + latitude[1] / 60 + latitude[2] / 3600
        lon_dec_format = longitude[0] + longitude[1] / 60 + longitude[2] / 3600

        return lat_dec_format, lon_dec_format

    return 0, 0

def main():
    exif = read_exif("files/photos/7.jpg")
    coordinates = get_coordinates(exif)
    write_coordinates_to_csv("files/coordinates.csv", coordinates)


if __name__ == '__main__':
    main()
