# import kivy classes
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
kivy.require("1.11.1")

# these will help with getting the news rss data from google
import feedparser
news_url = "http://news.google.com.br/news?pz=1&cf=all&ned=us&hl=en&output=rss"


class FeedPage(GridLayout):
    # want to have just a page pop up instantly with a scroll on various
    # news articles
    def __init__(self, **kwargs):
        super(FeedPage, self).__init__(**kwargs)

        self.cols = 1
        self.rows = 3
        self.spacing = 5

        keyword = "coronavirus"

        # get news articles based on search keyword, or all
        feed = feedparser.parse(news_url)
        news_articles = []

        if keyword != "":
            for entry in feed.entries:
                if keyword in entry.title:
                    news_articles.append(entry)
        else:
            news_articles = feed.entries


        # widgets:

        self.add_widget(Label(text="Damage Report News", font_size=20))

        # create an inset for the news articles
        self.newsfeed = GridLayout()
        self.newsfeed.rows = len(news_articles)
        self.add_widget(self.newsfeed)

        for article in news_articles:
            self.newsfeed.add_widget(Label(text=article.title, font_size=14, halign="left"))

        self.exit_button = Button(text="Exit")
        self.exit_button.bind(on_press=self.exitpress)
        self.add_widget(self.exit_button)

    def exitpress(self, instance):
        exit(1);


class NewsApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.feed_page = FeedPage()
        screen = Screen(name="FeedPage")
        screen.add_widget(self.feed_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    NewsApp().run()
