class RealProperty:
    def __init__(self, id: int, area: int, price_per_sqm: int, description: str):
        self.id = id
        self.area = area
        self.price_per_sqm = price_per_sqm
        self.description = description

    def total_price(self):
        return self.area * self.price_per_sqm
        

def cheaper_properties(properties: list, reference: "RealProperty"):
    return [(item, item.total_price()-reference.total_price()) for item in properties if item.total_price()<reference.total_price()]



if __name__ == "__main__":

    a1 = RealProperty(1, 16, 5500, "Central studio")
    a2 = RealProperty(2, 38, 4200, "Two bedrooms downtown")
    a3 = RealProperty(3, 78, 2500, "Three bedrooms in the suburbs")
    a4 = RealProperty(6, 215, 500, "Farm in the middle of nowhere")
    a5 = RealProperty(4, 105, 1700, "Loft in a small town")
    a6 = RealProperty(25, 1200, 2500, "Countryside mansion")

    properties = [a1, a2, a3, a4, a5, a6]

    print(f"cheaper options when compared to {a3.description}:")
    for item in cheaper_properties(properties, a3):
        print(f"{item[0].description:35} price difference {item[1]} euros")