import socket
import time
import argparse
import MySQLdb as mdb
import datetime

""" Check if port is open, avoid docker-compose race condition """

parser = argparse.ArgumentParser(description='Check if port is open, avoid\
                                 docker-compose race condition')
parser.add_argument('--service-name', required=True)
parser.add_argument('--ip', required=True)
parser.add_argument('--port', required=True)

args = parser.parse_args()

# Get arguments
service_name = str(args.service_name)
port = int(args.port)
ip = str(args.ip)

print("service_name:{}-port:{}-ip:{}".format(service_name, port, ip))


def run_sql_file(filename, connection):
    '''
    The function takes a filename and a connection as input
    and will run the SQL query on the given connection
    '''
    start = time.time()
    file = open(filename, 'r')
    sql = " ".join(file.readlines())
    print("Start executing: " + filename + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + "\n" + sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    end = time.time()
    print("Time elapsed to run the query:" + str((end - start) * 1000) + ' ms')


# Infinite loop
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        connection = mdb.connect(
            host='mysql',
            user='dev',
            passwd='dev',
            db='recipe_db',
            use_unicode=True,
            charset='utf8'
        )
        print("{0} port is open! ->  Bye!".format(service_name))
        break
    else:
        print("{0} port is not open! I'll check it soon!".format(service_name))
        time.sleep(3)
