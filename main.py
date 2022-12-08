from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
class Crawling:
    def __init__(self):
        self.urlLink = 'https://www.instagram.com'
        self.driver = webdriver.Chrome(executable_path=f'chromedriver\chromedriver.exe')
    def login(self):
        self.driver.get(self.urlLink)
        time.sleep(1)
        path = f"my_cookie1.pkl"
        cookies = pickle.load(open(path, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(5)
        return self.driver
    def crawl_gen(self):
        logging.basicConfig(
        format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
        logger = logging.getLogger()
        wait = WebDriverWait(self.driver, 10)
        wait_between_posts = random.randint(7, 16)
        tag = -1
        likes = 0
        comments = 0
        wait_to_comment = random.randint(5, 10)
        comments_list = ['Love this!, please follow me', 'Nice shot :), please follow me', 'Amazing~, please follow me', 'Looks great! :), please follow me', 'Beautiful, please follow me']

        hashtag_list = ['likeback ', 'likeforlikes','follow']
        for hash_tag in hashtag_list :
            # self.driver.refresh()
            print(hash_tag)
            self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag_list[tag]}/')
            thumbnail = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]')))
            time.sleep(2)
            thumbnail.click()
            try: 
                print("Start")
                for i in range(1, 100) :
                        time.sleep(2)
                        a= wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='_aamw']/button")))
                        a.click()
                        likes +=1
                        comn_prob = random.randint(1,2)
                        print("{}_{}: {}".format(hash_tag, i, comn_prob))
                        if comn_prob == 1: 
                            try:
                                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea'))).click()
                                comment_box = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')))
                                time.sleep(wait_to_comment)
                                rand_comment_index = random.randint(0, len(comments_list))
                                comment_box.send_keys(comments_list[rand_comment_index])
                                comment_box.send_keys(Keys.ENTER)
                                logger.info(
                                     f"Commented '{comments_list[rand_comment_index]}'")
                                comments += 1
                            except:
                               pass
                        time.sleep(random.randint(7, 16))
                        self.driver.find_element(By.XPATH, "//div[@class=' _aaqg _aaqh']/button").click()
                        logger.info('Getting next post')
                        time.sleep(random.randint(7, 16))
                tag += 1
                time.sleep(5*60)
            except Exception as e:
                print(e)
                pass
crawl = Crawling()
crawl.login()
while True:
    crawl.crawl_gen()

