# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unity_robotics_demo_msgs/PositionServiceRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import unity_robotics_demo_msgs.msg

class PositionServiceRequest(genpy.Message):
  _md5sum = "f8e4a2d3805052790871d9acbcc92af5"
  _type = "unity_robotics_demo_msgs/PositionServiceRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """PosRot input

================================================================================
MSG: unity_robotics_demo_msgs/PosRot
float32 pos_x
float32 pos_y
float32 pos_z
float32 rot_x
float32 rot_y
float32 rot_z
float32 rot_w

"""
  __slots__ = ['input']
  _slot_types = ['unity_robotics_demo_msgs/PosRot']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       input

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PositionServiceRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.input is None:
        self.input = unity_robotics_demo_msgs.msg.PosRot()
    else:
      self.input = unity_robotics_demo_msgs.msg.PosRot()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.input.pos_x, _x.input.pos_y, _x.input.pos_z, _x.input.rot_x, _x.input.rot_y, _x.input.rot_z, _x.input.rot_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = unity_robotics_demo_msgs.msg.PosRot()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.input.pos_x, _x.input.pos_y, _x.input.pos_z, _x.input.rot_x, _x.input.rot_y, _x.input.rot_z, _x.input.rot_w,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.input.pos_x, _x.input.pos_y, _x.input.pos_z, _x.input.rot_x, _x.input.rot_y, _x.input.rot_z, _x.input.rot_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.input is None:
        self.input = unity_robotics_demo_msgs.msg.PosRot()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.input.pos_x, _x.input.pos_y, _x.input.pos_z, _x.input.rot_x, _x.input.rot_y, _x.input.rot_z, _x.input.rot_w,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unity_robotics_demo_msgs/PositionServiceResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import unity_robotics_demo_msgs.msg

class PositionServiceResponse(genpy.Message):
  _md5sum = "f40a8c9d0d5d19208415bd9f23e5aa3f"
  _type = "unity_robotics_demo_msgs/PositionServiceResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """PosRot output

================================================================================
MSG: unity_robotics_demo_msgs/PosRot
float32 pos_x
float32 pos_y
float32 pos_z
float32 rot_x
float32 rot_y
float32 rot_z
float32 rot_w

"""
  __slots__ = ['output']
  _slot_types = ['unity_robotics_demo_msgs/PosRot']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       output

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PositionServiceResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.output is None:
        self.output = unity_robotics_demo_msgs.msg.PosRot()
    else:
      self.output = unity_robotics_demo_msgs.msg.PosRot()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.output.pos_x, _x.output.pos_y, _x.output.pos_z, _x.output.rot_x, _x.output.rot_y, _x.output.rot_z, _x.output.rot_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = unity_robotics_demo_msgs.msg.PosRot()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.output.pos_x, _x.output.pos_y, _x.output.pos_z, _x.output.rot_x, _x.output.rot_y, _x.output.rot_z, _x.output.rot_w,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_7f().pack(_x.output.pos_x, _x.output.pos_y, _x.output.pos_z, _x.output.rot_x, _x.output.rot_y, _x.output.rot_z, _x.output.rot_w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.output is None:
        self.output = unity_robotics_demo_msgs.msg.PosRot()
      end = 0
      _x = self
      start = end
      end += 28
      (_x.output.pos_x, _x.output.pos_y, _x.output.pos_z, _x.output.rot_x, _x.output.rot_y, _x.output.rot_z, _x.output.rot_w,) = _get_struct_7f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7f = None
def _get_struct_7f():
    global _struct_7f
    if _struct_7f is None:
        _struct_7f = struct.Struct("<7f")
    return _struct_7f
class PositionService(object):
  _type          = 'unity_robotics_demo_msgs/PositionService'
  _md5sum = '5190f887b70decc2fafe0ae2939b233a'
  _request_class  = PositionServiceRequest
  _response_class = PositionServiceResponse
