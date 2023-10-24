import grpc
import threading
from concurrent import futures
# from grpc_reflection.v1alpha import reflection
# from consumer.consumer import kafka_consumer_thread
from proto import scheduler_pb2
from proto import scheduler_pb2_grpc
from scheduler import scheduler
import threading
import time

class SchedulerService(scheduler_pb2_grpc.SchedulerServiceServicer):
    def __init__(self):
        self.schedulers = []
        self.task_threads = []

    def CreateScheduler(self, request, context):
        # Implement scheduling logic here and call the target service method
        scheduler_response = scheduler_pb2.SchedulerResponse(
            id=str(len(self.schedulers) + 1),
            name=request.name,
            target_service_method=request.target_service_method,
            repeat_minutes=request.repeat_minutes
        )
        self.schedulers.append(scheduler_response)

        scheduler_instance = scheduler.Scheduler(scheduler_id=scheduler_response.id,
                                                 name=scheduler_response.name, 
                                                 target_service_method= scheduler_response.target_service_method,
                                                 repeat_minutes= scheduler_response.repeat_minutes)
        scheduler_instance.create_scheduler()
        print(scheduler_response)

        return scheduler_response

    def GetAllSchedulers(self, request, context):
        return scheduler_pb2.SchedulerList(schedulers=self.schedulers)

    def ModifyScheduler(self, request, context):
        # Implement logic to modify the scheduler
        for scheduler in self.schedulers:
            if scheduler.id == request.id:
                scheduler.name = request.name
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scheduler_pb2_grpc.add_SchedulerServiceServicer_to_server(SchedulerService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Server started on port 50053")
    server.wait_for_termination()

if __name__ == '__main__':
    # test
    serve()
