import argparse
import json
import logging
import os
import sys

from github import Github, InputFileContent


logger = logging.getLogger("log")


DESCRIPTION = """
This script exports your github stars to a json file.
"""


def export_as_json(user, filename):
    data = []
    repos = []

    for repo in user.get_starred():
        data.append(
            {
                "description": repo.description,
                "name": repo.full_name,
                "lang": repo.language,
                "link": "https://github.com/{}".format(repo.full_name),
                "size": repo.size,
                "stars": repo.stargazers_count,
            }
        )
        repos.append(repo)

    filepath = os.path.abspath(filename)

    with open(filepath, "w") as fp:
        fp.write(json.dumps(data, indent=4))

    logger.warn("written to file: {}".format(filepath))
    return repos


def backup_to_gist(user, filename):
    with open(os.path.abspath(filename)) as fp:
        content = fp.read()

    gist = user.create_gist(public=False, files={filename: InputFileContent(content)})
    logger.warn("backup link: {}".format(gist.html_url))


def export_stars(args):
    gh = Github(args.token or os.getenv("GITHUB_TOKEN"))
    user = gh.get_user()

    stars = export_as_json(user, args.outfile)

    if args.backup:
        backup_to_gist(user, args.outfile)


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "-b",
        "--backup",
        action="store_true",
        required=False,
        help="backup the exported repos json file to private gist",
    )
    parser.add_argument("-t", "--token", required=False, help="Github API token")
    parser.add_argument("-o", "--outfile", required=True)
    args = parser.parse_args()
    export_stars(args)


if __name__ == "__main__":
    main()
