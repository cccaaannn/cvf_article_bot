## CVF article finder
[CVF site](http://openaccess.thecvf.com/menu.py)


**usage**
___

```python
from cvf_article_bot import cvf_article_bot

# match word
keywords = ["detection", "face]
# match only if ["face", "detection"] or ["cnn", "vgg"] are exits or "detection" exits by itself
keywords = [["face", "detection"], ["cnn", "vgg"], "detection"]

cvf_bot = cvf_article_bot()
cvf_bot.get_articles(keywords, write_to_file=True, download=True)
```