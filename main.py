from transport.transport_company import TransportCompany  # Импорт класса TransportCompany
from transport.truck import Truck  # Импорт класса Truck
from transport.train import Train  # Импорт класса Train
from transport.client import Client  # Импорт класса Client

def main():  # Основная функция программы
    transport_company = TransportCompany("Global Transport")  # Создание объекта транспортной компании

    while True:  # Основной цикл программы
        print("\nМеню:")  # Вывод меню на экран
        print("1. Добавить транспортное средство")  # Опция для добавления транспортного средства
        print("2. Добавить клиента")  # Опция для добавления клиента
        print("3. Оптимизировать распределение грузов")  # Опция для оптимизации распределения грузов
        print("4. Показать все транспортные средства")  # Опция для вывода всех транспортных средств
        print("5. Показать всех клиентов")  # Опция для вывода всех клиентов
        print("6. Удалить транспортное средство")  # Опция для удаления транспортного средства
        print("7. Удалить клиента")  # Опция для удаления клиента
        print("8. Выйти")  # Опция для выхода из программы

        choice = input("Выберите опцию: ")  # Получение выбора пользователя

        if choice == "1":  # Если пользователь выбрал добавление транспортного средства
            type_of_vehicle = input("Введите тип транспортного средства (Truck/Train): ").lower()  # Ввод типа транспортного средства
            
            if type_of_vehicle not in ["truck", "train"]:
                print("Неверный тип транспортного средства, допустимые значения: Truck или Train")
                continue  # Продолжение цикла при неверном типе транспортного средства

            try:
                capacity = float(input("Введите грузоподъемность (в тоннах): "))  # Ввод грузоподъемности
                if capacity <= 0:
                    raise ValueError("Грузоподъемность должна быть положительным числом")
            except ValueError as e:
                print(f"Ошибка: {e}")
                continue  # Продолжение цикла при ошибке

            if type_of_vehicle == "truck":  # Если выбрано транспортное средство типа Truck
                color = input("Введите цвет грузовика: ")  # Ввод цвета грузовика
                if not color:
                    print("Ошибка: Цвет грузовика не может быть пустым")
                    continue  # Продолжение цикла при ошибке
                vehicle = Truck(capacity, color)  # Создание объекта Truck
            elif type_of_vehicle == "train":  # Если выбрано транспортное средство типа Train
                try:
                    number_of_cars = int(input("Введите количество вагонов: "))  # Ввод количества вагонов
                    if number_of_cars <= 0:
                        raise ValueError("Количество вагонов должно быть положительным целым числом")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    continue  # Продолжение цикла при ошибке
                vehicle = Train(capacity, number_of_cars)  # Создание объекта Train

            transport_company.add_vehicle(vehicle)  # Добавление транспортного средства в компанию
            print(f"Транспортное средство добавлено с ID: {vehicle.vehicle_id}")  # Вывод сообщения о добавлении транспортного средства и его ID

        elif choice == "2":  # Если пользователь выбрал добавление клиента
            name = input("Введите имя клиента: ")  # Ввод имени клиента
            if not name or not name.isalpha() or len(name) < 2:
                print("Ошибка: Имя должно содержать только буквы и быть не менее 2 символов.")
                continue  # Продолжение цикла при ошибке

            try:
                cargo_weight = float(input("Введите вес груза (в тоннах): "))  # Ввод веса груза
                if cargo_weight <= 0 or cargo_weight > 10000:
                    raise ValueError("Вес груза должен быть положительным числом не более 10000 кг.")
            except ValueError as e:
                print(f"Ошибка: {e}")
                continue  # Продолжение цикла при ошибке
            is_vip = input("VIP клиент? (y/n): ").lower() == 'y'  # Ввод флага VIP-клиента
            client = Client(name, cargo_weight, is_vip)  # Создание объекта Client
            transport_company.add_client(client)  # Добавление клиента в компанию
            print("Клиент добавлен")  # Вывод сообщения о добавлении клиента

        elif choice == "3":  # Если пользователь выбрал оптимизацию распределения грузов
            transport_company.optimize_cargo_distribution()  # Оптимизация распределения грузов
            print("Грузы оптимизированы")  # Вывод сообщения об оптимизации грузов

        elif choice == "4":  # Если пользователь выбрал вывод всех транспортных средств
            for vehicle in transport_company.list_vehicles():  # Перебор всех транспортных средств
                print(vehicle)  # Вывод информации о транспортном средстве

        elif choice == "5":  # Если пользователь выбрал вывод всех клиентов
            for client in transport_company.list_clients():  # Перебор всех клиентов
                print(client)  # Вывод информации о клиенте

        elif choice == "6":  # Если пользователь выбрал удаление транспортного средства
            try:
                vehicle_id = int(input("Введите ID транспортного средства для удаления: "))  # Ввод ID транспортного средства
                if not any(v.vehicle_id == vehicle_id for v in transport_company.vehicles):
                    print(f"Транспортное средство с ID {vehicle_id} не найдено.")
                    continue  # Продолжение цикла при ошибке
                transport_company.remove_vehicle(vehicle_id)  # Удаление транспортного средства из компании
                print("Транспортное средство удалено")  # Вывод сообщения об удалении транспортного средства
            except ValueError:
                print("Ошибка: ID транспортного средства должно быть положительным целым числом")

        elif choice == "7":  # Если пользователь выбрал удаление клиента
            client_name = input("Введите имя клиента для удаления: ")  # Ввод имени клиента
            if not client_name:
                print("Ошибка: Имя клиента не может быть пустым")
                continue  # Продолжение цикла при ошибке
            if not any(c.name == client_name for c in transport_company.clients):
                print(f"Клиент с именем {client_name} не найден.")
                continue  # Продолжение цикла при ошибке
            transport_company.remove_client(client_name)  # Удаление клиента из компании
            print("Клиент удален")  # Вывод сообщения об удалении клиента

        elif choice == "8":  # Если пользователь выбрал выход из программы
            break  # Выход из цикла и завершение программы

        else:  # Если введена неверная опция
            print("Неверный выбор, попробуйте снова")  # Вывод сообщения об ошибке

if __name__ == "__main__":  # Если файл запущен как основная программа
    main()  # Вызов основной функции
