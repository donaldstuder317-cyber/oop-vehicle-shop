class Car:
    # Class attributes - using a dictionary for fast O(1) lookups
    all_cars = {}
    total_cars = 0

    def __init__(self, make, model, year, mileage=0):
        # Increment total cars and assign unique ID
        Car.total_cars += 1
        self._id = Car.total_cars
        
        # Instance attributes
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = []
        
        # Store instance in the dictionary using the ID as the key
        Car.all_cars[self._id] = self

    def get_details(self):
        """Returns a formatted string of the car's details and service history."""
        services_str = ", ".join(self._services) if self._services else "None"
        return (f"ID: {self._id} | {self._year} {self._make} {self._model} "
                f"| Mileage: {self._mileage} miles | Services: {services_str}")

    @classmethod
    def find_by_id(cls, car_id):
        """Class method to find and return a car instance by its unique ID (O(1) time)."""
        return cls.all_cars.get(car_id)


def main():
    while True:
        print("\n----  WELCOME  ----")
        print("1. Add a car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            make = input("Enter make: ").strip()
            model = input("Enter model: ").strip()
            try:
                year = int(input("Enter year: ").strip().replace(",", ""))
                mileage = int(input("Enter initial mileage: ").strip().replace(",", ""))
                car = Car(make, model, year, mileage)
                print(f"Success! Added car [ID: {car._id}]: {year} {make} {model}")
            except ValueError:
                print("❌ Invalid input. Year and mileage must be valid numbers.")
                
        elif choice == "2":
            if not Car.all_cars:
                print("No cars currently in the system.")
            else:
                print("\n--- All Cars ---")
                for car in Car.all_cars.values():
                    print(f"ID: {car._id} - {car._year} {car._make} {car._model}")
                    
        elif choice == "3":
            print(f"\nTotal number of cars: {Car.total_cars}")
            
        elif choice == "4":
            try:
                car_id = int(input("Enter car ID: ").strip())
                car = Car.find_by_id(car_id)
                if car:
                    print(f"\n--- Car Details ---\n{car.get_details()}")
                else:
                    print("❌ Car not found.")
            except ValueError:
                print("❌ Invalid ID. Please enter a number.")
                
        elif choice == "5":
            try:
                car_id = int(input("Enter car ID to service: ").strip())
                car = Car.find_by_id(car_id)
                if car:
                    service = input("Enter service description (e.g., Oil Change): ").strip()
                    car._services.append(service)
                    print("✅ Service added successfully.")
                else:
                    print("❌ Car not found.")
            except ValueError:
                print("❌ Invalid ID.")
                
        elif choice == "6":
            try:
                car_id = int(input("Enter car ID to update mileage: ").strip())
                car = Car.find_by_id(car_id)
                if car:
                    new_mileage = int(input("Enter new mileage: ").strip().replace(",", ""))
                    if new_mileage >= car._mileage:
                        car._mileage = new_mileage
                        print("✅ Mileage updated successfully.")
                    else:
                        print("❌ Error: New mileage cannot be less than current mileage.")
                else:
                    print("❌ Car not found.")
            except ValueError:
                print("❌ Invalid input. Mileage must be a number.")
                
        elif choice == "7":
            print("Exiting application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()