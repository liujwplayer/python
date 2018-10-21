 # -*- coding: utf-8 -*-
import re
from urllib import request
class Book:
    pass

class Books():

    def getHtmls(self, url):
        http = request.urlopen(url)
        #访问读取
        htmls = http.read()
        #用utf-8转译成html文本
        htmls = str(htmls,encoding='utf-8')
        
        return htmls

    def getRegHtml(self, regx, htmls):

        html = re.findall(regx, htmls)
        return html

    def go(self):
        # 取得全部书本信息
        bookUrl = 'http://books-d.parkone.cn/'
        bookReg = r'<div class="cover">([\s\S]*?)</div>'
        root_html = self.getHtmls(bookUrl)
        root_html = self.getRegHtml(bookReg, root_html)
        # 书本信息实体
        books = []
        index = 0
        for html in root_html:
            index = index + 1
            book = Book()
            book.index = index
            try:
                content = html
                # 取得书名
                bookName = re.search(r'alt="([\s\S]*?)"', content)
                book.name = bookName.group(1)
                # # 取得下转详情页面url
                xzurl = re.search(r'href="([\s\S]*?)"', content)
                # 访问详情页面
                book.info_url = xzurl.group(1)
                # 取得书本简介、出版社
                infoUrl = bookUrl + xzurl.group(1)
                print("正在处理书本: " +infoUrl)
                bookInfoHtml = self.getHtmls(infoUrl)
                # 出版社
                publisher = re.search(r'<div class="publishers">([\s\S]*?)<span>([\s\S]*?)</span>([\s\S]*?)</div>', bookInfoHtml)
                book.publisher = publisher.group(2)
                # 简介
                description = re.search(r'<p class="description">([\s\S]*?)</p>', bookInfoHtml)
                book.description = description.group(1)
            except Exception as e:
                print(e)
            books.append(book)
        print("开始输出书本：")
        for tmp in books:
            print(tmp.index)
            try:
                if hasattr(tmp, 'name'):
                    print(tmp.name)
                else:
                    print("has no name")

                if hasattr(tmp, 'info_url'):
                    print(tmp.info_url)
                else:
                    print("has no info_url")

                if hasattr(tmp, 'publisher'):
                    print(tmp.publisher)
                else:
                    print("has no publisher")

                if hasattr(tmp, 'description'):
                    print(tmp.description)
                else:
                    print("has no description")
            except AttributeError as e:
                pass
            print("")

books = Books()
books.go()