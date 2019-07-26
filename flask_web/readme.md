from sqlalchemy import create_engine
engine create_engine('sqlite://' , echo=False)
with engine.connect() as con:
rs con.execute('SELECT ,')
print rs.fetchone()