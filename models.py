from datetime import datetime
from pydantic import BaseModel


class Categoria(BaseModel):
    id: int
    nome: str


class Produto(BaseModel):
    id: int
    nome: str
    marca: str
    valor: float
    categoria: Categoria


class Venda(BaseModel):
    id: int
    total: float
    timestamp: datetime
    metodo_pagamento: str


class ItemVenda(BaseModel):
    id: int
    venda: Venda
    produto: Produto
    quantidade: float


class User(BaseModel):
    id: int
    nome: str
    is_admin: bool
