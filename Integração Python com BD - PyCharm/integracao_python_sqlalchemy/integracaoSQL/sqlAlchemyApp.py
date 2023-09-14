#pip install sqlalchemy

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

# A classe User é herança de Base
class User(Base):
    __tablename__ = "user"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    #relacionamento entre as tabelas,classes:
    #para não ter inconsistencias dentro do banco de dados, definir o cascade="all, delete-orphan"
    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    #representação da classe:
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    #relacionamento entre as tabelas,classes:
    user = relationship("User", back_populates="address")

    # representação da classe:
    def __repr__(self):
        return f"Address (id={self.id}, email={self.email})"


print(User.__tablename__)

#conexão com o banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#poder verificar o banco de dados criado
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

#Criar sessão para persistir dados no SQLite
with Session(engine) as session:
    maria = User(
        name='maria',#deixar a variavel em letra minuscula
        fullname='Maria Silva',
        address=[Address(email='maria.silva@email.com')]
    )

    jose = User(
        name='jose',
        fullname='José Silva',
        address=[Address(email='jose.silva@email.com'),
                 Address(email='jose.silva@email.org')]
    )

    joao = User(
        name='joão',
        fullname='João Silva'
    )

    #enviando para o banco (persistencia de dados)
    session.add_all([maria, jose, joao])
    session.commit()


#consultar informações no banco de dados
print("\nBuscar usuário pelo nome: ")
stmt = select(User).where(User.name.in_(['jose']))
for user in session.scalars(stmt):
    print(user)

print("\nBuscar email por id do usuário: ")
stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)

print("\nUsuários em ordem decrescente: ")
stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    print(result)

print("\nUtilizando o 'join': ")
stmt_join = select(User.fullname, Address.email).join_from(User, Address)
print(stmt_join)
for result in session.scalars(stmt_join):#o scalars pega apenas o primeiro resultado, no caso é o nome do usuário
    print(result)

print("\nExecutando statement a partir da connection :")
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for result in results:
    print(result)

print("\nUtilizando 'count' na tabela User: ")
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)