# YouTube Placements API Blocklist


## Installation
### Python
Make sure you have Python 3.6+ installed, we used [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to create a Python 3.8 virtual environment.

Then install the Python packages:<br>
`pip install -r requirements.txt`

## Notebooks
Notebooks for data collection, preprocessing and analysis

### 0-data-collection.ipynb
How we discovered and interacted with the "PlacementSuggestionService" API from "ads.google.com". Use this notebook mostly for reference, the code will not work with the expired parameters present.

### 1-data-preprocessing.ipynb
Parsing the API responses and fetching the suggested videos and channels for each term we sent to the undocumented API.

### 2-data-analysis-hate.ipynb
The bulk of stats, tables, and visualization for our hate methodology.

### 3-suggestion-analysis.ipynb
Looks at videos and channels suggested by the API for hate terms. We cross reference these suggestions with channels the ADL identified as "extremist" or "alternative".

### 4-data-analysis-social-justice.ipynb
The bulk of stats, tables, and visualization for our social justice methodology.

### terms.py
This contains lists of terms used in this series. Please take a look at the "Data" section below.

## Data
This directory is where intermediaries and outputs are saved.
```
data
├── input
│   ├── adl_extremist_alternative_channels_overlap.csv
│   ├── placements_api
│   │   ├── adhoc
│   │   ├── blocked
│   │   ├── blocked_basewords
│   │   ├── hate
│   │   ├── noise
│   │   ├── policy
│   │   └── social_justice
│   ├── placements_api_deep3
│   │   ├── we wuz kangz.json
│   │   ├── white ethnostate.json
│   │   └── whitegenocide.json
│   └── video_metadata
│       ├── deep_catalog_wwk_wg_we.csv
│       └── topline_hate_videos.csv
├── media
│   └── google_ad_portal_youtube_ad_placements.png
└── output
    ├── adl_extremist_alternative_channel_overlap.csv
    ├── placements_api_keyword_status
    │   ├── adhoc.csv
    │   ├── all_keywords.xlsx
    │   ├── basewords.csv
    │   ├── hate.csv
    │   ├── policy.csv
    │   └── social_justice.csv
    ├── placements_api_suggestions
    │   ├── channels_for_hate_terms.csv
    │   ├── channels_for_social_justice_terms.csv
    │   ├── videos_for_hate_terms.csv
    │   └── videos_for_social_justice_terms.csv
    └── video_metadata
        └── topline_videos_for_hate_terms.csv

```
`data/input/adl_extremist_alternative_channels_overlap.csv` - contains channel names and IDs that the ADL identified as "extremist" or "alternative." This is a subset of the list that overlaps with channels we found. For the full list contact the ADL.
`data/input/placements_api` -  This contains responses from the YouTube "PlacementSuggestionService" API. Each sub-directory is used to organize by the keyword list used.<br>
`data/input/video_metadata` - contains video metadata for suggested videos from the YouTube Data API (v3). Collected with a an unoffical Python client ([YouTube Data API](https://youtube-data-api.readthedocs.io/en/latest/))


`data/output/adl_extremist_alternative_channel_overlap.csv` - The count of "extremist" and "alternative" videos and channels from the topine suggestions for hate terms we sent through the "PlacementSuggestionService" API. We've included the channels that were surfaced in a " | "-delimited column called `channels`.

`data/output/placements_api_keyword_status` - Contains the status of keywords from `notebooks/terms.py` after being sent through the "PlacementSuggestionService" API. Briefly, this includes `hate` terms sourced from the SPLC, RationalWiki, and Muslim Advocates. `noise` terms which are just random alphanumeric characters. `blocked_basewords`, which were multi-word terms that were blocked, and re-submitted to the API word-by-word. `social_justice` terms sourced from Color of Change, Media Justice, Mijente, and Muslim Advocates.
<br>

`data/output/placements_api_suggestions` - The suggested YouTube videos and channels for each search term.<br>
`data/output/video_metadata` - Contains video metadata for videos suggested from Hate keywords. Data collected from the YouTube Data API V3.

`data/output/crossref` - The overlap of channels found in our investigation and those the ADL categorized as "extremist" or "alternative"