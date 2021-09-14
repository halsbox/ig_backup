#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from instaloader.__main__ import main
if __name__ == '__main__':
    USER = sys.argv[-1]
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    _args = ['-s', '--highlights', '--tagged', '--igtv', '-G', '-C', '-l', USER, USER]
    old_sys_argv = sys.argv
    sys.argv = [old_sys_argv[0]] + _args
    result=main()
    import instaloader
    import datetime
    L = instaloader.Instaloader()
    PROFILE = USER
    L.load_session_from_file(USER)
    profile = instaloader.Profile.from_username(L.context, PROFILE)
    ts_now = str(int(datetime.datetime.now().timestamp()))
    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())
    print("Storing followers into file.")
    with open(PROFILE + "/followers_" + ts_now + ".txt", 'w') as f:
        for follower in followers:
            print(follower.username, file=f)
    print("Fetching followees of profile {}.".format(profile.username))
    followees = set(profile.get_followees())
    print("Storing followees into file.")
    with open(PROFILE + "/followees_" + ts_now + ".txt", 'w') as f:
        for followee in followees:
            print(followee.username, file=f)
    sys.exit(result)
