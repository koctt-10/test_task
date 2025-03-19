# Классы фигур
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"Segment(({self.x1}, {self.y1}), ({self.x2}, {self.y2}))"


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Circle(center=({self.x}, {self.y}), radius={self.r})"


class Square:
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"Square(bottom-left=({self.x}, {self.y}), side={self.side})"


# Менеджер фигур
class ShapeManager:
    def __init__(self):
        self.shapes = {}

    def create_shape(self, shape_type, shape_id, *args):
        if shape_id in self.shapes:
            print(f"Error: Shape with id '{shape_id}' already exists.")
            return

        if shape_type == "point":
            self.shapes[shape_id] = Point(*args)
        elif shape_type == "segment":
            self.shapes[shape_id] = Segment(*args)
        elif shape_type == "circle":
            self.shapes[shape_id] = Circle(*args)
        elif shape_type == "square":
            self.shapes[shape_id] = Square(*args)
        else:
            print("Error: Unknown shape type.")
            return

        print(f"Shape '{shape_id}' created.")

    def delete_shape(self, shape_id):
        if shape_id in self.shapes:
            del self.shapes[shape_id]
            print(f"Shape '{shape_id}' deleted.")
        else:
            print(f"Error: Shape with id '{shape_id}' not found.")

    def list_shapes(self):
        if not self.shapes:
            print("No shapes created yet.")
            return

        for shape_id, shape in self.shapes.items():
            print(f"{shape_id}: {shape}")


# Основной цикл программы
def main():
    manager = ShapeManager()

    # Вывод справки при запуске программы
    print_help()

    while True:
        command = input("> ").strip().split()
        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "create":
            if len(command) < 3:
                print("Error: Invalid 'create' command format.")
                continue

            shape_type = command[1].lower()
            shape_id = command[2]

            if shape_type == "point" and len(command) == 5:
                manager.create_shape(shape_type, shape_id, int(command[3]), int(command[4]))
            elif shape_type == "segment" and len(command) == 7:
                manager.create_shape(shape_type, shape_id, int(command[3]), int(command[4]),
                                     int(command[5]), int(command[6]))
            elif shape_type == "circle" and len(command) == 6:
                manager.create_shape(shape_type, shape_id, int(command[3]), int(command[4]), int(command[5]))
            elif shape_type == "square" and len(command) == 6:
                manager.create_shape(shape_type, shape_id, int(command[3]), int(command[4]), int(command[5]))
            else:
                print("Error: Invalid parameters for 'create' command.")

        elif cmd == "delete":
            if len(command) == 2:
                manager.delete_shape(command[1])
            else:
                print("Error: Invalid 'delete' command format.")

        elif cmd == "list":
            manager.list_shapes()

        elif cmd == "help":
            print_help()

        elif cmd == "exit":
            print("Exiting the program.")
            break

        else:
            print("Error: Unknown command.")


# Функция для вывода справки
def print_help():
    help_text = """
Available commands:
  create point <id> <x> <y>          - Create a point with coordinates (x, y).
  create segment <id> <x1> <y1> <x2> <y2> - Create a segment between two points.
  create circle <id> <x> <y> <r>     - Create a circle with center (x, y) and radius r.
  create square <id> <x> <y> <side>  - Create a square with bottom-left corner (x, y) and side length.
  delete <id>                        - Delete a shape by its ID.
  list                               - List all created shapes.
  help                               - Show this help message.
  exit                               - Exit the program.
"""
    print(help_text)
    
if __name__ == "__main__":
    main()