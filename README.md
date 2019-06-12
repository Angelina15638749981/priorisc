# 文字识别算法

###### 采用双向LSTM + CRNN， 用于识别图片上的不定长文字
 

## 举例 
###### 训练或预测文件放/pic_omis/out
##
##### · 训练命令
python run.py -ex ../pic_omis/out --train
##
##### · 预测命令
python run.py -ex ../pic_omis/out --test --restore
