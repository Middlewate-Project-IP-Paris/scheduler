# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: channel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rchannel.proto\x12\x07\x63hannel\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"6\n\x0fPostStatRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\"V\n\x10PostStatResponse\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\r\n\x05views\x18\x03 \x01(\x04\x12\x0e\n\x06shares\x18\x04 \x01(\x04\"(\n\x12\x43hannelInfoRequest\x12\x12\n\nchannel_id\x18\x01 \x03(\x03\"A\n\x13\x43hannelInfoResponse\x12*\n\x0c\x63hannel_info\x18\x01 \x03(\x0b\x32\x14.channel.ChannelInfo\"g\n\x0b\x43hannelInfo\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bsubscribers\x18\x05 \x01(\x04\"*\n\x13GetChannelsResponse\x12\x13\n\x0b\x63hannel_ids\x18\x01 \x03(\x03\"/\n\x19\x43hannelSubsHistoryRequest\x12\x12\n\nchannel_id\x18\x01 \x03(\x03\"W\n\x1a\x43hannelSubsHistoryResponse\x12\x39\n\x14\x63hannel_subs_history\x18\x01 \x03(\x0b\x32\x1b.channel.ChannelSubsHistory\"b\n\x12\x43hannelSubsHistory\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12*\n\x06moment\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04subs\x18\x03 \x01(\x03\"X\n\x16PostStatHistoryRequest\x12\x12\n\nchannel_id\x18\x01 \x03(\x03\x12*\n\x0chistory_type\x18\x02 \x03(\x0e\x32\x14.channel.HistoryType\"N\n\x17PostStatHistoryResponse\x12\x33\n\x11post_stat_history\x18\x01 \x03(\x0b\x32\x18.channel.PostStatHistory\"U\n\x0fPostStatHistory\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12.\n\x0cpost_history\x18\x02 \x03(\x0b\x32\x18.channel.PostHistoryType\"x\n\x0fPostHistoryType\x12*\n\x0chistory_type\x18\x01 \x01(\x0e\x32\x14.channel.HistoryType\x12*\n\x06moment\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\"R\n\x0fGetPostsRequest\x12\x13\n\x0b\x63hannel_ids\x18\x01 \x03(\x03\x12*\n\x06moment\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"A\n\x10GetPostsResponse\x12-\n\x0e\x63hannels_posts\x18\x01 \x03(\x0b\x32\x15.channel.ChannelPosts\"3\n\x0c\x43hannelPosts\x12\x12\n\nchannel_id\x18\x01 \x01(\x03\x12\x0f\n\x07post_id\x18\x02 \x03(\x03*M\n\x0bHistoryType\x12\x17\n\x13HISTORY_UNSPECIFIED\x10\x00\x12\x11\n\rHISTORY_VIEWS\x10\x01\x12\x12\n\x0eHISTORY_SHARES\x10\x02\x32\xe4\x03\n\x0e\x63hannelService\x12\x42\n\x0bgetPostStat\x12\x18.channel.PostStatRequest\x1a\x19.channel.PostStatResponse\x12K\n\x0egetChannelInfo\x12\x1b.channel.ChannelInfoRequest\x1a\x1c.channel.ChannelInfoResponse\x12\x45\n\x0bgetChannels\x12\x16.google.protobuf.Empty\x1a\x1c.channel.GetChannelsResponse0\x01\x12`\n\x15getChannelSubsHistory\x12\".channel.ChannelSubsHistoryRequest\x1a#.channel.ChannelSubsHistoryResponse\x12W\n\x12getPostStatHistory\x12\x1f.channel.PostStatHistoryRequest\x1a .channel.PostStatHistoryResponse\x12?\n\x08getPosts\x12\x18.channel.GetPostsRequest\x1a\x19.channel.GetPostsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'channel_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HISTORYTYPE']._serialized_start=1311
  _globals['_HISTORYTYPE']._serialized_end=1388
  _globals['_POSTSTATREQUEST']._serialized_start=88
  _globals['_POSTSTATREQUEST']._serialized_end=142
  _globals['_POSTSTATRESPONSE']._serialized_start=144
  _globals['_POSTSTATRESPONSE']._serialized_end=230
  _globals['_CHANNELINFOREQUEST']._serialized_start=232
  _globals['_CHANNELINFOREQUEST']._serialized_end=272
  _globals['_CHANNELINFORESPONSE']._serialized_start=274
  _globals['_CHANNELINFORESPONSE']._serialized_end=339
  _globals['_CHANNELINFO']._serialized_start=341
  _globals['_CHANNELINFO']._serialized_end=444
  _globals['_GETCHANNELSRESPONSE']._serialized_start=446
  _globals['_GETCHANNELSRESPONSE']._serialized_end=488
  _globals['_CHANNELSUBSHISTORYREQUEST']._serialized_start=490
  _globals['_CHANNELSUBSHISTORYREQUEST']._serialized_end=537
  _globals['_CHANNELSUBSHISTORYRESPONSE']._serialized_start=539
  _globals['_CHANNELSUBSHISTORYRESPONSE']._serialized_end=626
  _globals['_CHANNELSUBSHISTORY']._serialized_start=628
  _globals['_CHANNELSUBSHISTORY']._serialized_end=726
  _globals['_POSTSTATHISTORYREQUEST']._serialized_start=728
  _globals['_POSTSTATHISTORYREQUEST']._serialized_end=816
  _globals['_POSTSTATHISTORYRESPONSE']._serialized_start=818
  _globals['_POSTSTATHISTORYRESPONSE']._serialized_end=896
  _globals['_POSTSTATHISTORY']._serialized_start=898
  _globals['_POSTSTATHISTORY']._serialized_end=983
  _globals['_POSTHISTORYTYPE']._serialized_start=985
  _globals['_POSTHISTORYTYPE']._serialized_end=1105
  _globals['_GETPOSTSREQUEST']._serialized_start=1107
  _globals['_GETPOSTSREQUEST']._serialized_end=1189
  _globals['_GETPOSTSRESPONSE']._serialized_start=1191
  _globals['_GETPOSTSRESPONSE']._serialized_end=1256
  _globals['_CHANNELPOSTS']._serialized_start=1258
  _globals['_CHANNELPOSTS']._serialized_end=1309
  _globals['_CHANNELSERVICE']._serialized_start=1391
  _globals['_CHANNELSERVICE']._serialized_end=1875
# @@protoc_insertion_point(module_scope)
