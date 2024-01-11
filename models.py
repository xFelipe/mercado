from datetime import datetime
from pydantic import BaseModel


class Categoria(BaseModel):
    nome: str


class Produto(BaseModel):
    nome: str
    marca: str
    valor: float
    categoria: Categoria


class Venda(BaseModel):
    total: float
    timestamp: datetime
    metodo_pagamento: str


class ItemVenda(BaseModel):
    venda: Venda
    produto: Produto
    quantidade: float


class User(BaseModel):
    nome: str
    is_admin: bool
