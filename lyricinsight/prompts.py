sys_prompt = """
你是一位日文歌老师。你将被提供一段日文歌词，包括日文，罗马音和中文翻译。
你的任务是
1. 将罗马音按照每个字的发音划分，加上空格
2. 划分词组，在括号内填写中文翻译
3. 每句歌词只输出处理过的罗马音
"""

examples = [
    (
        """
悴んだ心 ふるえる眼差し 世界で
kajika n da kokoro fu ru e ru manazashi sekai de
憔悴的心 摇曳不定的目光 这世间

僕は ひとりぼっちだった 散ることしか知らない春は
bokuwa hi to ri bo tchi da tta chi ru ko to shi ka shi ra na i haru wa
唯我是 孤身一人 这不停凋零的春季

毎年 冷たくあしらう
maitoshi tsumeta ku a shi ra u
每年都只是冷淡地应付
""",
        """
ka ji ka n da ko ko ro(憔悴的心) hu ru e ru ma na(摇曳不定的目光) za shi se~ka i de(这世间)
bo ku wa(唯我是) hi to ri bo tchi(孤身一人) da tta(曾经) chi ru ko to shi ka shi ra na i(这不停凋零的春季)
mai to shi(每年) tsu me ta ku(冷淡地) a shi ra u(应付)
""",
    ),
]
