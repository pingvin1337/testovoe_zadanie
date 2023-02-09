# import requests
# import psycopg2
# from psycopg2 import Error
# from psycopg2.extras import Json, DictCursor

# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# import _sqlite3

# url = "https://nodus.caseguru.ru/trainee/tasks"
 
# data = {
#     "task": 3,
#     "result":"abggafgfgafgfgafgfg",
#     # // "passion": "coding",
# }
 
# response = requests.post(url, json=data)
 
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())









# Подключение к существующей базе данных
connection = psycopg2.connect( dbname = "testtask",
                                user="trainee_user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="trainee_pass",
                                  host="95.183.10.174",
                                  port="5432")
#     cursor.close()
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# Курсор для выполнения операций с базой данных
cursor = connection.cursor()
cursor.execute("""SELECT ROUND(AVG(o.processing_time)) as avg_processing_time, o.managerid
FROM orders as o
JOIN statuses as s ON o.statuscode = s.code  
WHERE
o.createdat BETWEEN '2022-06-1' and '2022-09-01' and status_group = 'Выполнен'
GROUP BY o.managerid
ORDER BY avg_processing_time desc
LIMIT 1
""")
print(cursor.fetchall())



# ("SELECT orders.managerid, orders.processing_time FROM orders JOIN statuses ON orders.statuscode = statuses.code WHERE orders.createdat BETWEEN '2022-06-1' and '2022-08-31'   " )
#   SELECT MAX(avg_salary) FROM (SELECT managerid, AVG(processing_time) AS avg_salary FROM orders GROUP BY managerid) AS maxSalary   
#    "SELECT managerid, avgsal FROM( SELECT managerid, avg(processing_time) AS avgsal FROM orders GROUP BY managerid) WHERE avgsal = (SELECT MAX(avgsal) FROM(SELECT managerid, AVG(processing_time) AS avgsal FROM orders GROUP BY managerid))
# "SELECT orders.managerid, FLOOR(AVG(orders.processing_time)) as avg_time FROM (SELECT orders.id, orders.createdat, orders.processing_time, orders.managerid FROM orders INNER JOIN (SELECT statuses.code, statuses.name, statuses.status_group FROM statuses WHERE status_group = "Выполнен") statuses ON statuses.code = orders.statuscode WHERE orders.createdat BETWEEN '2022-06-1' and '2022-08-31') orders GROUP BY orders.managerid ORDER BY avg_time DESC LIMIT 1 
# select
#     orders.managerid,
#     floor(avg(orders.processing_time)) as avg_time
# from
#     (
#     select
#         orders.id ,
#         orders.createdat ,
#         orders.statuscode ,
#         orders.processing_time ,
#         orders.managerid
#     from
#         orders
#     inner join (
#         select
#             statuses.code,
#             statuses.name,
#             statuses.status_group
#         from
#             statuses
#         where
#             status_group = 'Выполнен' ) statuses
# on
#         statuses.code = orders.statuscode
#     where
#         orders.createdat BETWEEN '2022-06-1' and '2022-08-31'
# group by
#     orders.managerid
# order by
#     avg_time desc
# limit 1




# select floor(max(avg_salary))
# from (select managerid, avg(processing_time) AS avg_salary
#       from orders
#       group by managerid) As maxSalary
