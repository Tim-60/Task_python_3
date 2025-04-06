class Town:
    country: str = "Россия"
    current_year: int = 2025

    def __init__(self, name: str, date_of_foundation: int, population: int, famous_citizen: str, biggest_river: str) -> None:
        self.name = name
        self.date_of_foundation = date_of_foundation
        self.population = population
        self.famous_citizen = famous_citizen
        self.biggest_river = biggest_river

    def __str__(self) -> str:
        return f"{self.name} ({Town.country}) был основан в {self.date_of_foundation}, на {Town.current_year} его население составляет {self.population} человек. Одним из самых известных уроженцев города является {self.famous_citizen}. В этом городе протекает река {self.biggest_river}."

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return Town.current_year - self.date_of_foundation

    def category (self) -> str:
            if self.population > 3000000:
                return ('Это сверхкрупный город')
            elif self.population > 1000000 and self.population <= 3000000:
                return ('Это крупнейший город')
            elif self.population > 250000 and self.population <= 1000000:
                return ('Это крупный город')
            elif self.population > 100000 and self.population <= 250000:
                return ('Это большой город')
            elif self.population > 50000 and self.population <= 100000:
                return ('Это средний город')
            elif self.population >= 12000 and self.population <= 50000:
                return ('Это малый город')
            else: 
                 return('Это не город')

    def get_biggest_river(self) -> str:
        return self.biggest_river

    def change_country(country: str) -> None:
        Town.country = country


town_1 = Town("Псков", 903, 187129, 'В.М. Брадис', 'Великая')
town_2 = Town("Смоленск", 863, 310645, 'Борис Васильев', 'Днепр')
town_3 = Town("Санкт-Петербург", 1703, 5597763, 'Иосиф Бродский', 'Нева')

print(town_1)
print(town_2)
print(town_3)

print(town_1.get_name())
print(town_2.get_name())
print(town_3.get_name())

print(town_1.get_age())
print(town_2.get_age())
print(town_3.get_age())


print(town_1.category())
print(town_2.category())
print(town_3.category())


print(town_1.get_biggest_river())
print(town_2.get_biggest_river())
print(town_3.get_biggest_river())

Town.change_country('Беларусь')
print(Town.country)


