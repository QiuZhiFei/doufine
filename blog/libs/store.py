# encoding: utf-8

# import MySQLdb
import libs.sql_helper as _db




def addWB(item):
    item = {}
    item["created_at"] = "07-18"
    item["id"] = "4263234627933203"
    item["original_pic"] = "http://wx2.sinaimg.cn/large/badcfc6dly1fteaufdl16j20qo0zkh0s.jpg"
    item["scheme"] = "https://m.weibo.cn/status/Gqx1kxhMT?mblogid=Gqx1kxhMT&luicode=10000011&lfid=1076033135044717"
    item["text"] = "伏树哀鸣，为爱恨所苦者，蝉。"
    item["title"] = "路长人短"

    cmd = "INSERT INTO `application` \
    (`id`, `item_id`, `created_at`, \
    `original_pic`, `scheme`, `text`, \
    `title`) \
    VALUES \
    (NULL, '1', '2', '3', '4', '5', '6')"

    _db.execute(cmd)
    
    # db = MySQLdb.connect("127.0.0.1", "root", "", "doufine", charset='utf8')
    # cursor = db.cursor()

    # try:
    #     cursor.execute(cmd)
    #     db.commit()
    # except:
    #     db.rollback()
    
    # db.close()

