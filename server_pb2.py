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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\x12\x08servidor\"`\n\x11\x43riarCanalRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\'\n\ntipo_canal\x18\x02 \x01(\x0e\x32\x13.servidor.TipoCanal\x12\x14\n\x0cnome_criador\x18\x03 \x01(\t\"&\n\x12ResponseCriarCanal\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"9\n\x13RemoverCanalRequest\x12\x0c\n\x04nome\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\"(\n\x14RemoverCanalResponse\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"M\n\x0fMensagemRequest\x12\x12\n\nnome_canal\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\x12\x10\n\x08mensagem\x18\x03 \x01(\t\"$\n\x10MensagemResponse\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"?\n\x13\x41ssinarCanalRequest\x12\x12\n\nnome_canal\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\"I\n\x1dRemoverAssinaturaCanalRequest\x12\x12\n\nnome_canal\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\"(\n\x14ResponseAssinarCanal\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"2\n\x1eResponseRemoverAssinaturaCanal\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"4\n\x1c\x45nviarMensagensStreamRequest\x12\x14\n\x0cnome_cliente\x18\x01 \x01(\t\"2\n\x1a\x45nviarMensagemUnicaRequest\x12\x14\n\x0cnome_cliente\x18\x01 \x01(\t\"T\n\x16MensagemStreamResponse\x12\x12\n\nnome_canal\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\x12\x10\n\x08mensagem\x18\x03 \x01(\t\"S\n\x15ResponseMensagemUnica\x12\x12\n\nnome_canal\x18\x01 \x01(\t\x12\x14\n\x0cnome_criador\x18\x02 \x01(\t\x12\x10\n\x08mensagem\x18\x03 \x01(\t\"&\n\x12ListaCanaisRequest\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"\'\n\x13ListaCanaisResponse\x12\x10\n\x08mensagem\x18\x01 \x01(\t*&\n\tTipoCanal\x12\x0b\n\x07SIMPLES\x10\x00\x12\x0c\n\x08MULTIPLO\x10\x01\x32\xac\x05\n\x07Greeter\x12\x42\n\x05\x43riar\x12\x1b.servidor.CriarCanalRequest\x1a\x1c.servidor.ResponseCriarCanal\x12H\n\x07Remover\x12\x1d.servidor.RemoverCanalRequest\x1a\x1e.servidor.RemoverCanalResponse\x12M\n\x0c\x41ssinarCanal\x12\x1d.servidor.AssinarCanalRequest\x1a\x1e.servidor.ResponseAssinarCanal\x12k\n\x16RemoverAssinaturaCanal\x12\'.servidor.RemoverAssinaturaCanalRequest\x1a(.servidor.ResponseRemoverAssinaturaCanal\x12H\n\x0fReceberMensagem\x12\x19.servidor.MensagemRequest\x1a\x1a.servidor.MensagemResponse\x12\x63\n\x15\x45nviarMensagensStream\x12&.servidor.EnviarMensagensStreamRequest\x1a .servidor.MensagemStreamResponse0\x01\x12\\\n\x13\x45nviarMensagemUnica\x12$.servidor.EnviarMensagemUnicaRequest\x1a\x1f.servidor.ResponseMensagemUnica\x12J\n\x0bListaCanais\x12\x1c.servidor.ListaCanaisRequest\x1a\x1d.servidor.ListaCanaisResponseB&\n\x1cufabc.aluno.sistemas.clienteP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034ufabc.aluno.sistemas.clienteP\001\242\002\003HLW'
  _globals['_TIPOCANAL']._serialized_start=974
  _globals['_TIPOCANAL']._serialized_end=1012
  _globals['_CRIARCANALREQUEST']._serialized_start=26
  _globals['_CRIARCANALREQUEST']._serialized_end=122
  _globals['_RESPONSECRIARCANAL']._serialized_start=124
  _globals['_RESPONSECRIARCANAL']._serialized_end=162
  _globals['_REMOVERCANALREQUEST']._serialized_start=164
  _globals['_REMOVERCANALREQUEST']._serialized_end=221
  _globals['_REMOVERCANALRESPONSE']._serialized_start=223
  _globals['_REMOVERCANALRESPONSE']._serialized_end=263
  _globals['_MENSAGEMREQUEST']._serialized_start=265
  _globals['_MENSAGEMREQUEST']._serialized_end=342
  _globals['_MENSAGEMRESPONSE']._serialized_start=344
  _globals['_MENSAGEMRESPONSE']._serialized_end=380
  _globals['_ASSINARCANALREQUEST']._serialized_start=382
  _globals['_ASSINARCANALREQUEST']._serialized_end=445
  _globals['_REMOVERASSINATURACANALREQUEST']._serialized_start=447
  _globals['_REMOVERASSINATURACANALREQUEST']._serialized_end=520
  _globals['_RESPONSEASSINARCANAL']._serialized_start=522
  _globals['_RESPONSEASSINARCANAL']._serialized_end=562
  _globals['_RESPONSEREMOVERASSINATURACANAL']._serialized_start=564
  _globals['_RESPONSEREMOVERASSINATURACANAL']._serialized_end=614
  _globals['_ENVIARMENSAGENSSTREAMREQUEST']._serialized_start=616
  _globals['_ENVIARMENSAGENSSTREAMREQUEST']._serialized_end=668
  _globals['_ENVIARMENSAGEMUNICAREQUEST']._serialized_start=670
  _globals['_ENVIARMENSAGEMUNICAREQUEST']._serialized_end=720
  _globals['_MENSAGEMSTREAMRESPONSE']._serialized_start=722
  _globals['_MENSAGEMSTREAMRESPONSE']._serialized_end=806
  _globals['_RESPONSEMENSAGEMUNICA']._serialized_start=808
  _globals['_RESPONSEMENSAGEMUNICA']._serialized_end=891
  _globals['_LISTACANAISREQUEST']._serialized_start=893
  _globals['_LISTACANAISREQUEST']._serialized_end=931
  _globals['_LISTACANAISRESPONSE']._serialized_start=933
  _globals['_LISTACANAISRESPONSE']._serialized_end=972
  _globals['_GREETER']._serialized_start=1015
  _globals['_GREETER']._serialized_end=1699
# @@protoc_insertion_point(module_scope)
