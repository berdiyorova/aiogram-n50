import os
import csv


class CSVManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def _file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read_data(self):
        if self._file_exists_and_not_empty():
            with open(self.file_name, 'r', newline='') as file:
                return list(csv.reader(file))  # Convert to list right away
        return []

    def write_data(self, data: list):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def add_data(self, data: list):
        all_data = self.read_data()
        if data not in all_data:
            all_data.append(data)
        self.write_data(all_data)
        return "Data added successfully"

    def delete_file(self):
        os.remove(self.file_name)
        print("File deleted!")
        return True




user_manager = CSVManager("users.csv")
