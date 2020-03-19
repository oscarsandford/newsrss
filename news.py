#!/usr/bin/env python3

import sys
import feedparser
news_url = "http://news.google.com.br/news?pz=1&cf=all&ned=us&hl=en&output=rss"

def print_summary(entries, cnt):
    print("Summary: ")
    print("Displaying " + str(cnt) + " entries of " + str(len(entries)) + " retrieved.")

def get_entries(keywords, lmtr):

    feed = feedparser.parse(news_url)
    entries = []

    # if we have keywords to look for
    if (len(keywords) > 0):
        for post in feed.entries:
            # for each keyword, see if in the article title; if so, add
            for word in keywords:
                if (post.title.lower().split().count(word) > 0):
                    entries.append(post)
    # if not, just add all entries up to the limiter
    else:
        for post in feed.entries:
            entries.append(post)


    find_news(entries, lmtr)

def find_news(entry_list, limiter):
    # might have instance of duplicates
    # would be nice to remove, but list(set(arr))
    # doesn't work for some reason
    count = 0
    for post in entry_list:
        if (count < limiter):
            print("Post: " + post.title)
            print("Published: " + post.published)
            #print("Link: " + post.link + "\n")
            print("\n", "-"*40, "\n")
            count += 1

    print_summary(entry_list, count)

def main():
    keywords = []
    limit = 9999
    arg_len = len(sys.argv)

    # if no args given, display verbose entries
    if (arg_len == 1):
        get_entries(keywords, limit)
    else:
        try:
            # try if first arg is limiter
            try:
                if (int(sys.argv[1])):
                    limit = int(sys.argv[1])
                # see if we have more keyword args
                if (arg_len >= 3):
                    # add args to keywords list
                    for i in range(2, arg_len):
                        keywords.append(sys.argv[i])

            # else there's no limiter
            except (ValueError):
                # add args to keywords list
                for i in range(1, arg_len):
                    keywords.append(sys.argv[i])

        # catch any unforeseen wacko stuff
        except:
            print("Usage:   news.py <limiter (int)> <keyword(s) (str)>" )
            sys.exit(0)

        get_entries(keywords, limit)
    # end if/else


if __name__ == '__main__':
    main()
