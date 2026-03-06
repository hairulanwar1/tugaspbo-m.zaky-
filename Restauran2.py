class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang buka!")


restaurant1 = Restaurant("Bakso Pak Kumis", "Bakso")
restaurant2 = Restaurant("Ayam Geprek Bensu", "Ayam Geprek")
restaurant3 = Restaurant("Sushi Tei", "Japanese Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()