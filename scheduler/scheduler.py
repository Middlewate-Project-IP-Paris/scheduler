import grpc
# import scheduler_pb2
# import scheduler_pb2_grpc
from proto.channel import channel_pb2, channel_pb2_grpc
# import google_dot_protobuf_dot_empty__pb2 

# import proto.channel.
import threading
import time
import vars

class Scheduler:
    def __init__(self, scheduler_id, name, target_service_method, repeat_minutes):
        self.name = name
        self.target_service_method = target_service_method
        self.repeat_minutes = repeat_minutes
        self.scheduler_id = scheduler_id
        self.is_running = False

    def create_scheduler(self):
        self.start_scheduler()
        pass

    def start_scheduler(self):
        channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
        stub = channel_pb2_grpc.channelServiceStub(channel)
        if self.target_service_method == 'updateChannels':
            empty_request = channel_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
            for channel_id in stub.getChannels(request = empty_request):
                print(channel_id)

        # elif self.target_service_method == 'updateChannelsInfo':
        #     # channel_
        pass

    def stop_scheduler(self):
        pass
