Exports list of all your starred Github repos to a json file.
Also can optionally unstar all backed up repositories.


## install:

```
pip install gh_stars_export
```

## usage

```
$ gh_starts_export.py -o gh_stars.json --token x35b2rb37x6rbf328xnrr8rxnf23r83f
```

or 
```
$ export GITHUB_TOKEN=x35b2rb37x6rbf328xnrr8rxnf23r83f

$ gh_starts_export.py -o gh_stars.json
```

optionally, passing `-u/--unstar` also unstars the backed up starred repos.

```
$ export GITHUB_TOKEN=x35b2rb37x6rbf328xnrr8rxnf23r83f

$ gh_starts_export.py -o gh_stars.json --unstar

unstarring namhyung/uftrace
unstarring cybertec-postgresql/pgwatch2
unstarring nicolargo/glances
unstarring groveco/django-sql-explorer
unstarring ultrabug/py3status
unstarring apple/foundationdb
unstarring souvikmaity/somersault
unstarring git-tips/tips
```

## FAQ: 

1. Where to get the github token from?
Ans. [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
