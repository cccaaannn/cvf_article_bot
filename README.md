# CVF article finder

![](https://img.shields.io/github/repo-size/cccaaannn/cvf_article_bot?style=flat-square) [![GitHub license](https://img.shields.io/github/license/cccaaannn/cvf_article_bot?style=flat-square)](https://github.com/cccaaannn/cvf_article_bot/blob/master/LICENSE)

[CVF site](http://openaccess.thecvf.com/menu.py)


### Match individual words
```python
from cvf_article_bot import cvf_article_bot

keywords = ["detection", "face"]
cvf_bot = cvf_article_bot()
cvf_bot.get_articles(keywords)
```

### Match a group of words 
```python
from cvf_article_bot import cvf_article_bot

keywords = [["face", "detection"], ["cnn", "vgg"], "detection"]
cvf_bot = cvf_article_bot()
cvf_bot.get_articles(keywords, write_to_file=True, download=True)
```

### Match whole word only (this also can be a group of words)
```python
from cvf_article_bot import cvf_article_bot

keywords = [["face", "detection"], "detection"]
cvf_bot = cvf_article_bot()
cvf_bot.get_articles(keywords, match_whole_word_only=True)
```

### Download articles and save links of articles to text file 
```python
from cvf_article_bot import cvf_article_bot

keywords = [["face", "detection"], ["cnn", "vgg"], "detection"]

# You can specify download path and text file names on object
cvf_bot = cvf_article_bot(main_save_folder_path = "articles", articles_text_name = "articles.txt")
cvf_bot.get_articles(keywords, match_whole_word_only=True, write_to_file=True, download=True)
```