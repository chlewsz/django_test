import pymysql


# 添加该配置后Django使用pymysql库而不是使用python2.X中使用的mysql-python库
pymysql.install_as_MySQLdb()
