from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser = webdriver.Chrome()
# wait = WebDriverWait(browser, 10)
import pandas as pd
import re
import requests
from sqlalchemy import create_engine
engine = create_engine("oracle://name:passwd@127.0.0.1:1521/acornbi")
def getStoreLink():
    browser.get('http://www.bjda.gov.cn/eportal/ui?pageId=331148')

def GetYaodianDetail(url):
    v_storename=[]
    v_num =[]
    v_zhuce = []
    v_ware = []
    v_gsp = []
    vurl=[]
    res = requests.get(url).text
    v_pa=re.compile(r'<td>(.*?)</td>')
    vdata = re.findall(v_pa,res)
    v_storename.append(vdata[0])
    v_num.append(vdata[1])
    v_zhuce.append(vdata[5])
    v_ware.append(vdata[6])
    v_gsp.append(vdata[11])
    vurl.append(url)
    data ={
        "vlink":vurl,
        "v_storename":v_storename,
        "v_num":v_num,
        "v_zhuce":v_zhuce,
        "v_ware":v_ware,
        "v_gsp":v_gsp
    }
    df = pd.DataFrame(data)
    df.to_sql('yaopin_detail',engine,if_exists='append',index=None)


def nextPage(page_number):
    browser.get('http://www.bjda.gov.cn/eportal/ui?pageId=331148')
    browser.execute_script("document.getElementById('currentPage').value="+page_number+";document.getElementById('currentPage').form.submit();")
    wait = WebDriverWait(browser, 10)
    res = browser.page_source
    v_pa = re.compile(r'<td style="text-align:center;"><a href="(.*?)>.*?')
    vdata = re.findall(v_pa, res)
    data ={"vdata":vdata,
           "vnum":page_number}
    df =pd.DataFrame(data)
    # print(df)
    df.to_sql('yaopin_new',engine,if_exists='append',index=None)

    # for link in browser.find_elements_by_xpath('//*[@id="form"]/div[2]/table/tbody/tr[4]//a'):
    #     print(link.get_attribute('href'))
if __name__=='__main__':
    # 得到链接的代码
     for i in range(1,279):
         nextPage(str(i))
    # 得到明细数据的代码
    # for i in dataList:
    #   GetYaodianDetail(i)