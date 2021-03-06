# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/steps/scheduler_traffic_split.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.test_platform import request_pb2 as test__platform_dot_request__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test_platform/steps/scheduler_traffic_split.proto',
  package='test_platform.steps',
  syntax='proto3',
  serialized_options=_b('Z=go.chromium.org/chromiumos/infra/proto/go/test_platform/steps'),
  serialized_pb=_b('\n1test_platform/steps/scheduler_traffic_split.proto\x12\x13test_platform.steps\x1a\x1btest_platform/request.proto\"\xaf\x02\n\x1dSchedulerTrafficSplitRequests\x12\x43\n\x08requests\x18\x01 \x03(\x0b\x32\x31.test_platform.steps.SchedulerTrafficSplitRequest\x12_\n\x0ftagged_requests\x18\x02 \x03(\x0b\x32\x46.test_platform.steps.SchedulerTrafficSplitRequests.TaggedRequestsEntry\x1ah\n\x13TaggedRequestsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.test_platform.steps.SchedulerTrafficSplitRequest:\x02\x38\x01\"\xb7\x02\n\x1eSchedulerTrafficSplitResponses\x12\x45\n\tresponses\x18\x01 \x03(\x0b\x32\x32.test_platform.steps.SchedulerTrafficSplitResponse\x12\x62\n\x10tagged_responses\x18\x02 \x03(\x0b\x32H.test_platform.steps.SchedulerTrafficSplitResponses.TaggedResponsesEntry\x1aj\n\x14TaggedResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32\x32.test_platform.steps.SchedulerTrafficSplitResponse:\x02\x38\x01\"M\n\x1cSchedulerTrafficSplitRequest\x12\'\n\x07request\x18\x01 \x01(\x0b\x32\x16.test_platform.RequestJ\x04\x08\x02\x10\x03\"U\n\x1dSchedulerTrafficSplitResponse\x12.\n\x0eskylab_request\x18\x02 \x01(\x0b\x32\x16.test_platform.RequestJ\x04\x08\x01\x10\x02\x42?Z=go.chromium.org/chromiumos/infra/proto/go/test_platform/stepsb\x06proto3')
  ,
  dependencies=[test__platform_dot_request__pb2.DESCRIPTOR,])




_SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY = _descriptor.Descriptor(
  name='TaggedRequestsEntry',
  full_name='test_platform.steps.SchedulerTrafficSplitRequests.TaggedRequestsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.SchedulerTrafficSplitRequests.TaggedRequestsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.SchedulerTrafficSplitRequests.TaggedRequestsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=407,
)

_SCHEDULERTRAFFICSPLITREQUESTS = _descriptor.Descriptor(
  name='SchedulerTrafficSplitRequests',
  full_name='test_platform.steps.SchedulerTrafficSplitRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='test_platform.steps.SchedulerTrafficSplitRequests.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_requests', full_name='test_platform.steps.SchedulerTrafficSplitRequests.tagged_requests', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=407,
)


_SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY = _descriptor.Descriptor(
  name='TaggedResponsesEntry',
  full_name='test_platform.steps.SchedulerTrafficSplitResponses.TaggedResponsesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test_platform.steps.SchedulerTrafficSplitResponses.TaggedResponsesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='test_platform.steps.SchedulerTrafficSplitResponses.TaggedResponsesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=615,
  serialized_end=721,
)

_SCHEDULERTRAFFICSPLITRESPONSES = _descriptor.Descriptor(
  name='SchedulerTrafficSplitResponses',
  full_name='test_platform.steps.SchedulerTrafficSplitResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='test_platform.steps.SchedulerTrafficSplitResponses.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_responses', full_name='test_platform.steps.SchedulerTrafficSplitResponses.tagged_responses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=721,
)


_SCHEDULERTRAFFICSPLITREQUEST = _descriptor.Descriptor(
  name='SchedulerTrafficSplitRequest',
  full_name='test_platform.steps.SchedulerTrafficSplitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='test_platform.steps.SchedulerTrafficSplitRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=800,
)


_SCHEDULERTRAFFICSPLITRESPONSE = _descriptor.Descriptor(
  name='SchedulerTrafficSplitResponse',
  full_name='test_platform.steps.SchedulerTrafficSplitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skylab_request', full_name='test_platform.steps.SchedulerTrafficSplitResponse.skylab_request', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=887,
)

_SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY.fields_by_name['value'].message_type = _SCHEDULERTRAFFICSPLITREQUEST
_SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY.containing_type = _SCHEDULERTRAFFICSPLITREQUESTS
_SCHEDULERTRAFFICSPLITREQUESTS.fields_by_name['requests'].message_type = _SCHEDULERTRAFFICSPLITREQUEST
_SCHEDULERTRAFFICSPLITREQUESTS.fields_by_name['tagged_requests'].message_type = _SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY
_SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY.fields_by_name['value'].message_type = _SCHEDULERTRAFFICSPLITRESPONSE
_SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY.containing_type = _SCHEDULERTRAFFICSPLITRESPONSES
_SCHEDULERTRAFFICSPLITRESPONSES.fields_by_name['responses'].message_type = _SCHEDULERTRAFFICSPLITRESPONSE
_SCHEDULERTRAFFICSPLITRESPONSES.fields_by_name['tagged_responses'].message_type = _SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY
_SCHEDULERTRAFFICSPLITREQUEST.fields_by_name['request'].message_type = test__platform_dot_request__pb2._REQUEST
_SCHEDULERTRAFFICSPLITRESPONSE.fields_by_name['skylab_request'].message_type = test__platform_dot_request__pb2._REQUEST
DESCRIPTOR.message_types_by_name['SchedulerTrafficSplitRequests'] = _SCHEDULERTRAFFICSPLITREQUESTS
DESCRIPTOR.message_types_by_name['SchedulerTrafficSplitResponses'] = _SCHEDULERTRAFFICSPLITRESPONSES
DESCRIPTOR.message_types_by_name['SchedulerTrafficSplitRequest'] = _SCHEDULERTRAFFICSPLITREQUEST
DESCRIPTOR.message_types_by_name['SchedulerTrafficSplitResponse'] = _SCHEDULERTRAFFICSPLITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchedulerTrafficSplitRequests = _reflection.GeneratedProtocolMessageType('SchedulerTrafficSplitRequests', (_message.Message,), dict(

  TaggedRequestsEntry = _reflection.GeneratedProtocolMessageType('TaggedRequestsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY,
    __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitRequests.TaggedRequestsEntry)
    ))
  ,
  DESCRIPTOR = _SCHEDULERTRAFFICSPLITREQUESTS,
  __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitRequests)
  ))
_sym_db.RegisterMessage(SchedulerTrafficSplitRequests)
_sym_db.RegisterMessage(SchedulerTrafficSplitRequests.TaggedRequestsEntry)

SchedulerTrafficSplitResponses = _reflection.GeneratedProtocolMessageType('SchedulerTrafficSplitResponses', (_message.Message,), dict(

  TaggedResponsesEntry = _reflection.GeneratedProtocolMessageType('TaggedResponsesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY,
    __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
    # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitResponses.TaggedResponsesEntry)
    ))
  ,
  DESCRIPTOR = _SCHEDULERTRAFFICSPLITRESPONSES,
  __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitResponses)
  ))
_sym_db.RegisterMessage(SchedulerTrafficSplitResponses)
_sym_db.RegisterMessage(SchedulerTrafficSplitResponses.TaggedResponsesEntry)

SchedulerTrafficSplitRequest = _reflection.GeneratedProtocolMessageType('SchedulerTrafficSplitRequest', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULERTRAFFICSPLITREQUEST,
  __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitRequest)
  ))
_sym_db.RegisterMessage(SchedulerTrafficSplitRequest)

SchedulerTrafficSplitResponse = _reflection.GeneratedProtocolMessageType('SchedulerTrafficSplitResponse', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULERTRAFFICSPLITRESPONSE,
  __module__ = 'test_platform.steps.scheduler_traffic_split_pb2'
  # @@protoc_insertion_point(class_scope:test_platform.steps.SchedulerTrafficSplitResponse)
  ))
_sym_db.RegisterMessage(SchedulerTrafficSplitResponse)


DESCRIPTOR._options = None
_SCHEDULERTRAFFICSPLITREQUESTS_TAGGEDREQUESTSENTRY._options = None
_SCHEDULERTRAFFICSPLITRESPONSES_TAGGEDRESPONSESENTRY._options = None
# @@protoc_insertion_point(module_scope)
