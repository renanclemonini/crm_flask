from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float, Column, Integer, String, Numeric, DateTime, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Estoque_Movimento(db.Model):
    id_movimento: Mapped[int] = mapped_column(Integer, autoincrement=True)
    id_produto: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantidade_produto: Mapped[int] = mapped_column(Integer, nullable=False)
    valor_unitario: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)
    valor_total: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)
    data_movimento: Mapped[str] = mapped_column(String(30), primary_key=True)
    numero_nf: Mapped[int] = mapped_column(Integer, primary_key=True)
    tipo_movimento: Mapped[str] = mapped_column(Enum('E', 'S'), primary_key=True)
    status_movimento: Mapped[str] = mapped_column(Enum('Processado', 'Pendente', 'Entregue'))
    descricao: Mapped[str] = mapped_column(String(255))

    def __int__(self, id_produto, quantidade_produto, valor, data_p, numero_nf, tipo_movimento):
        self.id_produto = id_produto
        self.quantidade_produto = quantidade_produto
        self.valor = valor
        self.data_p = data_p
        self.numero_nf = numero_nf
        self.tipo_movimento = tipo_movimento

class Produto(db.Model):
    id_produto: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome_produto: Mapped[str] = mapped_column(String(100), nullable=False)
    valor_produto: Mapped[float] = mapped_column(Float, nullable=False)
    id_categoria: Mapped[int] = mapped_column(Integer, nullable=False)

    def __init__(self, nome_produto, valor_produto, id_categoria):
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto
        self.id_categoria = id_categoria


