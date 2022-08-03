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
        user_agent='RDT Terminator Script'
    )

def list_comments(reddit, user):
    for comment in reddit.redditor(user).comments.top():
        print(comment.body)

def delete_comments(reddit, user):
    for comment in reddit.redditor(user).comments.top():
        comment.delete()

def delete_submissions(reddit, user):
    for submission in reddit.redditor(user).submissions.top():
        submission.delete()


def app():
    reddit = get_reddit_client()
    delete_submissions(reddit, 'lemtale')


if __name__ == '__main__':
    app()