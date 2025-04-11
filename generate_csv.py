import csv
import random

PARTS_NAMES = [
    "Filtro de Aire", "Pastillas de Freno", "Batería 12V", 
    "Amortiguadores", "Correa de Distribución", "Sensor de Oxígeno",
    "Bomba de Combustible", "Alternador", "Radiador"
]

COMPATIBLE_BRANDS = [
    "Toyota Hilux 2020", "Chevrolet Spark 2015", 
    "Ford Fiesta 2018", "Honda Civic 2022"
]

def generateCSV(numRecords=500, filename='spare_parts.csv'):
    """Generate CSV file with spare parts data"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'compatibility', 'price', 'stock', 'expiration_days'])
        
        for i in range(numRecords):
            writer.writerow([
                i + 1,
                random.choice(PARTS_NAMES),
                random.choice(COMPATIBLE_BRANDS),
                round(random.uniform(10, 200), 2),
                random.randint(0, 15),
                random.choice([30, 60, 90, None])
            ])

if __name__ == "__main__":
    generateCSV(500)
