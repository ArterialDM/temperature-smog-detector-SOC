import pymysql
import json
from bottle import route,run

def add_info(info_json):
    print(info_json)
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1999113WDM', db='soc')
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        info=json.loads(info_json)
        degree=info["degree"]
        sql = "INSERT INTO info(degree) VALUES (%f)" % (degree)
        cursor.execute(sql)
        con.commit()
        return True
    except Exception as e:
        con.rollback()
        print(e)
        return False
    finally:
        con.close()

def get_degree():
    sql="SELECT degree,CAST(time AS CHAR) AS time FROM info"
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1999113WDM', db='soc')
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)
        con.commit()
        result = cursor.fetchmany(12)
        result_json = json.dumps(result)
        return result_json
    except Exception as e:
        print(e)
        return ""
    finally:
        con.close()

@route('/')
def index():
    return 'hello, bottle'

@route('/addInfo/<info_json>')
def add_info_controller(info_json):
    if (add_info(info_json)==True):
        return "1"
    else:
        return "-1"

@route('/getDegree')
def get_degree_controller():
    return get_degree()
run(host = 'localhost', port = 80)
