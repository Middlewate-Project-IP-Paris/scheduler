import grpc
from proto import scheduler_pb2
from proto import scheduler_pb2_grpc
import threading
import time

class SchedulerService(scheduler_pb2_grpc.SchedulerServiceServicer):
    def __init__(self):
        self.schedulers = []
        self.task_threads = []

    def CreateScheduler(self, request, context):
        # Implement scheduling logic here and call the target service method
        scheduler = scheduler_pb2.SchedulerResponse(
            id=str(len(self.schedulers) + 1),
            name=request.name,
            cron_expression=request.cron_expression,
            target_service_method=request.target_service_method,
            repeat_minutes=request.repeat_minutes
        )
        self.schedulers.append(scheduler)

        # Start a thread to handle repeated scheduling
        task_thread = threading.Thread(target=self.execute_repeatedly, args=(scheduler,))
        self.task_threads.append(task_thread)
        task_thread.start()

        return scheduler

    def GetAllSchedulers(self, request, context):
        return scheduler_pb2.SchedulerList(schedulers=self.schedulers)

    def ModifyScheduler(self, request, context):
        # Implement logic to modify the scheduler
        for scheduler in self.schedulers:
            if scheduler.id == request.id:
                scheduler.name = request.name
                scheduler.cron_expression = request.cron_expression
                scheduler.target_service_method = request.target_service_method
                scheduler.repeat_minutes = request.repeat_minutes
                return scheduler
        context.set_code(grpc.StatusCode.NOT_FOUND)
        return scheduler_pb2.SchedulerResponse()

    def execute_repeatedly(self, scheduler):
        while True:
            # Sleep for the specified number of minutes
            time.sleep(60 * scheduler.repeat_minutes)
            
            # Implement logic to call the target service method here
            print(f"Executing task: {scheduler.target_service_method} for {scheduler.name}")

def serve():
    server = grpc.server(grpc.ThreadPoolExecutor(max_workers=10))
    scheduler_pb2_grpc.add_SchedulerServiceServicer_to_server(SchedulerService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
