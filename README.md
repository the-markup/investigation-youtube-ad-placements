# YouTube Ad Placements
This repository contains code and data to reproduce the findings featured in our stories, "[Google Has a Secret Blocklist that Hides YouTube Hate Videos from Advertisers—But It’s Full of Holes](https://themarkup.org/google-the-giant/2021/04/08/google-youtube-hate-videos-ad-keywords-blocklist-failures)," and "[Google Blocks Advertisers from Targeting Black Lives Matter YouTube Videos](https://themarkup.org/google-the-giant/2021/04/09/google-blocks-advertisers-from-targeting-black-lives-matter-youtube-videos)" from our series [Google the Giant](https://themarkup.org/series/google-the-giant).

Our methodology is described in "[How We Discovered Google’s Hate Blocklist for Ad Placements on YouTube](https://themarkup.org/google-the-giant/2021/04/08/how-we-discovered-googles-hate-blocklist-for-ad-placements-on-youtube)," and "[How We Discovered Google’s Social Justice Blocklist for YouTube Ad Placements](https://themarkup.org/google-the-giant/2021/04/09/how-we-discovered-googles-social-justice-blocklist-for-youtube-ad-placements)."

Data that we collected and analyzed are in the `data` folder.

Jupyter notebooks used for data collection, preprocessing and analysis are in the `notebooks` folder.

<img src="https://raw.githubusercontent.com/the-markup/investigation-youtube-ad-placements/master/data/reference/media/youtube_placements.png" width=700>
<i> Advertisers can use Google's ad portal to search for YouTube videos and channels related to keywords like: "hiking gear reviews" to advertise on.</i>
<br>
<br>
Warning: this repository contains many offensive terms and expletives.

## Installation
### Python
Make sure you have Python 3.6+ installed, we used [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to create a Python 3.8 virtual environment.

Then install the Python packages:<br>
`pip install -r requirements.txt`

## Notebooks
These notebooks are intended to be run sequentially, but they are not dependent on one another.

### 0-data-collection.ipynb
How we interacted with the "PlacementSuggestionService" API from "ads.google.com". We sent each term from `terms.py` through the API. Use this notebook for reference: it is not functional due to the expired or redacted parameters present.

### 1-data-preprocessing.ipynb
Parsing the API responses and fetching the suggested videos and channels for each term we sent to the API.

### 2-data-analysis-hate.ipynb
The bulk of stats and tables for our hate methodology.

### 3-suggestion-analysis.ipynb
Looks at videos and channels suggested by the API for `hate` terms. We cross reference these suggestions with channels identified as "extremist" or "alternative" by researchers from Dartmouth College, Northeastern University, and University of Exeter and provided to the Markup by the [ADL](https://www.adl.org/resources/reports/exposure-to-alternative-extremist-content-on-youtube), as well as a channels researchers at [EPFL and UFMG](https://dl.acm.org/doi/abs/10.1145/3351095.3372879) identified as "alt-right" or "alt-lite".

### 4-data-analysis-social-justice.ipynb
The bulk of stats and tables for our social justice methodology.

### 5-rerun-and-check-status.ipynb
After we shared our findings with Google, we re-run the analysis on data collected on March 31, 2021. Check what changed from the original data we collected on November 20, 2020.

### utils.py
Contains functions to parse and decipher the API responses.

### terms.py
This contains lists of terms used in the series. This includes `hate` terms sourced from the SPLC, RationalWiki.org, and Muslim Advocates. `social_justice` terms sourced from Color of Change, MediaJustice, Mijente, and Muslim Advocates. `adhoc` terms were submitted for comparison against terms in the other lists. `noise` contains randomly generated strings.

Refer to the "Data" section below for the API status of each of these terms.


## Data
This directory is where inputs, intermediaries and outputs are saved.
```
data
├─── reference
│   ├── placements_api_example_responses
│   │   ├── blocked.json
│   │   ├── empty.json
│   │   ├── full.json
│   │   └── partially_blocked.json
│   └── what_is_blocked.xlsx
├── input
│   ├── channel_lists
│   ├── hate_terms_background_info.csv
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
└── output
    ├── channel_overlap.csv
    ├── tables
    ├── placements_api_keyword_status
    │   ├── adhoc.csv
    │   ├── basewords.csv
    │   ├── hate.csv
    │   ├── policy.csv
    │   └── social_justice.csv
    └── placements_api_suggestions
        ├── channels_for_hate_terms.csv
        ├── channels_for_social_justice_terms.csv
        ├── videos_for_hate_terms.csv
        └── videos_for_social_justice_terms.csv
```

| filename or directory                             | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `data/reference/placement_api_example_responses/` | Examples of `blocked`, `partially_blocked`, `full` and `empty` responses from the "PlacementSuggestionService" API. See the methodology for details, and [determine_status](https://github.com/the-markup/investigation-youtube-ad-placements/blob/master/notebooks/utils.py#L4) in `notebooks/utils.py` for implementation.                                                                                                                                                                                                                                                                                                                                                         |
| `data/reference/what_is_blocked.xlsx`             | A spreadsheet with the kind of API responses for all the terms in our investigation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `data/output/tables/`                             | CSVs of tables that are in the methodology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `data/input/placements_api/`                      | This contains responses for keywords from `notebooks/terms.py` that we submitted to the "PlacementSuggestionService" API. Each subdirectory is organized by the keyword list used. `blocked` are terms that we resubmitted after removing spaces, and `blocked_basewords` are terms that were blocked and resubmitted word-by-word.                                                                                                                                                                                                                                                                                                                                                  |
| `data/output/placements_api_keyword_status/`      | Contains the API status of keywords from `notebooks/terms.py` after being sent through the "PlacementSuggestionService" API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `data/output/placements_api_suggestions/`         | The suggested YouTube videos and channels for each search term.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `data/input/placements_api_deep3/`                | API responses for the `hate` terms "we wuz kangz", "white ethnostate" and "white genocide" beyond the topline 20 video suggestions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `data/input/video_metadata/`                      | Video metadata for suggested videos from the YouTube Data API (v3). Collected with the unofficial Python client ([YouTube Data API](https://youtube-data-api.readthedocs.io/en/latest/))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `data/input/channel_lists/`                       | Contains channel names and IDs that researchers at EPFL and UFMG identified as "alt-right" and "alt-lite" in their 2020 ACM FAT* paper "[Auditing radicalization pathways on YouTube](https://dl.acm.org/doi/abs/10.1145/3351095.3372879)". We used a supplementary "extremist" and "alternative" channel list created by researchers for the ADL report "[Exposure to Alternative & Extremist Content on YouTube](https://www.adl.org/resources/reports/exposure-to-alternative-extremist-content-on-youtube)", however that list is only available [by request](https://www.adl.org/resources/reports/exposure-to-alternative-extremist-content-on-youtube#the-belfer-fellowship). |
| `data/output/channel_overlap.csv`                 | The count of unique "extremist", "alternative", "alt-right" and "alt-lite" videos and channels from the topline suggestions for `hate` terms we sent through the "PlacementSuggestionService" API. We included the channels that were suggested in the `channels` column.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `data/input/hate_terms_background_info.csv`       | Links for more information about each of the terms in the `hate` list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `data/z_data_rerun/`                              | API responses from re-running the experiment on March 31, 2021. Identical organization as `data/input/placements_api/` and `data/output/placements_api_keyword_status/`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Licensing

Copyright 2021, The Markup News Inc.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.