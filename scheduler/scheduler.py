import grpc
# import scheduler_pb2
from proto import scheduler_pb2, scheduler_pb2_grpc
from proto.channel import channel_pb2, channel_pb2_grpc
from proto.tg_assistant import assistant_on_demand_pb2, assistant_on_demand_pb2_grpc
# import google_dot_protobuf_dot_empty__pb2
import datetime
# import proto.channel.
import threading
import time
import vars
import sched
from google.protobuf.timestamp_pb2 import Timestamp



def on_method_action(action_name):
    channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
    assistant = grpc.insecure_channel(f'''localhost:{vars.ASSISTANT_SERVICE_PORT}''')
    stub_ch = channel_pb2_grpc.channelServiceStub(channel)
    stub_as = assistant_on_demand_pb2_grpc.assistanceOnDemandStub(assistant)
    if action_name == 'getPosts':
        timestamp = Timestamp()
        timestamp.FromDatetime(datetime.datetime.fromtimestamp(1697800000))
        #t = Timestamp()
        #t1 = timestamp.FromDatetime(datetime.datetime.fromtimestamp(1549836078))
        #t.CopyFrom(timestamp.FromDatetime(datetime.datetime.fromtimestamp(1549836078)))
        #print("type %s", type(timestamp.FromDatetime(datetime.datetime.fromtimestamp(1549836078))))
        request = channel_pb2.GetPostsRequest(channel_ids=[1])
        request.moment.CopyFrom(timestamp)
        response = stub_ch.getPosts(request=request)
        print(response)
        for dict_ch_post in response.channels_posts:
            channel_id = dict_ch_post.channel_id
            try:
                for post_id in dict_ch_post.post_id:
                    request = assistant_on_demand_pb2.PostRequest(channel_id=channel_id, post_id=post_id)
                    stub_as.getPost(request)
            except AttributeError:
                print("No new posts")
    if action_name == 'getPostStat':
        timestamp = Timestamp()
        timestamp.FromDatetime(datetime.datetime.fromtimestamp(1697800000))
        request = channel_pb2.GetPostsRequest(channel_ids=[1])
        request.moment.CopyFrom(timestamp)
        response = stub_ch.getPosts(request=request)
        for dict_ch_post in response.channels_posts:
            channel_id = dict_ch_post.channel_id
            print(channel_id)
            #try:
            for post_id in dict_ch_post.post_id:
                request = assistant_on_demand_pb2.PostStatRequest(channel_id=channel_id, post_id=post_id)
                stub_as.getPost(request)
            #except AttributeError:
                #print("No new posts")
    if action_name == 'getChannelInfo':
        empty_request = channel_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        response = stub_ch.getChannels(request=empty_request)
        print(response)
        for channel in response:
            print(channel)
            print(channel.channel_ids)
            channel_id = list(channel.channel_ids)
            print(channel_id[0])
            request = assistant_on_demand_pb2.ChannelMetaRequest(channel_id=channel_id[0])
            stub_as.getChannelMeta(request)
    if action_name == 'getChannelSubs':
        empty_request = channel_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty()
        response = stub_ch.getChannels(request=empty_request)
        for channel in response:
            channel_id = list(channel.channel_ids)
            request = assistant_on_demand_pb2.ChannelSubsRequest(channel_id=channel_id[0])
            stub_as.getChannelSubs(request)


class Scheduler:
    def __init__(self, scheduler_id, name, target_service_method, repeat_minutes):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.name = name
        self.target_service_method = target_service_method
        self.repeat_minutes = repeat_minutes
        self.scheduler_id = scheduler_id
        self.is_running = False

#    def create_scheduler(self):
#        if self.target_service_method == 'SubNum':
#            self.start_scheduler()
#        if self.target_service_method == 'ChannelMeta':
#            self.start_scheduler()
#        if self.target_service_method == 'PostContent':
#            self.start_scheduler()
#        if self.target_service_method == 'PostStats':
#            self.start_scheduler()

#    def start_scheduler(self):
#        channel = grpc.insecure_channel(f'''localhost:{vars.CHANNEL_SERICE_PORT}''')
#        stub = channel_pb2_grpc.channelServiceStub(channel)
#        if self.target_service_method == 'updateChannels':
#            empty_request = channel_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty
#            for channel_id in stub.getChannels(request = empty_request):
#                print(channel_id)

        # elif self.target_service_method == 'updateChannelsInfo':
        #     # channel_
#        pass
    def repeat_task(self):
        self.scheduler.enter(self.repeat_minutes, 1, on_method_action, self.target_service_method)
        self.scheduler.enter(self.repeat_minutes, 1, self.repeat_task, ())

    def run(self):
        if self.is_running:
            self.repeat_task()
            self.scheduler.run()
#            print(self.scheduler.queue)
#            self.event = self.scheduler.enter(self.repeat_minutes, 1, self.run, (action, action_args))

#            action(*action_args)

    def start(self):
        self.is_running = True
        self.run()
#        self.scheduler.run()

    def stop(self):
        self.is_running = False
#        if self.scheduler and self.event:
#            self.scheduler.cancel(self.event)

    def modify_scheduler(self):
        pass
