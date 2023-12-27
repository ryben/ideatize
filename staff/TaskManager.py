from manager.ResourcesManager import ResourcesManager
from model.Resource import Resource
from staff.TaskOutputSink import TaskOutputSink
from staff.StaffTask import StaffTask
from util.TaskLoader import TaskLoader


class TaskManager:
    tasks: list[StaffTask]
    resources_manager: ResourcesManager
    task_loader: TaskLoader
    output_consumer: TaskOutputSink

    def __init__(self, task_names: list[str], task_outputs: list[str]):
        self.tasks = []
        self.resources_manager = ResourcesManager()
        self.task_loader = TaskLoader()

        self.output_consumer = TaskOutputSink(self.resources_manager, task_outputs)
        self.resources_manager.subscribe(self.output_consumer)

        # Setup tasks so that they take inputs and send outputs to each other
        for task_name in task_names:
            base_task = self.task_loader.load_by_name(task_name)
            staff_task = StaffTask(base_task, self.resources_manager)
            self.tasks.append(staff_task)
            self.resources_manager.subscribe(staff_task)

    def execute_tasks(self, resources: list[Resource]):
        for resource in resources:
            self.resources_manager.add_resource(resource)
