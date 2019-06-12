# 文字识别算法

###### 采用双向LSTM + CRNN， 用于识别图片上的不定长文字
###### 训练集采用自生成方式， 训练 600 epoch 识别率可达96.5%

#### 自生成文件放在 pic_gentor 内，主要做训练图片自生成，tests.py 罗列了一些调整生成图片
#### 的背景、字体、模糊等方法，用于模仿实际应用场景中90%经过处理后的图片情况，这里假定图片
#### 在进行识别前是通过opencv或其他软件处理成与生成图片相同的情况。
 

## 举例 
###### 训练或预测文件放/pic_omis/out
##
##### · 训练命令
python run.py -ex ../pic_omis/out --train
##
##### · 预测命令
python run.py -ex ../pic_omis/out --test --restore
