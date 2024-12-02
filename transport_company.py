import json  # Импорт модуля для работы с JSON
from vehicle import Vehicle  # Импорт класса Vehicle
from client import Client  # Импорт класса Client
from truck import Truck  # Импорт класса Truck
from train import Train  # Импорт класса Train

class TransportCompany:
    def __init__(self, name, filename='data.json'):
        self.name = name  # Название компании
        self.vehicles = []  # Список транспортных средств
        self.clients = []  # Список клиентов
        self.filename = filename  # Имя файла для сохранения данных
        self.load_from_file()  # Загрузка данных из файла

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)  # Добавление транспортного средства в список
            self.save_to_file()  # Сохранение данных в файл
        else:
            raise ValueError("Invalid vehicle")  # Ошибка при неверном типе транспортного средства

    def list_vehicles(self):
        return self.vehicles  # Возвращает список транспортных средств

    def remove_vehicle(self, vehicle_id):
        self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]  # Удаление транспортного средства по ID
        self.save_to_file()  # Сохранение данных в файл после удаления

    def add_client(self, client):
        if isinstance(client, Client):
            self.clients.append(client)  # Добавление клиента в список
            self.save_to_file()  # Сохранение данных в файл
        else:
            raise ValueError("Invalid client")  # Ошибка при неверном типе клиента

    def list_clients(self):
        return self.clients  # Возвращает список клиентов

    def remove_client(self, name):
        self.clients = [c for c in self.clients if c.name != name]  # Удаление клиента по имени
        self.save_to_file()  # Сохранение данных в файл после удаления

    def optimize_cargo_distribution(self):
        vip_clients = [client for client in self.clients if client.is_vip]  # Список VIP клиентов
        regular_clients = [client for client in self.clients if not client.is_vip]  # Список обычных клиентов
        all_clients = vip_clients + regular_clients  # Все клиенты с приоритетом VIP клиентов

        for client in all_clients:
            for vehicle in self.vehicles:
                if vehicle.capacity - vehicle.current_load >= client.cargo_weight:
                    vehicle.load_cargo(client)  # Загрузка груза клиента в транспортное средство
                    break

    def save_to_file(self):
        data = {
            "vehicles": [vehicle.__dict__ for vehicle in self.vehicles],  # Преобразование объектов транспортных средств в словари
            "clients": [client.__dict__ for client in self.clients]  # Преобразование объектов клиентов в словари
        }
        with open(self.filename, 'w') as f:
            json.dump(data, f)  # Сохранение данных в файл в формате JSON

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)  # Загрузка данных из файла JSON
                self.vehicles = []  # Очистка списка транспортных средств
                for v in data['vehicles']:
                    if 'color' in v:
                        self.vehicles.append(Truck(**v))  # Создание объектов Truck из данных
                    elif 'number_of_cars' in v:
                        self.vehicles.append(Train(**v))  # Создание объектов Train из данных
                    else:
                        self.vehicles.append(Vehicle(**v))  # Создание объектов Vehicle из данных
                self.clients = [Client(**c) for c in data['clients']]  # Создание объектов Client из данных
        except FileNotFoundError:
            pass  # Игнорировать ошибку, если файл не найден
