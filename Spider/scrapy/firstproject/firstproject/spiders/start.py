from scrapy import cmdline

# 下面两种都可以
cmdline.execute(['scrapy', 'crawl', 'qiushi'])
# cmdline.execute('scrapy crwal qiushi'.split(' '))