# coding: utf-8
import requests
import hashlib
from operator import itemgetter


# 填写测试方的api_secret
api_secret_key = ''


def make_sign(d):
    md5_str = ''
    # 请求参数都需要转成utf-8之后再进行计算
    for k, v in sorted(d.items(), key=itemgetter(0)):
        # if isinstance(v, unicode):
        #     v = v.encode('utf-8')
        if isinstance(v, str):
            print('#######################')
            md5_str += "%s%s" % (k, v)

    md5_str += api_secret_key
    return hashlib.md5(md5_str).hexdigest().lower()


def make_sign_36(d):
    md5_str = ''
    # 请求参数都需要转成utf-8之后再进行计算
    for k, v in sorted(d.items(), key=itemgetter(0)):
        if isinstance(v, str):
            md5_str += "%s%s" % (k, v)

    md5_str += api_secret_key
    m = hashlib.md5()
    m.update(md5_str.encode("utf8"))
    return m.hexdigest().lower()


def get_request(url, payload):
    payload['api_sign'] = make_sign_36(payload)
    r = requests.post(url, data=payload)

    return r
