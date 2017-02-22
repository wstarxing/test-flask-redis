# -*- coding: UTF-8 -*-
from redis import Redis, ConnectionPool

pool = ConnectionPool(host='192.168.0.203', port=6379, db=3)
r = Redis(connection_pool=pool)

'''参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行
'''


# 在Redis中设置值，默认不存在则创建，存在则修改
def set2(key, value):
    r.set(key, value)
    result = r.get(key)
    print result
    r.mset(name1='zhangsan', name2='lisi')  # 批量设置值
    print r.get('name1')
    print r.mget('name1', 'name2')  # 批量获取
    print r.getset("name1", "wangwu")  # 设置新值，打印原值
    print r.get("name1")
    r.setrange("name", 1, "z")  # 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
    print(r.getrange("name", 0, 3))  # 根据字节获取子序列
    print(r.strlen("name"))  # 返回name对应值的字节长度（一个汉字3个字节）
    print(r.incr("mount", amount=2))  # 自增mount对应的值，当mount不存在时，则创建mount＝amount，否则，则自增,amount为自增数(整数)
    # incrbyfloat(self, name, amount=1.0)
    # decr(self, name, amount=1)
    r.append("name", "lisi")  # 在name对应的值后面追加内容


def hash2():
    r.hset('dic_name', 'a1', 'aa')
    r.hset('dic_name', 'b1', 'bb')
    print(r.hgetall("dic_name"))
    print(r.hget('dic_name', 'a1'))


def list2(a, b, c):
    list_name = a + b
    r.rpush(list_name, c)
    if r.llen(list_name) > 5:
        r.lpop(list_name)
    print r.llen(list_name)


if __name__ == '__main__':
    b = {'a':'a'}
    # list2('a', 'b', b)
    print r.lindex('ab',4)
