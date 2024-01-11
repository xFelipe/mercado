from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Categoria(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    nome: str


class Produto(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    nome: str
    marca: str
    valor: float
    categoria: Categoria


class Venda(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    total: float
    timestamp: datetime
    metodo_pagamento: str


class ItemVenda(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    venda: Venda
    produto: Produto
    quantidade: float


class User(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    nome: str
    is_admin: bool
