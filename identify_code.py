import os
import random

rate = 0.2

data_path = './Discuz'
# 读取图片
imgs = os.listdir(data_path)
# 打乱图片顺序
random.shuffle(imgs)

imgs_num = len(imgs)
test_imgs_num = int(imgs_num * rate)
train_imgs_num = int(imgs_num * (1 - rate))
test_imgs = imgs[:test_imgs_num]
train_imgs = imgs[test_imgs_num:]
# 根据文件名获取测试集标签
test_labels = list(map(lambda x: x.split('.')[0], test_imgs))
# 根据文件名获取训练集标签
train_labels = list(map(lambda x: x.split('.')[0], train_imgs))
