from cvf_article_bot import cvf_article_bot

keywords = [["fusion", "context"]]

cvf_bot = cvf_article_bot()
cvf_bot.get_articles(keywords, match_whole_word_only=True)
# cvf_bot.get_articles(keywords, match_whole_word_only=True, write_to_file=True, download=True)