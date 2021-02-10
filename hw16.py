from geopy.geocoders import Nominatim
import csv


class LocationHandler:

    def __init__(self, lat, lon, nominatim):
        self.nominatim = nominatim
        self.latitude = lat
        self.longitude = lon
        self.location = {}

    def find_location(self, lang="ru"):
        coordinates = f"{self.latitude}, {self.longitude}"

        try:
            self.location = self.nominatim.reverse(coordinates, language=lang).raw
            return self.location

        except:
            print("Something went wrong. Trying again...")
            return self.find_location(lang)

    def get_location_info(self):
        if self.location is not None:
            return self.location['display_name']
        else:
            print("Location is empty! Use find_location() to get location info!")

    def generate_google_maps_link(self):
        if self.location is not None:
            return f"https://www.google.com/maps/search/?api=1&query={self.location['lat']},{self.location['lon']}"
        else:
            print("Location is empty! Use find_location() to get location info!")


def read_coordinates_from_csv(file, delimiter=";"):
    with open(file) as f:
        reader = csv.reader(f, delimiter=delimiter)
        next(reader, None)  # skip headers
        data = [row for row in reader]

    return data


def main():
    data = read_coordinates_from_csv("files/coordinates.csv")
    nominatim = Nominatim(user_agent="oreldan")

    for elem in data:
        lh = LocationHandler(float(elem[0]), float(elem[1]), nominatim)
        lh.find_location()
        print(f"Location: {lh.get_location_info()}")
        print(f"Google Maps URL: {lh.generate_google_maps_link()}\n")


if __name__ == "__main__":
    main()
