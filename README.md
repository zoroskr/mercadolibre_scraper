# NYTimes Scraper
Welcome to the README for my project. This documentation is primarily available in English.
If you prefer to read this documentation in Spanish, you can access the Spanish version by clicking [here](README-es.md).
## Introduction

This Python library, NYTimes Scraper, is designed to scrape and interact with data from The New York Times website. It provides classes and functions to extract various types of information, including articles, sections, types, renditions, and more.

# Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Classes](#classes)
- [Usage](#usage)

## Installation

Install the NYTimes Scraper library using `pip`:

```bash
pip install nyt-scraper
```

## Features
- ## Search Functionality
  - Conduct searches for any entry using a keyword.
  - Sort information by "newest," "oldest," or "best."
  - Filter results by type or section.

- ## Versatility
  - Access information for various content types, including articles, videos, audio, slideshows, recipes, interactives, and paid posts, using only the URL.
  - Obtain profiles of persons by providing their URL.

- ## Media Download
  - Download videos and images in different qualities.

## Classes

### `Scraper`

The `Scraper` class is the main interface for interacting with The New York Times website. It provides methods to perform searches, retrieve articles, download media, and more.


- `search(keyword, sort="newest", type_="", section="")`
    - Performs a search in The New York Times database.
    - `keyword` (str): The search term.
    - `sort` (str, optional): Sorting order ("newest", "oldest", "best").
    - `type_` (str, optional): Type of content to filter. ('article', 'recipe', 'video', 'etc')
    - `section` (str, optional): Section to filter. ('food', 'arts', 'travel', 'business', 'etc')

- `search_person(url)`
    - Searches for information about a person based on their URL.
    - `url` (str): URL of the person.

- `search_suggest(query)`
    - Gets search suggestions for a given query.
    - `query` (str): The search query.

- `get_article(url)`
    - Retrieves an article based on its URL.
    - `url` (str): URL of the article.

- `get_video(url)`
    - Retrieves video information from the given URL.
    - `url` (str): URL of the video.

- `get_audio(url)`
    - Retrieves audio information from the given URL.
    - `url` (str): URL of the audio.

- `get_slideshow(url)`
    - Retrieves slideshow information from the given URL.
    - `url` (str): URL of the slideshow.

- `get_recipe(url)`
    - Retrieves recipe information from the given URL.
    - `url` (str): URL of the recipe.

- `get_interactive(url)`
    - Retrieves interactive content information from the given URL.
    - `url` (str): URL of the interactive content.

- `get_paidpost(url)`
    - Retrieves paidpost information from the given URL.
    - `url` (str): URL of the paidpost.

## Usage
#### `Initializate`
```python
import nyt_scraper
scraper = nyt_scraper.Scraper()
```
#### `Search`
You can perform searches in The New York Times database using the search function.
##### Methods
- `next(self)`: Retrieves the next 10 entries on each call and returns a list of entries representing the new results. It also updates the list of `Search.entries`. Please note that a maximum of 1000 entries can be obtained from a search
##### Example

```python
results = scraper.search(keyword="restaurant", sort="oldest", type_="article", section="food")
print(results)
#output: Search(entries, sections, types, totalEntries)
print(results.totalEntries)
#output: 14386
print(results.entries)
#output: Entries(10 entries)
first_entry_result = results.entries[0]
print(first_entry_result)
#output: Article(type, url, title, summary, authors, language, published, modified, section, subsection, alteration)

for entry in results.entries:
    print(entry.type)
    print(entry.title)

print("Length entries search")
print(len(results))  # 10
results.next()
print(len(results))  # 20
results.next()
print(len(results))  # 30
```

#### `Video`
 Retrieve a Video object for a specific URL

##### Example
 ```python
video = scraper.get_video(url="https://www.nytimes.com/video/world/asia/100000008963375/china-barbecue-restaurant-explosion.html")

print(video)
# output: Video(type, url, title, summary, authors, language, section, subsection, published, modified, duration, transcript, renditions, keyword, tags)

print(video.title)  # output: Explosion Kills Dozens at Barbecue Restaurant in China
print(video.duration)  # output: 29429

# Download the best quality of video
video.download(path="local_path.mp4")

# To select a different quality or file format, you can use video.renditions
```

#### `Renditions`
The Renditions class represents a collection of different renditions of a video. These renditions may vary in terms of quality, size, and video file format.
This is an iterable. Helpful To access specific details about each rendition, you can loop through the "renditions" and print information such as "width", "height", and "type" for each rendition. This allows you to inspect the features of each available version before selecting one to download.

##### Methods
- `download(self, path)`: Downloads the best available video quality among the renditions and saves it to the location specified by path. Returns True if the download was successful.
  - `path (str)`: the location or directory where a file should be saved or retrieved

- `find(self, width=None, height=None, type_=None)`: Searches for a specific rendition within the collection of renditions. You can specify the following search criteria:

  - `width (int, optional)`: Width of the rendition in pixels.
  - `height (int, optional)`: Height of the rendition in pixels.
  - `type_ (str, optional)`: Video file type (e.g., "mp4", "mov").
It returns the first rendition that matches the search criteria or None if no match is found.

##### Example

 ```python
video = scraper.get_video(url="https://www.nytimes.com/video/world/asia/100000008963375/china-barbecue-restaurant-explosion.html")

# Access available renditions
renditions = video.renditions

# Download the best video quality (default: mp4)
renditions.download(path="local_path.mp4")

for rendition in renditions:
    print('----------------------------')
    print('width: ', rendition.width)
    print('height: ', rendition.height)
    print('type: ', rendition.type)

rendition_480 = renditions.find(width=480, height=480, type_="webm")
print(rendition_480) # output: Rendition(url, width, height, type, bitrate, aspectRatio)
rendition_480.download("video_480.webm")
```

#### `Images`
The `Images` class represents a collection of images. It allows you to work with multiple images efficiently, providing methods to find images based on criteria such as name and type (typename).

##### Methods
- `download(self, path)`: Downloads the best resolution image and saves it to the location specified by path. Returns True if the download was successful.
  - `path (str)`: the location or directory where a file should be saved or retrieved

- `find(self, name=None, typename=None)`: This method searches for a specific image within the collection of images based on the given criteria:

  - `name` (str, optional).
  - `typename` (str, optional).

  It returns the first image that matches the specified criteria or None if no match is found.

##### Example

```python
# Access available images
person = scraper.get_person(url="https://www.nytimes.com/by/axel-boada")
images = person.photos

# Download the best image resolution
images.download(path="best_resolution.jpg")

for image in images:
    print('----------------------------')
    print('name: ', image.name)
    print('typename: ', image.typename)
    print('size: ', image.size)

# Find an specific image by name and type
image = images.find(name="articleLarge", typename="ImageRendition")
print(image)  # Output: Image(url, name, typename, width, height, size)
image.download("articleLarge.jpg") # download specific image
```

# All the plural classes function in the same way: they can be iterated to obtain the singular classes and their respective attributes.
### - Sections -> Section
### - Subsections -> Sections
### - Types -> Type
### - Images -> Image
### - Persons -> Person

MIT License
Copyright (c) 2023 Diego-Arrechea