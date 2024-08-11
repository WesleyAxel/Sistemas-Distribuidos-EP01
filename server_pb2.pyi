from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TipoCanal(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIMPLES: _ClassVar[TipoCanal]
    MULTIPLO: _ClassVar[TipoCanal]
SIMPLES: TipoCanal
MULTIPLO: TipoCanal

class CriarCanalRequest(_message.Message):
    __slots__ = ("nome", "tipo_canal", "nome_criador")
    NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    nome: str
    tipo_canal: TipoCanal
    nome_criador: str
    def __init__(self, nome: _Optional[str] = ..., tipo_canal: _Optional[_Union[TipoCanal, str]] = ..., nome_criador: _Optional[str] = ...) -> None: ...

class ResponseCriarCanal(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class RemoverCanalRequest(_message.Message):
    __slots__ = ("nome", "nome_criador")
    NOME_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    nome: str
    nome_criador: str
    def __init__(self, nome: _Optional[str] = ..., nome_criador: _Optional[str] = ...) -> None: ...

class RemoverCanalResponse(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class MensagemRequest(_message.Message):
    __slots__ = ("nome_canal", "nome_criador", "mensagem")
    NOME_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nome_canal: str
    nome_criador: str
    mensagem: str
    def __init__(self, nome_canal: _Optional[str] = ..., nome_criador: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class MensagemResponse(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class AssinarCanalRequest(_message.Message):
    __slots__ = ("nome_canal", "nome_criador")
    NOME_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    nome_canal: str
    nome_criador: str
    def __init__(self, nome_canal: _Optional[str] = ..., nome_criador: _Optional[str] = ...) -> None: ...

class RemoverAssinaturaCanalRequest(_message.Message):
    __slots__ = ("nome_canal", "nome_criador")
    NOME_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    nome_canal: str
    nome_criador: str
    def __init__(self, nome_canal: _Optional[str] = ..., nome_criador: _Optional[str] = ...) -> None: ...

class ResponseAssinarCanal(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class ResponseRemoverAssinaturaCanal(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class EnviarMensagensStreamRequest(_message.Message):
    __slots__ = ("nome_cliente",)
    NOME_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    nome_cliente: str
    def __init__(self, nome_cliente: _Optional[str] = ...) -> None: ...

class EnviarMensagemUnicaRequest(_message.Message):
    __slots__ = ("nome_cliente",)
    NOME_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    nome_cliente: str
    def __init__(self, nome_cliente: _Optional[str] = ...) -> None: ...

class MensagemStreamResponse(_message.Message):
    __slots__ = ("nome_canal", "nome_criador", "mensagem")
    NOME_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nome_canal: str
    nome_criador: str
    mensagem: str
    def __init__(self, nome_canal: _Optional[str] = ..., nome_criador: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ResponseMensagemUnica(_message.Message):
    __slots__ = ("nome_canal", "nome_criador", "mensagem")
    NOME_CANAL_FIELD_NUMBER: _ClassVar[int]
    NOME_CRIADOR_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    nome_canal: str
    nome_criador: str
    mensagem: str
    def __init__(self, nome_canal: _Optional[str] = ..., nome_criador: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class ListaCanaisRequest(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...

class ListaCanaisResponse(_message.Message):
    __slots__ = ("mensagem",)
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    mensagem: str
    def __init__(self, mensagem: _Optional[str] = ...) -> None: ...
