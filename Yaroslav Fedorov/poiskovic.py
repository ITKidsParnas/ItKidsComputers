from icrawler.builtin import GoogleImageCrawler
google_crawler = GoogleImageCrawler(storage={'root-dir':'C:\Users\ITK-2\Desktop\Files\Yaroslav Fedorov'})
google_crawler.crawl(keyword='cat', max_num=100)
