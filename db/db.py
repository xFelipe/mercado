from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy import Float, Enum, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


# Create the async engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()


class MetodoPagamento(Enum):
    CREDITO = 'CREDITO'
    DEBITO = 'DEBITO'
    DINHEIRO = 'DINHEIRO'
    PIX = 'PIX'


class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    nome = Column(String, nullable=False)


class Produto(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    nome = Column(String, nullable=False)
    marca = Column(String)
    valor = Column(Float, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    categoria = relationship("Categoria")


class Venda(Base):
    __tablename__ = 'venda'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    total = Column(Float)
    metodo_pagamento = MetodoPagamento
    itens_venda = relationship("ItemVenda", back_populates="venda")


class ItemVenda(Base):
    __tablename__ = 'item_venda'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    venda_id = Column(Integer, ForeignKey('venda.id'))
    venda = relationship("Venda", back_populates="itens_venda")
    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto = relationship("Produto")
    quantidade = Column(Float, nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    nome = Column(String, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)



# Create a session factory
SessionLocal = sessionmaker(bind=engine)


def create_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
