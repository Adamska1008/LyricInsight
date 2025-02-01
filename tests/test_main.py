"""
"""

from main import SplitJob


import sys
import os

# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))


def test_split():
    lyrics = """花道を薄く照らして（淡薄照亮花道）

hanamichi wo usuku terashite


寄せ木細工　音を奏でた（拼貼木紋　奏出音色）

yosegizaiku oto wo kanadeta


艶やかな　上弦の月（艷麗的　上弦之月）

adeyaka na jougen no tsuki


雲に消えた　傘もないのに（消失於雲中　明是手中也無傘）

kumo ni kieta kasa mo nai noni


朝がきてそれが春の霜解（しもど）けの様に（黎明到來那就如春日雪融般）

asa ga kite sore ga haru no shimodoke no youni


凍てついた戀がいつか熱く流れるならば（冰凍的愛戀若將有日　熾熱流淌）

itetsuita koi ga itsuka atsuku nagareru naraba


終わらない雨の中で抱きしめて（就在不止的雨中緊緊擁抱吧）

owaranai ame no naka de dakishimete


貴方が答えを隠しているのなら（若你藏起了解答）

anata ga kotae wo kakushite iru no nara


変わらない聲でどうか囁いて（至少請用不變的聲音呢喃）

kawaranai koe de douka sasayaite


壊れた心をせめて包んで（包容那毀壞的心吧）

kowareta kokoro wo semete tsutsunde
"""
    expected = [
        [
            """花道を薄く照らして（淡薄照亮花道）
hanamichi wo usuku terashite
寄せ木細工　音を奏でた（拼貼木紋　奏出音色）
yosegizaiku oto wo kanadeta
艶やかな　上弦の月（艷麗的　上弦之月）
adeyaka na jougen no tsuki""",
            """雲に消えた　傘もないのに（消失於雲中　明是手中也無傘）
kumo ni kieta kasa mo nai noni
朝がきてそれが春の霜解（しもど）けの様に（黎明到來那就如春日雪融般）
asa ga kite sore ga haru no shimodoke no youni
凍てついた戀がいつか熱く流れるならば（冰凍的愛戀若將有日　熾熱流淌）
itetsuita koi ga itsuka atsuku nagareru naraba""",
            """終わらない雨の中で抱きしめて（就在不止的雨中緊緊擁抱吧）
owaranai ame no naka de dakishimete
貴方が答えを隠しているのなら（若你藏起了解答）
anata ga kotae wo kakushite iru no nara
変わらない聲でどうか囁いて（至少請用不變的聲音呢喃）
kawaranai koe de douka sasayaite""",
            """壊れた心をせめて包んで（包容那毀壞的心吧）
kowareta kokoro wo semete tsutsunde""",
        ],
    ]
    job = SplitJob(5, 3)
    inps = job.apply(lyrics)
    for i, inp in enumerate(inps):
        assert expected[0][i] == inp
    job = SplitJob(5, 5)
    inps = job.apply(lyrics)
    for i, inp in enumerate(inps):
        print(i)
        print(inp)
