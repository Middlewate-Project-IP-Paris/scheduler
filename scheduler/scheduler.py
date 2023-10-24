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
    if action_name == 'updateChannels':
        empty_request = channel_pb2_grpc.google_dot_protobuf_dot_empty__pb2.Empty
        stub_ch.getChannels(request=empty_request)
#        for channel_id in stub_ch.getChannels(request=empty_request):
#            print(channel_id)
    if action_name == 'getPosts':
        timestamp = Timestamp()
        request = channel_pb2.GetPostsRequest(channel_ids=(3, 5), moment=timestamp.FromDatetime(datetime.datetime.fromtimestamp(232342143)))
        stub_ch.getPosts(request=request)
    if action_name == 'getPostStat':
        request = channel_pb2.PostStatRequest(channel_id=3, post_id=4)
        stub_ch.getPostStat(request=request)
    if action_name == 'getChannelInfo':
        request = channel_pb2.ChannelInfoRequest(channel_id=(3, 5))
        stub_ch.getChannelInfo(request=request)
    if action_name == 'getChannelSubsHistory':
        request = channel_pb2.ChannelSubsHistoryRequest(channel_id=(3, 5))
        stub_ch.getChannelSubsHistory(request=request)
    if action_name == 'getPostStatHistory':
        request = channel_pb2.PostStatHistoryRequest(channel_id=(3, 5), history_type=(1, 2))
        stub_ch.getPostStatHistory(request=request)
    if action_name == 'subCount':
        # request = {'channel_id': -1001604616173}
        request = assistant_on_demand_pb2.ChannelSubsRequest(channel_id=-1001604616173)
        stub_as.getChannelSubs(request)
#        for subs in stub_as.getChannelSubs(request=request):
#            print(subs)
    if action_name == 'channelMeta':
        request = assistant_on_demand_pb2.ChannelMetaRequest(channel_id=-1001604616173)
        stub_as.getChannelSubs(request)
#        for info in stub_as.getChannelMeta(request=request):
#            print(info)
    if action_name == 'postStat':
        request = assistant_on_demand_pb2.PostStatRequest(channel_id=-1001604616173, post_id=3)
        stub_as.getChannelSubs(request)
#        for info in stub_as.getPostStat(request=request):
#            print(info)
    if action_name == 'postContent':
        request = assistant_on_demand_pb2.PostRequest(channel_id=-1001604616173, post_id=3)
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

    def run(self, action, action_args=()):
        if self.is_running:
            self.event = self.scheduler.enter(self.repeat_minutes, 1, self.run, (action, action_args))
            action(*action_args)

    def start(self):
        self.is_running = True
        self.run(on_method_action(self.target_service_method))
        self.scheduler.run()

    def stop(self):
        self.is_running = False
        if self.scheduler and self.event:
            self.scheduler.cancel(self.event)

    def modify_scheduler(self):
        pass
