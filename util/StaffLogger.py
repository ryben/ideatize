from time import strftime

from model.Resource import Resource
from util import FileManager


class StaffLogger:
    def __init__(self, staff_name: str):
        self.staff_name = staff_name

    def log_output_resources(self, resources: list[Resource]):
        time = strftime("%Y-%m-%d %H.%M.%S")
        for resource in resources:
            FileManager.write_file(f"{time} - {self.staff_name} - {resource.type}", resource.content)

