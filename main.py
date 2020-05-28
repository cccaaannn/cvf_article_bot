from cvf_article_bot import cvf_article_bot

keywords = [["food", "fusion"], ["food", "context"], ["food", "ingredient"], ["food", "recipe"]]

ab = cvf_article_bot()
ab.get_articles(keywords, write_to_file=True, download=True)