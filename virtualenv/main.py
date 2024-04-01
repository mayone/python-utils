# -*- coding: utf-8 -*-

try:
    from github import Github
except Exception:
    print("venv test FAILED")
    exit(0)


def test():
    gh = Github(auth=None)
    user = gh.get_user()
    print("venv test SUCCESS")


if __name__ == "__main__":
    test()
