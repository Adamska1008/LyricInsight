"""
stores prompts string literal
"""

sys_prompt = """你将被提供一段日文歌词，其中每一句歌词都由日文，罗马音和中文翻译组成。
你的任务是
1. 将罗马音按照音节划分，中间加上空格
2. 按含义划分词组，并在词组后加入括号，填上提供的对应的中文翻译和日文原文
 - 词组应保持细粒度，每一句划分3~5个词组
 - 如果原中文是繁体，翻译为简体
 - 句末的罗马音词组也应有中文翻译
3. 每句歌词只输出步骤1、2中处理后的罗马音
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
ka ji ka n da ko ko ro (憔悴的心 悴んだ心) fu ru e ru ma na za shi (摇曳不定的目光 ふるえる眼差し) se ka i de (这世间 世界で)
bo ku wa (唯我是 僕は) hi to ri bo tchi da tta (孤身一人 ひとりぼっちだった) chi ru ko to shi ka shi ra na i ha ru wa (这不停凋零的春季 散ることしか知らない春は)
ma i to shi (每年 毎年) tsu me ta ku a shi ra u (冷淡地应付 冷たくあしらう)
""",
    ),
]
