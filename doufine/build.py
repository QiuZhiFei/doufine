# coding: utf-8

import os
import commands
import sys

def build():
    os.system("yarn build")
    os.system("rm -rf /var/www/html")
    os.system("mkdir -p /var/www/html")
    os.system("mv dist/* /var/www/html")
    os.system("cp static/* /var/www/html")

    os.system("cp nginx.conf /etc/nginx/conf.d/")
    # os.system("ln -sf nginx.conf /etc/nginx/conf.d/")

    # result, pwd = commands.getstatusoutput("lsof -i:1111")

    # pwd = os.system("pwd") + "/nginx.conf"
    # pwd = os.system("pwd").read()

    # result, pwd = commands.getstatusoutput("lsof -i:1111")
    # if pwd == "":
    #     result, pwd = commands.getstatusoutput("pwd")
    #     nginx_file_name = pwd + "/nginx.conf"
    #     os.system("sudo nginx -c %s" % nginx_file_name)
    #     # sys.exit("nginx %s" % nginx_file_name)
    #     # sys.exit("nginx 80 没有开启")

    # os.system("yarn | yarn serve")
        
    # print result
    # print pwd, type(pwd), pwd == ""

    # result, pwd = commands.getstatusoutput("pwd")
    # nginx_file_name = pwd + "/nginx.conf"

    # result, nginx_result = commands.getstatusoutput("nginx -c %s" % nginx_file_name)

    # print nginx_file_name
    # print pwd, type(pwd)
    # print result
    # print nginx_result

    # exit()


if __name__ == '__main__':
    build()



