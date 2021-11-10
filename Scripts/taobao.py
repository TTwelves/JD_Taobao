# coding:utf-8
import random
from time import sleep
import selenium
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.keys import Keys


class taobao:

    def random_second(self):
        second = random.randint(2,20)
        return int(second)

    def save_yaml(self, data: list):
        with open('./taobao-dog.yaml', 'a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def get_datas(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        # todo:复用浏览器内进行操作
        Total_data = []
        clickable = self.driver.find_element_by_xpath('//a[@data-key="s" and @data-url="pager"]/span[2]').is_enabled()

        while clickable is True:
            sleep(10)

            # li_list = self.driver.find_elements_by_xpath('//ul[@id="list-container"]/li')
            li_list = self.driver.find_elements_by_xpath('//a[@class="shop-name J_shop_name"]')
            print(len(li_list))

            if len(li_list) != 20:
                action1 = TouchActions(self.driver)
                action1.scroll(0, -5000).perform()
                action1.scroll(0, 5000).perform()
                self.driver.refresh()
                continue


            for l in li_list:
                datas = []
                # trace_uid_element = l.find_element_by_xpath('./ul/li/a')
                # trace_uid = trace_uid_element.get_attribute("trace-uid")
                trace_uid = l.get_attribute("trace-uid")

                list1 = self.driver.find_elements_by_xpath(f'//a[@trace-uid="{trace_uid}"]')
                shop_name = list1[1].text
                shop_link = list1[1].get_attribute("href")
                shop_rank = str(list1[2].get_attribute("class")).replace("rank seller-rank-","")
                shop_uid = list1[3].text

                datas.append(shop_name)
                datas.append(shop_rank)
                datas.append(shop_link)
                datas.append(shop_uid)

                print(datas)
                Total_data.append(datas)
                action1 = TouchActions(self.driver)
                action1.scroll(0, 250).perform()
                sleep(3)

            self.save_yaml(Total_data)
            print("total:", len(Total_data))
            Total_data = []
            sleep(self.random_second())
            # 点击下一页
            clickable = self.driver.find_element_by_xpath(
                '//a[@data-key="s" and @data-url="pager"]/span[2]').is_enabled()
            self.driver.find_element_by_xpath('//a[@data-key="s" and @data-url="pager"]/span[2]').click()


if __name__ == '__main__':
    t = taobao()
    t.get_datas()
