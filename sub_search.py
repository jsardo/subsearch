import praw
import sys

r = praw.Reddit("sub_search.py: search a subreddit for threads that
                                mention any one of the words given by
                                the user")

def get_subname(s):
    if s[:10] != "subreddit=":
        print "error: invalid syntax"
        sys.exit()

    return s[10:]

def parse_words(s):
    words = []
    if s[:7] != "words=[":
        print "error: invalid syntax"
        sys.exit()

    c = 7
    word = []
    while s[c] != ']':
        word.append(s[c])
        c += 1
        if s[c] == ',' or s[c] == ']':
            words.append("".join(word))
            word = []
            if (s[c] != ']'):
                c += 1
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
    if len(sys.argv) != 4:
        print "error: program requires three arguments:\n"
        print "       subreddit=<subreddit name> words=[<words to search for>] <search limit>"
        sys.exit()

    sub_name = get_subname(sys.argv[1])
    words    = parse_words(sys.argv[2])
    n        = sys.argv[3]
    sub_search(words, sub_name, n) 


main()
