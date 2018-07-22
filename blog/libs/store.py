# encoding: utf-8

# import MySQLdb
import libs.sql_helper as _db


def addWBItemsIfNeeded(items):
    for item in items:
        addWBItemIfNeeded(item)
    

def addWBItemIfNeeded(item):
    item_id = item.get("item_id", "")
    if item_id == "":
        return
    
    items = searchWB(item_id)

    # print ("add items == %s %s" % (items, len(items)))
    print ("add items == %s %s" % (item_id, len(items)))

    if len(items) == 0:
        print ("add item == " % item)
        addWB(item)


def addWB(item):
    # item = {}
    # item["item_id"] = "4263234627933203"
    # item["created_at"] = "07-18"
    # item["original_pic"] = "http://wx2.sinaimg.cn/large/badcfc6dly1fteaufdl16j20qo0zkh0s.jpg"
    # item["scheme"] = "https://m.weibo.cn/status/Gqx1kxhMT?mblogid=Gqx1kxhMT&luicode=10000011&lfid=1076033135044717"
    # item["text"] = "伏树哀鸣，为爱恨所苦者，蝉。"
    # item["title"] = "路长人短"

    cmd = "INSERT INTO `application` \
    (`id`, `item_id`, `created_at`, \
    `original_pic`, `scheme`, `text`, \
    `title`) \
    VALUES \
    (NULL, '%s', '%s', '%s', '%s', '%s', '%s')" % \
    (item["item_id"], item["created_at"], item["original_pic"], \
    item["scheme"], item["text"], item["title"])

    # print "cmd == %s" % cmd

    _db.execute(cmd)
    
    # db = MySQLdb.connect("127.0.0.1", "root", "", "doufine", charset='utf8')
    # cursor = db.cursor()

    # try:
    #     cursor.execute(cmd)
    #     db.commit()
    # except:
    #     db.rollback()
    
    # db.close()


def searchWB(item_id):
    cmd = "SELECT * FROM `application` \
    WHERE \
    `item_id` = '%s'" % item_id

    cursor = _db.execute(cmd)

    res = cursor.fetchall()

    items = []
    for data in res:
        item = {}
        item["id"] = data[0]
        item["item_id"] = data[1]
        item["created_at"] = data[2]
        item["original_pic"] = data[3]
        item["scheme"] = data[4]
        item["text"] = data[5]
        item["title"] = data[6]
        items.append(item)

    return  items