subsearch
=========

Return all threads in a particular subreddit that contain any of the words provided by the user.

usage
=====

    python sub_search.py sub=<subreddit name> words=[<list of words>] <search limit>

example
=======

    python sub_search.py sub=python words=[django, flask, pypy, api, html, javascript] 50
    1: http://redd.it/25qqrp
    2: http://redd.it/25q0mx
    3: http://redd.it/25nztu

caveat
======

with the recent addition of comment parsing the script now takes a very long time to execute.
keep this in mind when searching a large subreddit with large comment threads.  

coming soon
===========

* choice to ignore case or not
* extend search to multiple subreddits
* search for a string containing multiple words
* choice to search the submission's title, body, and comments or a combination of the three.
