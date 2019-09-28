from cassandra.cluster import Cluster

cluster = Cluster()
connect = cluster.connect('keyspace1')

batch = """
BEGIN BATCH
 update keyspace1."Stores_Holiday_Presents_Client" set season_year = 'Autinm' 
 where holiday_name = 'Christmas' and  present_name ='Smartphone' and passport_num = 102 and store_name ='Comfy';

  update keyspace1."Stores_Holiday_Presents_Client" set character = {name:'Olga',age: 30,gender :'W',family_state: 'Notmarried'}
   where holiday_name = '8 March' and present_name ='Flowers' and passport_num= 101 and store_name = 'Silpo' ;

APPLY BATCH;
"""
connect.execute(batch)