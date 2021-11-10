# coding:utf-8
import random
from time import sleep

import selenium
import yaml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import TouchActions


class demo:

    def random_second(self):
        second = random.randint(2,10)
        return int(second)

    def save_yaml(self, data: list):
        with open('./demo3.yaml', 'a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def get_data(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        # todo:复用浏览器内进行操作
        next_page = self.driver.find_element_by_xpath('//a[@class="pn-next"]').is_enabled()

        Page_data = []
        while next_page is True:

            action1 = TouchActions(self.driver)
            action1.scroll(0, 6000).perform()

            sleep(5)

            li_list = self.driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li')
            for l in li_list:
                data_list = []
                sku = l.get_attribute('data-sku')

                strong_list = self.driver.find_elements_by_xpath(f'//li[@data-sku="{sku}"]//strong')

                # 价格
                price = strong_list[0].text
                data_list.append(price)

                # 评价数
                comments = strong_list[1].text
                data_list.append(comments)

                # 标题
                title = self.driver.find_element_by_xpath(
                    f'//li[@data-sku="{sku}"]//div[@class="p-name p-name-type-3"]//em').text
                data_list.append(title)

                # 店铺名称
                try:
                    shop_name = self.driver.find_element_by_xpath(
                        f'//li[@data-sku="{sku}"]//a[@class="curr-shop hd-shopname"]').text

                    data_list.append(shop_name)
                except NoSuchElementException:
                    data_list.clear()
                    continue

                # 标签
                tags = self.driver.find_elements_by_xpath(f'//li[@data-sku="{sku}"]//div[@class="p-icons"]/i')
                tag = []
                for t in tags:
                    tag.append(t.text)

                data_list.append(tag)

                # 链接
                link = self.driver.find_element_by_xpath(
                    f'//li[@data-sku="{sku}"]//div[@class="p-img"]/a').get_attribute('href')

                data_list.append(link)

                Page_data.append(data_list)
                print("price:", price)
                print("comments:", comments)
                print("title:", title)
                print("shop_name", shop_name)
                print("tags:", tag)
                print("Link:", link)
                print("*******************************************************************")

            self.save_yaml(Page_data)
            Page_data = []
            sleep(self.random_second())
            self.driver.find_element_by_xpath('//a[@class="pn-next"]').click()
            next_page = self.driver.find_element_by_xpath('//a[@class="pn-next"]').is_enabled()


if __name__ == '__main__':
    d = demo()
    d.get_data()
