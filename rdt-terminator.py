from getpass import getpass
import praw


def get_reddit_client():
    client_id = getpass('Client_Id: ')
    client_secret = getpass('Client_Secret: ')
    username = input('Username: ')
    password = getpass('Password: ')

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        user_agent="RDT Terminator Script"
    )

def app():
    reddit = get_reddit_client()
    for submission in reddit.subreddit("all").hot(limit=25):
        print(submission.title)


if __name__ == '__main__':
    app()