#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys

from retrying import retry
from github import Github


logger = logging.getLogger(__name__)


DESCRIPTION = '''
This script exports your github stars to a json file,
and optionally unstars all starred repositories.
'''


def write_to_file(filepath, data):
    if filepath:
        try:
            with open(filepath) as fp:
                old_data = json.loads(fp.read())
        except FileNotFoundError:
            old_data = {}
        
        data.append(old_data)
        with open(filepath, 'w') as fp:
            fp.write(json.dumps(data, indent=4))
    else:
        sys.stdout.write(json.dumps(data, indent=4))


def export_as_json(stars, filepath):
    data = [
        {
            'description': repo.description,
            'name': repo.full_name,
            'lang': repo.language,
            'link': 'https://github.com/{}'.format(repo.full_name),
            'size': repo.size,
            'stars': repo.stargazers_count,
        } for repo in stars
    ]

    write_to_file(filepath, data)


@retry(stop_max_attempt_number=3, wait_fixed=500)
def unstar(user, repo):
    user.remove_from_starred(repo)


def export_stars(args):
    gh = Github(args.token or os.getenv('GITHUB_TOKEN'))
    user = gh.get_user()
    stars = list(user.get_starred())
    export_as_json(stars, args.outfile)

    if args.unstar:
        for repo in stars:
            if args.outfile:
                logger.warn('unstarring {}'.format(repo.full_name))
            unstar(user, repo)


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-u', '--unstar', action='store_true', required=False, help='unstar all exported repos')
    parser.add_argument('-t', '--token', required=False, help='Github API token')
    parser.add_argument('-o', '--outfile', required=False)
    args = parser.parse_args()
    export_stars(args)


if __name__ == '__main__':
    main()
