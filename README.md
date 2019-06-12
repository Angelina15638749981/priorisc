# 文字识别算法

###### 采用双向LSTM + CRNN， 用于识别图片上的不定长文字
###### 训练集采用自生成方式， 训练 600 epoch 识别率可达96.5%
 

## 举例 
###### 训练或预测文件放/pic_omis/out
##
##### · 训练命令
python run.py -ex ../pic_omis/out --train
##
##### · 预测命令
python run.py -ex ../pic_omis/out --test --restore
