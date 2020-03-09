"""
pymysql与数据库交互分为几步：
1. 连接数据库
    :param host: Host where the database server is located
    :param user: Username to log in as
    :param password: Password to use.
    :param database: Database to use, None to not use a particular one.
    :param port: MySQL port to use, default is usually OK. (default: 3306)

2. 创建cursor（车辆

3. 执行sql，进行数据的传递

4. 关闭cursor  关闭数据库的连接
"""
from pymysql import connect

HOST = '192.168.182.128'
USER = 'root'
PASSWORD = '123456'
DATABASE = 'jinse_news'
PORT = 3306
CHARSET = 'utf8'

def data_to_db(sql):
    conn = connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE, port=PORT, charset=CHARSET)

    cs1 = conn.cursor()

    cs1.execute(sql)
    conn.commit()

    cs1.close()
    conn.close()

if __name__ == '__main__':

    sql = 'insert into news (title, summary, child_id) values ("独家 | Bakkt期货合约数据一览", "金色财经报道，Bakkt Volume Bot数据显示，2月26日，Bakkt比特币月度期货合约单日交易额为2932万美元，环比上升135%；未平仓合约量为1128万美元，环比下降4%。", "150119")'
    data_to_db(sql)