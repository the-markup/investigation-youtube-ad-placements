# YouTube Placements API Blocklist



## Notebooks
1. How we collected data
2. How we parse the data
3. How we refined the data
4. How We analyzed the data


## Data
`data/input/placements_api` -  This contains responses from the YouTube "PlacementSuggestionService" API.<br>
`data/input/sources` - Contains keyword lists curated from several sources<br>
`data/input/crossref` - 


`data/output/placements_api_keyword_status` - Contains the status of keywords from `data/input/sources` after being sent through the "PlacementSuggestionService" API.<br>
`data/output/placements_api_suggestions` - The suggested YouTube videos and channels for each search term.<br>
`data/output/video_metadata` - Contains video metadata for videos suggested from Hate keywords. Data collected from the YouTube Data API V3.

`data/output/crossref` - The overlap of channels found in our investigation and those the ADL categorized as "extremist" or "alternative"