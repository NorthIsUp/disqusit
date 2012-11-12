def submit_link(request):
    pass


def vote_link(request, value):
    pass


def upvote_link(request):
    return vote_link(request, 1)


def downvote_link(request):
    return vote_link(request, -1)


def friend_user(request):
    pass


def unfriend_user(request):
    pass
