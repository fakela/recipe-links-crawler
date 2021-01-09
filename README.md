# related-dishes

This is a very simple crawler that scrapes wikipedia for dishes that are similar to other dishes, and links them in a Neo4j graph database. 

![sample output](./output.png)

To run this script, run:

```
pip3 install requirements.txt
python3 crawler.py
```

## details

The script  uses the wikipedia API to scrape the 'See Also' links on a page for a particular dish. It is seeded with a list of starting dishes (see the `to_visit` list at the top of the file) that try and get a wide spread across a network. On each of those pages, it finds links under 'see also', after testing to see whether each of those links is in a wikipedia category that would imply that it is a dish. Once a page has been visited, it's added to a text file (`novisit.txt`) to prevent the crawler from visiting places it's already been. This way the scraper can be run multiple times with different starting seeds, without duplicating paths.

![The 'see also' section for Lasagne](./see-also.png)

The crawler ignores pages with 'List' in the title (as they are too general), and only counts pages that have certain categories (currently just `dish`, and `bread`, though this should be expanded), in addition to ignoring pages it has already visited. If a page passes each of these tests, its URL is appended to the `to_visit` list, and the crawler will go there next. It stops when the crawler runs out of urls on `to_visit`.

## next steps

This crawler is somewhat basic and buggy, and has a few obvious flaws. A key one is the structure of the `see also` section, as it is used differently on different pages, with the added `related` section (or custom-named sections like `related recipes`) sometimes being used. There's also many pages where `see also` contains names of dishes rather than links to them, and a way to parse them would be nice.
