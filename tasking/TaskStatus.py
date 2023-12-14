from enum import Enum


class TaskStatus(Enum):
    MISSING_RESOURCE = 1
    READY = 2
    IN_PROGRESS = 3
    DONE = 4
