#Cassandra set up for thermostat database

from cassandra.cluster import Cluster

create_user_table = ''' CREATE TABLE temp_data (
            indoor_time timestamp,
            outdoor_time timestamp,
            out_condition text,
            out_temp_f double,
            in_temp_f double,
            PRIMARY KEY (indoor_time))
        '''

cluster = Cluster()
session = cluster.connect()
session = cluster.connect('environment_data')

session.execute('DROP TABLE temp_data')

session.execute(create_user_table)

#If you want to create an index on a column
#session.execute('CREATE INDEX condIndex ON temp_data(out_condition)')
#session.execute('CREATE INDEX tempIndex ON temp_data(out_temp_f)')
#session.execute('CREATE INDEX timeIndex ON temp_data(outdoor_time)')

cluster.shutdown()


query1 = 'SELECT max(indoor_time), in_temp_f, out_condition, out_temp_f, outdoor_time FROM environment_data.temp_data'

query2 = 'SELECT * FROM environment_data.temp_data'
