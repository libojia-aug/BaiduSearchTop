import spider.baiduTop as s

def main():
    myspider = s.BaiduTop()
    myspider.getTopics()
    print(myspider.topics_list)
    print(myspider.values_list)
    print(myspider.urls_list)

if __name__ == '__main__':
    main()