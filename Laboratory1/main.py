from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

cluster = Cluster()
connect= cluster.connect('keyspace1')


with open('drop_buts.cql', mode='r') as f:
    text = f.read()
    stmts = text.split(';')
    for i in stmts:
        stmt = i.strip()
        if stmt != '':
            print(f'Executing {stmt}')
            query = SimpleStatement(stmt, consistency_level=ConsistencyLevel.QUORUM)
            connect.execute(query)
            print(f'{stmt} - done')

with open('create_buts.cql', mode='r') as f:
    text = f.read()
    stmts = text.split(';')
    for i in stmts:
        stmt = i.strip()
        if stmt != '':
            print(f'Executing {stmt}')
            query = SimpleStatement(stmt, consistency_level=ConsistencyLevel.ALL)
            connect.execute(query)
            print(f'{stmt} - done')
with open('work_buts.cql', mode='r') as f:
    text = f.read()
    stmts = text.split(';')
    for i in stmts:
        stmt = i.strip()
        if stmt != '':
            print(f'Executing {stmt}')
            query = SimpleStatement(stmt, consistency_level=ConsistencyLevel.ONE)
            connect.execute(query)
            print(f'{stmt} - done')
