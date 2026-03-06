class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo {self.first_name}, selamat datang kembali!")

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo {self.first_name}, selamat datang kembali!")

# Membuat beberapa instance
user1 = User("Budi", "Santoso", 25, "budi@example.com")
user2 = User("Siti", "Aisyah", 30, "siti@example.com")
user3 = User("Andi", "Wijaya", 22, "andi@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()