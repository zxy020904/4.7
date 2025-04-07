import os
import shutil
import pandas as pd

from weibo_crawler import *


def extract(x):
    # 将x配置在weibo-crawler的json文件中，运行weibo.py

    # 得到x.csv文件，将其中内容提取成和训练集一样的数据格式
    df_data_content=pd.read_csv(f'weibo_crawler\\weibo\\{x}\\{x}.csv')
    df_data_user_all=pd.read_csv('weibo_crawler\\weibo\\users.csv')
    df_data_user=df_data_user_all[df_data_user_all['用户id']==x]
    df_data_user=df_data_user.reset_index()
    data_altered=dict()
    data_altered['has_birth_date'] = (1 if df_data_user.loc[0,'生日'] else 99)
    data_altered['has_photo'] = (1 if df_data_user.loc[0,'头像']else 99)
    data_altered['gender']=(1 if df_data_user.loc[0,'性别']=='m' else 2 if df_data_user.loc[0,'性别']=='f' else 99)
    data_altered['has_nickname']=(1 if df_data_user.loc[0,'昵称'] else 99)
    data_altered['has_about'] = (1 if df_data_user.loc[0,'简介'] else 0)
    subscriber_value=df_data_user.loc[0,'关注数']
    data_altered['subscribers_count'] = subscriber_value
    data_altered['has_career'] = (1 if df_data_user.loc[0,'公司'] else 0)
    data_altered['has_schools'] = (1 if df_data_user.loc[0,'学习经历'] else 99)
    data_altered['is_verified'] = (1 if df_data_user.loc[0,'是否认证'] else 0)
    posts_value=df_data_user.loc[0, '微博数']
    data_altered['posts_count'] = posts_value
    likes_value=df_data_content['点赞数'].sum()
    data_altered['avg_likes'] = likes_value/posts_value
    comments_value=df_data_content['评论数'].sum()
    data_altered['avg_comments'] = comments_value/posts_value
    df_data_altered=pd.DataFrame(data_altered,index=[0])
    return df_data_altered

print(extract(5654104319))

























