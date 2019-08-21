#coding:utf8

#更新 by Master_13
#@20180115

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def process_category(all_event_url,driver):
    total=len(all_event_url)
    print "开始报名"+str(total)+"个活动..."
    cnt=0
    no=0
    for url in all_event_url:
        driver.get(url[0])
        no+=1
        try:
            big_btn=driver.find_element_by_class_name("big-btn")
            if big_btn.text.find(u'取消报名')!=-1 or big_btn.text.find(u'已报名')!=-1:
                continue
            big_btn.click()

            try:    #同意黄金替补
                time.sleep(1)
                sel=Select(driver.find_element_by_class_name("J_applyExtendInfo"))
                sel.select_by_index(1)                
            except:
                pass

            time.sleep(2)            
            ok=driver.find_element_by_id("J_pop_ok")
            ok.click()
            cnt+=1
            print str(cnt)+" success:"+url[1].encode('gbk','ignore')
        except Exception, e:
            print str(no)+' failed:'+url[1].encode('gbk','ignore')
            print format(e)
        time.sleep(1)
    return

def main():
    print '正在执行……'
    skiptext=[u"牙",u"齿",u"搬家",u"口腔"]

    print sys.argv
    print len(sys.argv)
    dper= sys.argv[1]
    print "your dper is:"+dper
    
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36")
    driver = webdriver.Chrome(chrome_options=opts)
    time.sleep(1)
    driver.maximize_window()

    driver.get("http://s.dianping.com/event/shanghai")
    driver.add_cookie({'name':'dper', 'value':dper,'path':'/'})
    driver.get("http://s.dianping.com/event/shanghai")   
    
    tabs=driver.find_element_by_class_name('s-fix-wrap').find_elements_by_tag_name('div')
    
    all_event_url=[]
    for tab in tabs:
        if tab.text.find(u'全部')!=-1:
            continue
        if tab.text.find(u'美食')!=-1: # or tab.text.find(u'玩乐')!=-1 or tab.text.find(u'酒旅')!=-1 or tab.text.find(u'生活服务')!=-1:
            tab.click()
            try:
                while(1): #点击查看更多
                    more=driver.find_element_by_class_name("load-more")
                    more.click()
                    time.sleep(2)
            except:
                pass
            time.sleep(1)
            elements=driver.find_element_by_class_name("activity-lists").find_elements_by_tag_name('li')
            for e in elements:
                a = e.find_element_by_tag_name("a")
                event_url= a.get_attribute("href")
                title=e.find_element_by_tag_name("h4")
                for s in skiptext:
                    if s in title.text:
                        continue
                all_event_url.append((str(event_url),title.text))                    
    
    process_category(all_event_url, driver)
              
    driver.quit()

if __name__ == '__main__':
    main()
