# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x08servidor\"`\n\x11\x43riarCanalRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\'\n\ntipo_canal\x18\x02 \x01(\x0e\x32\x13.servidor.TipoCanal\x12\x14\n\x0cnome_criador\x18\x03 \x01(\t\"&\n\x12ResponseCriarCanal\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"9\n\x13RemoverCanalRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\"(\n\x14RemoverCanalResponse\x12\x10\n\x08mensagem\x18\x01 \x01(\t*&\n\tTipoCanal\x12\x0b\n\x07SIMPLES\x10\x00\x12\x0c\n\x08MULTIPLO\x10\x01\x32\x97\x01\n\x07Greeter\x12\x42\n\x05\x43riar\x12\x1b.servidor.CriarCanalRequest\x1a\x1c.servidor.ResponseCriarCanal\x12H\n\x07Remover\x12\x1d.servidor.RemoverCanalRequest\x1a\x1e.servidor.RemoverCanalResponseB6\n\x1dufanc.aluno.sistemas.servidorB\rServidorProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035ufanc.aluno.sistemas.servidorB\rServidorProtoP\001\242\002\003HLW'
  _globals['_TIPOCANAL']._serialized_start=265
  _globals['_TIPOCANAL']._serialized_end=303
  _globals['_CRIARCANALREQUEST']._serialized_start=26
  _globals['_CRIARCANALREQUEST']._serialized_end=122
  _globals['_RESPONSECRIARCANAL']._serialized_start=124
  _globals['_RESPONSECRIARCANAL']._serialized_end=162
  _globals['_REMOVERCANALREQUEST']._serialized_start=164
  _globals['_REMOVERCANALREQUEST']._serialized_end=221
  _globals['_REMOVERCANALRESPONSE']._serialized_start=223
  _globals['_REMOVERCANALRESPONSE']._serialized_end=263
  _globals['_GREETER']._serialized_start=306
  _globals['_GREETER']._serialized_end=457
# @@protoc_insertion_point(module_scope)
