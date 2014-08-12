import praw
import sys

r = praw.Reddit("sub_search.py: search a subreddit for threads that"
                                "mention any one of the words given by"
                                "the user")

def get_subname(s):
    if s[:4] != "sub=":
        print "error: invalid syntax"
        sys.exit()

    return s[4:]

def parse_words(s):
    words = []
    i = 0
    while s[i:i+7] != "words=[":
        i += 1
    if i == len(s):
        print "error: invalid syntax"
        sys.exit()

    start = i+7
    end   = start
    while s[end] != ']':
        end += 1

    words = s[start:end].split(',')
    for i in range(len(words)):
        words[i] = words[i].strip()
   
    return words

def sub_search(words, name, n):
    i = 1
    seen = []

    subreddit = r.get_subreddit(name)
    for submission in subreddit.get_hot(limit=25):
        title = submission.title.lower().split()
        text  = submission.selftext.lower().split()

        has_word = any(string in text or string in title for string in words)

        if submission.id not in seen and has_word:
            print "%d: %s" % (i, submission.short_link)
            i += 1
            if i > n:
                return 0
            seen.append(submission.id)

def main():
    sub_name = get_subname(sys.argv[1])
    words    = parse_words(" ".join(sys.argv))
    n        = int(sys.argv[len(sys.argv)-1])
    sub_search(words, sub_name, n) 

main()
