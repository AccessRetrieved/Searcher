# Searcher
Powerful search tool.

## Search method
- Local(disks, filenames, filepaths, and inside readable files)
- Web(Baidu and Google)


## Integrate it into your project
1. Download searcher.py and drag into your working directory.
2. impor searcher

examples:

```
search_local = Searcher().search('String')
search_web = Searcher().WebSearcher('String')
```

## WARNING
Don't send requests too fast as you might get blocked by google and baidu. Default duration is 600 ms.
