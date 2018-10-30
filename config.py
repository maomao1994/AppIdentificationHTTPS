#!/usr/bin/env python
#encoding=utf-8
"""
@author: TianMao
@contact: tianmao1994@yahoo.com
@file: config.py
@time: 18-10-24 下午3:33
@desc: 配置文件
"""
HTTPS_CONFIG={
    "pcap_path":"../../data/wd_https/raw_pcap/",
    "total_path":"../../data/wd_https/output/total/",
    "vedio_path":"../../data/wd_https/output/vedio/",
    "social_path":"../../data/wd_https/output/social/",
    "news_path":"../../data/wd_https/output/news/",
    "music_path":"../../data/wd_https/output/music/",
    "ebook_path":"../../data/wd_https/output/ebook/",
    "record_type_path":"../../data/wd_https/record_type/total/",
    "packet_lenth_path":"../../data/wd_https/packet_length/total/",
    "choose":"total_path",
    "ouput_path":"../../data/wd_https/https_train_eval/output.csv",
    "train_path":"../../data/wd_https/https_train_eval/train.csv",
    "val_path":"../../data/wd_https/https_train_eval/val.csv",

    "all_train_path":"../../data/wd_https/https_train_eval/all_train.csv",
    "all_val_path":"../../data/wd_https/https_train_eval/all_val.csv",
    "record_type_total":"../../data/wd_https/record_type/total/",
    "record_type_output_path":"../../data/wd_https/https_train_eval/record_type.csv",
    "record_type_train_path":"../../data/wd_https/https_train_eval/record_type_train.csv",
    "record_type_val_path":"../../data/wd_https/https_train_eval/record_type_val.csv",

    "packet_length_total":"../../data/wd_https/packet_length/total/",
    "packet_length_output_path":"../../data/wd_https/https_train_eval/packet_length.csv",
    "packet_length_train_path":"../../data/wd_https/https_train_eval/packet_length_train.csv",
    "packet_length_val_path":"../../data/wd_https/https_train_eval/packet_length_val.csv",

    "train_data_sni_path":"../../data/wd_https/https_train_eval/train_data_sni.csv",
    "val_data_sni_path":"../../data/wd_https/https_train_eval/val_data_sni.csv",
    "combined_data":"../../data/wd_https/https_train_eval/combined_data.csv",
    "filtered_data":"../../data/wd_https/https_train_eval/filtered_data.csv",
    "num_class":3,
    "outcome":"../outcome/",
    "result":"../result/"
}