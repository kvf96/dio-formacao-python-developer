from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, text

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData()

user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('email', String(40)),
    Column('nickname', String(40), nullable=False)
)

user_prefs = Table(
    'user_prefs',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

metadata_obj.create_all(engine)

