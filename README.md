Exports list of all your starred Github repos to a json file.


## install:

```
pip3 install gh_stars_export
```

## usage

```
$ gh_stars_export -o gh_stars.json --token x35b2rb37x6rbf328xnrr8rxnf23r83f
```

or 
```
$ export GITHUB_TOKEN=x35b2rb37x6rbf328xnrr8rxnf23r83f

$ gh_stars_export -o gh_stars.json
```

## FAQ: 

1. Where to get the github token from?
Ans. [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)
make sure you give the gist permission if you want to use the backup to gist feature.
