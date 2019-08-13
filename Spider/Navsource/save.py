import pymysql
import pymongo

class SaveMongo():
    ...

class SaveSql():
    """创建对象时传入需要连接的数据库名字，以及插入数据的sql语句"""
    def __init__(self, db, sql):
        self.db = db
        self.sql = sql

    def connect_db(self):
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='123456',
            db=self.db,
            # 链接编码
            charset='utf8mb4'
        )
        return connection

    def save_to_mysql(self):
        db = self.connect_db()
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(self.sql)
            # 在增删改时，需要commit不然不会生效
            db.commit()
        except Exception as e:
            print(e)
            # 添加事务，如果出错，进行回滚
            db.rollback()
