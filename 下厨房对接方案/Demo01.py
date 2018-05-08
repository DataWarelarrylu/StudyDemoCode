from 下厨房对接方案.lib import  *
import datetime
import simplejson
import json
import pandas as pd

def order_sync(bdate,edate):
    url = 'https://openapi.xiachufang.com/order/sync'

    values = {
        'start_modified': bdate,
        'end_modified': edate,
        'page_no': 1,
        'page_size': 20,
    }

    # 以下的参数也都需要是utf-8编码的，windows下的开发者可能需要额外的编码工作。
    data = {
        'api_key': api_key,
        'version': '1',
        'time': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        'param': simplejson.dumps(values)
    }
    r = get_request(url, data)
    return (json.loads(r.text))
# 订单明细
def getorderDetail(bdate,edate):
    orderstatus = []  # 订单状态
    consign_time = []  # 卖家发货时间
    receiver_state = []  # 收货人的所在省份
    receiver_city = []  # 收货人的所在城市
    receiver_district = []  # 收货人的所在地区
    receiver_name = []  # 收货人的姓名
    receiver_phone = []  # 收货人的电话号码
    alipay_trade_no = []  # 支付宝交易流水号
    pay_time = []  # 付款时间
    tid = [] #交易订单ID
    res = order_sync(bdate,edate)
    # print(res)
    for i in (res['result']['trades']):
        orderstatus.append(i['status'])
        consign_time.append(i['consign_time'])
        receiver_state.append(i['receiver_state'])
        receiver_city.append(i['receiver_city'])
        receiver_district.append(i['receiver_district'])
        receiver_name.append(i['receiver_name'])
        receiver_phone.append(i['receiver_phone'])
        alipay_trade_no.append(i['alipay_trade_no'])
        pay_time.append(i['pay_time'])
        tid.append(i['tid'])

    dataframe = {
        'orderstatus': orderstatus,
        'consign_time': consign_time,
        'receiver_state': receiver_state,
        'receiver_city': receiver_city,
        'receiver_district': receiver_district,
        'receiver_name': receiver_name,
        'receiver_phone': receiver_phone,
        'alipay_trade_no': alipay_trade_no,
        'pay_time': pay_time,
        'tid':tid
    }
    df = pd.DataFrame(dataframe)
    return(df)

if __name__ == '__main__':
    now_time = datetime.datetime.now()
    yes_time =now_time + datetime.timedelta(days=-1)
    print(yes_time.strftime('%Y-%m-%d %H:%M:%S'), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    res =order_sync(yes_time.strftime('%Y-%m-%d ')+'00:00:00', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print(res)
    # print(sys.argv[1], sys.argv[2])
    # res =getorderDetail(sys.argv[1],sys.argv[2])
    # res.to_csv('/root/acorn_xcf/data/orderdetail'+datetime.datetime.now().strftime("%Y%m%d")+'.csv')


