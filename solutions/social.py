
tweets = [
    {
        "id": 100200297,
        "full_text": "Look at this delicious sandwich!",
        "img_url": "https://sandwhoa.com/sandwich.png",
        "user": {"screen_name": "sandwhoa", "followers": 5000},
        "likes_count": 150
    },
    {
        "id": 100200298,
        "full_text": "I love sandwiches",
        "img_url": None,
        "user": {"screen_name": "person1", "followers": 100},
        "likes_count": 5
    },
    {
        "id": 100200299,
        "full_text": "@sandwhoa yumm...",
        "img_url": None,
        "user": {"screen_name": "person2", "followers": 200},
        "likes_count": 10
    },
    {
        "id": 100200300,
        "full_text": "@sandwhoa that sandwich looks amazing!!",
        "img_url": None,
        "user": {"screen_name": "person3", "followers": 300},
        "likes_count": 35
    },
    {
        "id": 100200301,
        "full_text": "I ate a great sandwich today",
        "img_url": None,
        "user": {"screen_name": "person4", "followers": 400},
        "likes_count": 50
    }
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING SOCIAL MEDIA DATA...")
    print("------------------")
    print(tweets)

    # breakpoint()

    #
    # QUESTION A
    #
    # "Print" the screen name of the user who authored the first tweet (i.e. "sandwhoa"):

print("Question A:")
print(tweets[0]["user"]["screen_name"])
    #
    # QUESTION B
    #
    # Of all the tweets which include the phrase "@sandwhoa" in their full text,
    # ... "print" the screen name of the user who authored that tweet,
    # ... each on a separate line (i.e. "person2", then "person3"):

for tweet in tweets: 
    if "@sandwhoa" in tweet["ull_text"]:
        print(tweet["user"]["screen_name"])




    #
    # QUESTION C
    #
    # Of all the tweets which include the phrase "@sandwhoa" in their full text,
    # ... determine which tweet has the greatest number of likes,
    # ... and then "print" the screen name of the user who authored that tweet (i.e. "person3").
    # ... FYI: Assume the tweet order can change at any time
    # ... and has no relationship with the number of likes.



##class one 
#
## checking to see if the Git utility is installed
#git --version
## cloning a repo from the command-line:
#cd ~/Desktop/
#git clone git@github.com:s2t2/exam-solutions-starter-py.git # OR YOUR OWN REMOTE ADDRESS
#cd exam-solutions-starter-py/
#code .
#
## running python applications from the "base" anaconda env:
#python solutions/social.py
#
## committing on the "master" branch / default work space:
#git branch # make sure you're on the master branch
## make some changes via text editor
#git status # which files have changed?
#git diff # how have the files changed?
#git add . # prepare all the files to be committed
#git commit -m "Example commit" # save / commit a new version locally
## after one or more local commits, push to GitHub:
#git remote -v # checking to see which remote assiciations, for example "origin" points to repo on GitHub
#git push origin master # upload / push code to your GitHub repo's master branch
#
## branch operations / committing in a different working space:
#git checkout -b tweets # create a new branch / working space called "tweets" and activate it
#git branch # check that the tweets branch is active
## repeat the local process to change files and make a commit, then...
#git push origin tweets # to push to the "tweets" branch on GitHub
## then visit your repo on GitHub and open up a new "Pull Request" for the specified branch, where you can review 