import json
import pandas as pd

def determine_status(resp: dict) -> str:
    """
    Determines the status (`Full`, `Blocked`, `Partial Block` or `Empty`) 
    of or a given keyword's API response (`resp`).
    
    Examples for each kind of response in 
    `../data/reference/placements_api_response_examples`. 
    
    Please read the methodology for more detail.
    """
    if resp['is_blocked'] == True:
        return 'Blocked'
    elif resp['n_youtube_channels'] == 0 and resp['n_youtube_videos'] == 0:
        return 'Empty'
    elif resp['n_youtube_videos'] == 1:
        return 'Partial Block'
    return 'Full'

def value_counts(df: pd.DataFrame, 
                 col: str, 
                 *args, **kwargs) -> pd.DataFrame:
    """
    For a DataFrame (`df`): display normalized (percentage) 
    `value_counts(normalize=True)` and regular counts 
    `value_counts()` for a given `col`.
    """
    count = df[col].value_counts(*args, **kwargs).to_frame(name='count')
    perc = df[col].value_counts(normalize=True, *args,**kwargs) \
                  .to_frame(name='percentage')
    
    return pd.concat([count, perc], axis=1)

def process_api_response(fn) -> dict:
    """
    Reads the JSON returned from the API, and parses metadata for 
    YouTube video and channel suggestions.
    """
    data = json.load(open(fn))
    search_term = fn.split('/')[-1].replace('.json', '')
    record = {'fn' : fn, 'search_term' : search_term}
    if data == dict():
        record['is_blocked'] = True
        return record
    else:
        record['is_blocked'] = False
    try: 
        # 4 - YouTube channel suggestions
        youtube_channels_ = data.get('4')
        if youtube_channels_:
            youtube_channels_number = int(youtube_channels_['2'])
            youtube_channels = youtube_channels_.get('1', [])
            channel_meta = []
            for youtube_channel in youtube_channels:
                youtube_channel_meta_ = youtube_channel['8']
                row = dict(
                    youtube_channel_id = youtube_channel['7']['1']['1'],
                    youtube_channel_name = youtube_channel['7']['2'],
                    youtube_channel_subs = youtube_channel_meta_.get('2'),
                    youtube_channel_videos = youtube_channel_meta_['1'],
                    youtube_channel_thumbnail = youtube_channel_meta_['3']
                )
                channel_meta.append(row)
            record['n_youtube_channels'] = youtube_channels_number
            record['youtube_channels'] = channel_meta
    except: pass
    try:
        # 5 - YouTube video suggestions
        youtube = data.get('5')
        if youtube:
            youtube_number_videos = int(youtube['2'])
            youtube_videos = youtube.get('1', [])
            youtube_video_meta = []
            for youtube_video in youtube_videos:
                row = dict(
                    youtube_video_id = youtube_video['1'],
                    youtube_video_title = youtube_video['2'],
                    youtube_video_views = youtube_video['3'],
                    youtube_video_channel = youtube_video['4']    
                )
                youtube_video_meta.append(row)
            record['n_youtube_videos'] = youtube_number_videos
            record['youtube_videos'] = youtube_video_meta
    except: pass
    return record