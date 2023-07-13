from typing import Union, Tuple, List
import numpy as np
import random
import pandas as pd
import torch
import numpy as np
import random
import pandas as pd
from datetime import datetime, date
from tqdm.notebook import tqdm
from tqdm import tqdm
# from IPython.display import Image
from joblib import Parallel, delayed
import re
import argparse
import gc
from datetime import datetime, date
from tqdm.notebook import tqdm
from tqdm import tqdm
# from IPython.display import Image
from joblib import Parallel, delayed
import json
import ast
from data_utils import *


def main(args):
    print('-------------------Reading Datas-------------------')
    with open('/opt/ml/wine/code/data/feature_map/item2idx.json','r') as f: item2idx = json.load(f)
    with open('/opt/ml/wine/data/price_vocab.json','r') as f: price_vocab = json.load(f)
    with open('/opt/ml/wine/data/note.json','r') as f: notes_data = json.load(f)
    
    basic_info = pd.read_csv('/opt/ml/wine/data/basic_info_total.csv')
    wine_df = pd.read_csv('/opt/ml/wine/data/wine_df.csv')
    review_df = pd.read_csv('/opt/ml/wine/data/review_df_total.csv',encoding = 'utf-8-sig').loc[:,['user_url','rating','text','wine_url']]
    print('-------------------Done-------------------')
    print()

    print('-------------------Processing review text-------------------')
#########################REVIEW DATA#########################
    review_df = review_df[review_df['text'].isna()==False]
    review_df['text'] = review_df['text'].apply(lambda x: x + '.' if x[-1] != '.' else x)

    review_df['text'] = review_df['text'].apply(keep_english_and_digits)
    review_df['wine_id'] = review_df['wine_url'].map(item2idx)
    review_df = review_df[review_df['wine_id'].isna()==False]
    review_df['wine_id'] = review_df['wine_id'].astype('int').astype('category')

    review_df['length'] = review_df['text'].apply(get_len_text)
    review_df = review_df.loc[:, 'wine_id','text','length']

    review_df = review_df.sort_values(['wine_id', 'length'])
    review_df = merge_short_review(review_df, args.min_len)

#########################PRICE LABEL#########################
    
    price_label = marking_price_data(review_df, price_vocab)

#########################NOTE LABEL#########################
    notes_data = get_notes_group(wine_df)
    note_label = parallel_dataframe_2input(marking_note_data, review_df, notes_data, 8)
  
    
    wine_info = wine_df.loc[:, ['url','winetype']].merge(basic_info, on='url')
    wine_info['wine_id'] = wine_info['url'].map(item2idx)
    wine_info = wine_info[wine_info['wine_id'].isna()==False]
    wine_info['wine_id'] = wine_info['wine_id'].astype('int').astype('category')
    wine_info = wine_info.loc[:,['wine_id','country','grapes','winetype']]

    wine_info, grape2idx, country2idx, winetype2idx = gen_labeled_data(wine_info)

    with open('/opt/ml/wine/code/feature_map/grape2idx.json','w') as f: json.dump(grape2idx, f)
    with open('/opt/ml/wine/code/feature_map/country2idx.json','w') as f: json.dump(country2idx, f)
    with open('/opt/ml/wine/code/feature_map/winetype2idx.json','w') as f: json.dump(winetype2idx, f)

    labeled_data = pd.merge(review_df, wine_info, on = 'wine_id', how = 'inner')
    del wine_info, review_df
    gc.collect()
    labeled_data = pd.merge(labeled_data, note_label, on = 'wine_id', how = 'inner')
    del note_label
    gc.collect()
    labeled_data = pd.merge(labeled_data, price_label, on = 'wine_id', how = 'inner')
    print('-------------------Done-------------------')
    labeled_data.to_csv(args.save_path)
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
#######Train#############################################################################
    parser.add_argument("--min_len", default=6, type=int)
    parser.add_argument("--save_path", default="/opt/ml/wine/data/labeled_review.csv", type=str)
     
    args = parser.parse_args()
    main(args)