  
from bs4 import BeautifulSoup
import requests
import shutil
import json
import time
import os
import re

class cvf_article_bot():
    def __init__(self, main_save_folder_path = "articles", articles_text_name = "articles.txt"):
        self.cvf_conferences = self.__read_json_file()
        
        self.main_save_folder_name = main_save_folder_path
        self.articles_text_name = os.path.join(self.main_save_folder_name, articles_text_name)
        self.__create_folder(self.main_save_folder_name)

        self.base_url = "http://openaccess.thecvf.com/"
        self.soup = BeautifulSoup(features="html.parser")


    def __get_url(self, url):
        raw_site = requests.get(url, verify=False).text
        self.soup = BeautifulSoup(raw_site, features="html.parser")

    def __download_file(self, url, download_path):
        file_name = os.path.join(download_path, url.split('/')[-1])
        try:
            with requests.get(url, stream=True) as r:
                with open(file_name, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
        except Exception as e:
            print(e, "download error")

    def __create_folder(self, folder_name):
        if(not os.path.exists(folder_name)):
            os.makedirs(folder_name)

    def __write_to_file(self, to_write, write_mode="a"):
        try:
            with open(self.articles_text_name, write_mode, encoding='utf-8') as file:
                    file.write(to_write)
        except (OSError, IOError) as e:
            print(e)

    def __read_json_file(self, cfg_path="cvf_links.cfg"):
        try:
            with open(cfg_path,"r") as file:
                cfg_file = json.load(file)
            return cfg_file
        except:
            raise ValueError("cfg file is broken")

    def __match_function(self, match_whole_word_only, pattern, search_text):
        # convert to lower
        pattern = pattern.lower()
        search_text = search_text.lower()

        is_match = False
        # use regex for match_whole_word_only
        if(match_whole_word_only):
            compiled_pattern = re.compile("\\b{0}\\b".format(pattern))
            is_match = compiled_pattern.search(search_text)
        # use in for rest
        else:
            is_match = (pattern in search_text)

        if(is_match):
            return True
        else:
            return False



    def get_articles(self, keywords, match_whole_word_only=False, write_to_file=False, download=False):   
        # time execution
        start_time = time.time()
        print("\nThis generally takes 2,5 to 3 second per link without downloads (links are in the cfg file)\n\n")

        matched_article_counter = 0
        for cvf_conference_name in self.cvf_conferences:
            new_file_path = os.path.join(self.main_save_folder_name, cvf_conference_name)

            # get url and articles
            self.__get_url(self.cvf_conferences.get(cvf_conference_name))
            articles = self.soup.findAll("dt", {"class": "ptitle"})
            
            for article in articles:
                for keyword in keywords:
                    is_match = False

                    # match if a list of words given
                    if(isinstance(keyword, list)):

                        # this look so complicated so I made the other one
                        # if(all(map(lambda keywords_list: True if self.__match_function(match_whole_word_only, keywords_list, article.text) else False, keyword))):
                            # is_match = True

                        for keyword_list_element in keyword:
                            if(not self.__match_function(match_whole_word_only, keyword_list_element, article.text)):
                                break
                        else:
                            is_match = True

                    # match if only single word
                    else:
                        if(self.__match_function(match_whole_word_only, keyword, article.text)):
                            is_match = True


                    if(is_match):
                        matched_article_name = article.text
                        matched_article_link = self.base_url + article.find_next_sibling("dd").find_next_sibling("dd").find("a")["href"]
                        matched_article_counter += 1
                        
                        contet_text ="{}- name: {}\nurl: {}\ncvf_conference_name: {}\nmatched_words: {}\n\n".format(matched_article_counter, matched_article_name, matched_article_link, cvf_conference_name, keyword)
                        print(contet_text)

                        if(download):
                            # create file if new article exists
                            self.__create_folder(new_file_path)
                            self.__download_file(matched_article_link, new_file_path)

                        if(write_to_file):
                            self.__write_to_file(contet_text)

        print("--- {0} seconds ---".format(time.time() - start_time))


