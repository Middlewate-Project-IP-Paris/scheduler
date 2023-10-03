import grpc
# import scheduler_pb2
# import scheduler_pb2_grpc
import threading
import time

class Scheduler:
    def __init__(self, name, target_service_method, repeat_minutes):
        self.name = name
        self.target_service_method = target_service_method
        self.repeat_minutes = repeat_minutes
        self.scheduler_id = None
        self.is_running = False

    def create_scheduler(self):
        pass

    def start_scheduler(self):
        pass

    def stop_scheduler(self):
        pass
