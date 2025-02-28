# LyricInsight

用于将日文歌词（包括罗马音和中文翻译）处理为更适合练习演唱的格式。

虽然罗马音能帮助指导发音，但有时即使有了罗马音，也很难准确掌握演唱的节奏。例如，在《春日影》中：

```plaintext
... ippoutsuukou ..
```

这个长单词（“一方通行”）的发音可能令人困惑。经过处理后：

```plaintext
i ppo u tsuu ko u (单向通行)
```

逐音拆分的形式不仅更直观，还更方便理解和练习。同时，将中文翻译嵌入每个词汇旁边，也能帮助更轻松地理解歌词的含义。

通过prompt engineering实现，目前只使用OpenAI的gpt-4o-mini。**注意**，由AI生成的内容不保证正确性，使用时请自行检查。

## Usage

以春日影为例。将歌词放在文本文件中：

```plaintext
# examples/haruhikage.txt
悴んだ心 ふるえる眼差し 世界で
kajika n da kokoro fu ru e ru manazashi sekai de
憔悴的心 摇曳不定的目光 这世间

僕は ひとりぼっちだった 散ることしか知らない春は
bokuwa hi to ri bo tchi da tta chi ru ko to shi ka shi ra na i haru wa
唯我是 孤身一人 这不停凋零的春季

毎年 冷たくあしらう
maitoshi tsumeta ku a shi ra u
每年都只是冷淡地应付

暗がりの中 一方通行に ただ ただ
kuragari no naka ippoutsuukou ni ta da ta da
在黑暗深处 单向通行 仅仅 仅仅是

....
```

运行

```sh
uv run main.py [FILENAME]
```

输出将保存到后缀带有`_transformed`的文本文件中。

```plaintext
歌词转换中……
ka ji ka n da ko ko ro(憔悴的心) hu ru e ru ma na(摇曳不定的目光) za shi se~ka i de(这世间)  
bo ku wa(唯我是) hi to ri bo tchi(孤身一人) da tta(曾经) chi ru ko to shi ka shi ra na i ha ru wa(这不停凋零的春季)  
mai to shi(每年) tsu me ta ku(冷淡地) a shi ra u(应付)  
ku ra ga ri no na ka(在黑暗深处) i ppo u tsuu ko u ni(单向通行) ta da ta da(仅仅)  
ko to ba wo ka ki na gu tte(草草写下话语) ki ta i su ru da ke(仅仅是心怀期待) mu na shi i to wa ka tte i te mo(即便知道一切空虚)  
su ku i wo mo to me tsu zu ke ta(也在持续寻求着救赎)  
se tsu na ku te(苦闷不已) i to o shi i(惹人怜悯)  
i ma na ra ba(若是如今) wa ka ru ki ga su ru(好像已经明白)  
shi a wa se de(幸福满溢) ku ru o shi i(宛若疯狂)  
a no hi na ke na ka tta(那天没有哭出来的我)  
hi ka ri wa ya sa shi ku(是光芒温柔地) tsu re da tsu yo(与我结伴前行)
.... 
```

```sh
usage: main.py [-h] file

将日文歌词解析为易于练习演唱的格式。

positional arguments:
  file        歌词文件

options:
  -h, --help  show this help message and exit
```