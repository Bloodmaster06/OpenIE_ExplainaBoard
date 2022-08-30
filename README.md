# OpenIE_ExplainaBoard

## 测试脚本
测试脚本使用方法：
```
python eval.sh --CFG xx.cfg
```
其中cfg文件位于 /configs文件夹中，在cfg文件中给定测试文件，模型输出结果，以及测试结果存放路径即可。

## 训练集
其格式如下：
```
words       ex_tag  pre     ext1    ext2
Courtaulds  NP      O       A0-B    O
'           NP      O       A0-I    O
spinoff     NP      O       A0-I    O
reflects    O       P-B     P-B     O
pressure    NP      O       A1-B    O
on          O       O       A1-I    O
British     NP      O       A1-I    A1-B
industry    NP      O       A1-I    A1-I
to          O       O       O       O
boost       O       P-B     O       P-B
share       NP      O       O       0-B
prices      NP      O       O       0-I
beyond      O       O       A2-B
the         NP      O       O       A2-I
reach       NP      O       O       A2-I
of          NP      O       O       A2-I
corporate   NP      O       O       A2-I
raiders     NP      O       O       A2-I
.           O       O       O       O
```
第一列为文本，第二列句子中蕴含的所有relation，第三列之后每一列都对应一个extraction的序列标注。

## 测试集
其格式如下：
```
Earlier this year , President Bush made a final `` take - it - or - leave it '' offer on the minimum wage : an increase to $ 4.25 an hour over three years , and only if accompanied by a lower wage for the first six months of a job .	made a final `` take - it - or - leave it '' offer on	President Bush	the minimum wage	Earlier this year

Earlier this year , President Bush made a final `` take - it - or - leave it '' offer on the minimum wage : an increase to $ 4.25 an hour over three years , and only if accompanied by a lower wage for the first six months of a job .	is	Bush	President

Blagoja ` Billy ' Celeski is an Australian footballer who plays as a midfielder for the Newcastle Jets .	is	Blagoja ` Billy ' Celeski	an Australian footballer

Blagoja ` Billy ' Celeski is an Australian footballer who plays as a midfielder for the Newcastle Jets .	plays	Blagoja ` Billy ' Celeski	as a midfielder
```
测试文件输出格式为 [sentences] [relation] [arg_0] [arg_1],...,[arg_n]\\
即，句子（每个word以空格分隔），relation，与relation相关的arguments。每部分内容（[]内的部分）以一个tab分隔。需要注意的是同一个句子可能会被预测出不同的结果，根本原因是一个句子中可能含有多个不同的relation。模型的输出以及test_gold（测试集标准答案）均为以上格式。

## 测试结果指标
测试结果指标主要包括三个指标：precision, recall, f1。\\
评测过程中将relation和arguments统一视为entities参与评测。\\
评测指标可选模式很多，主要是一些判断是否正确的标准上的区别（比如span和text都要正确，或者仅需要text正确）。但大体都遵循以下计算方式。\\
precision = 预测正确的enties数量/预测entities数量\\
recall = 预测正确的enties数量/gold的entities数量\\
f1 = 2\*precision\*recall / (precision+recall)\\
