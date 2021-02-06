class Warehouse:
    equipment = []  # For keeping the objects of equipment
    name = ""

    def __init__(self, name):
        self.equipment = []
        self.name = name

    def get_equipment_list(self):
        for i in self.equipment:
            print(f"Equipment type: {i.equipment_type} | Model: {i.model} | Serial number: {i.serial_number} | "
                  f"Department: {'free to take' if not i.department else i.department}")

    def give_out(self, model_name, department_name):
        for i in self.equipment:
            if i.model == model_name and i.department == "":
                i.department = department_name
                break
        else:
            print(f"No equipment {model_name} is available")

    def return_from_department(self, model_name, department_name):
        for i in self.equipment:
            if i.model == model_name and i.department == department_name:
                i.department = ""
                break
        else:
            print(f"No equipment {model_name} is available for return")

    def take_to_warehouse(self, obj):
        for i in self.equipment:  # Validation of NO equal serial number
            if i.serial_number == obj.serial_number and i.equipment_type == obj.equipment_type:
                print(f"No equal serial number possible to use for same type of equipment: {i.serial_number}"
                      f"for {i.equipment_type}")
                break
        self.equipment.append(obj)

    def free_to_use(self, model_name):
        for i in self.equipment:
            if i.model == model_name:
                return True


class OfficeEquipment:
    model = ""
    serial_number = ""
    department = ""
    equipment_type = ""


class Printer(OfficeEquipment):
    toner_model = ""
    format_size = ()

    def __init__(self, equipment_type, model, serial_number, format_size=(), toner_model=""):
        self.model = model
        self.serial_number = serial_number
        self.format_size = format_size
        self.toner_model = toner_model
        self.equipment_type = equipment_type


class Scanner(OfficeEquipment):
    scanner_size = ()

    def __init__(self, equipment_type, model, serial_number, scanner_size=()):
        self.model = model
        self.serial_number = serial_number
        self.scanner_size = scanner_size
        self.equipment_type = equipment_type


class Copier(OfficeEquipment):
    format_size = ()

    def __init__(self, equipment_type, model, serial_number, format_size=()):
        self.model = model
        self.serial_number = serial_number
        self.format_size = format_size
        self.equipment_type = equipment_type


my_warehouse = Warehouse("Office warehouse")
print(f"\n{15 * '_'} Loading equipment {15 * '_'}\n")
my_warehouse.take_to_warehouse(Printer("Printer", "HP1550", "aWFGHw034", ('A3', 'A4'), "CN1550D"))  # Initialisation
my_warehouse.take_to_warehouse(Printer("Printer", "HP1451", "aQWErw545", ('A3', 'A4'), "CN1550D"))  # Initialisation
my_warehouse.take_to_warehouse(Scanner("Scanner", "HP1856", "aWASyw986", ('A4', 'A5')))  # Initialisation
my_warehouse.take_to_warehouse(Scanner("Scanner", "HP1220", "aWEtrWsw437", ('A4', 'A5')))  # Initialisation
my_warehouse.take_to_warehouse(Copier("Copier", "HP1243", "aWEW456sw437", ('A4', 'A5')))  # Initialisation
my_warehouse.take_to_warehouse(Copier("Copier", "HP1227", "aWEW34sw437", ('A4', 'A5')))  # Initialisation
my_warehouse.take_to_warehouse(Copier("Copier", "HP1227", "aWEW34sw437", ('A4', 'A5')))  # ERROR with same serial number
my_warehouse.get_equipment_list()
print(f"\n{15 * '_'} Take from warehouse equipment to IT department {15 * '_'}\n")
my_warehouse.give_out("HP1550", "IT")  # Arrange to IT department
my_warehouse.give_out("HP1451", "IT")  # Arrange to IT department
my_warehouse.give_out("HP1220", "IT")  # Arrange to IT department
my_warehouse.give_out("HP1550", "IT")  # Error no such type equipment available

my_warehouse.get_equipment_list()
print(f"\n{15 * '_'} Return to warehouse all equipment from IT department {15 * '_'}\n")
my_warehouse.return_from_department("HP1550", "IT")  # Take back from IT
my_warehouse.return_from_department("HP1451", "IT")  # Take back from IT
my_warehouse.return_from_department("HP1220", "IT")  # Take back from IT

my_warehouse.get_equipment_list()
