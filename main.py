import os
import argparse
from openai import OpenAI
from loguru import logger
import typeguard
import prompts


class SplitJob:
    """
    Describe how lyrics will be divided
    """

    single_lyrics_lines: int  # 一句歌词占几行
    lyrics_per_group: int | None  # 一组翻译几句歌词。越小，模型表现越好。
    remove_blank_lines: bool

    def __init__(
        self,
        sinlgle_lyrics_lines: int,
        lyrics_per_group: int = None,
        remove_blank_lines=True,
    ):
        self.single_lyrics_lines = sinlgle_lyrics_lines
        self.lyrics_per_group = lyrics_per_group
        self.remove_blank_lines = remove_blank_lines

    @typeguard.typechecked
    def apply(self, inp: str) -> list[str]:
        """
        Apply the split job on the input str.
        If self.lyrics_per_group is None, return a list with single element (the whole lyrics)
        """
        inps = inp.splitlines()
        # divide `self.single_lyrics_lines` lines into a group
        inps = [
            inps[i : i + self.single_lyrics_lines]
            for i in range(0, len(inps), self.single_lyrics_lines)
        ]
        # remove blank lines
        for i, group in enumerate(inps):
            inps[i] = [inp for inp in group if len(inp) != 0]
        inps = ["\n".join(inp) for inp in inps]
        if self.lyrics_per_group:
            inps = [
                "\n".join(inps[i : i + self.lyrics_per_group])
                for i in range(0, len(inps), self.lyrics_per_group)
            ]
        else:
            inps = ["\n".join(inps)]
        return inps


@typeguard.typechecked
def transform(inp: str, job: SplitJob) -> str:
    # client = OpenAI(
    #     base_url=os.getenv("DEEPSEEK_BASE_URL"), api_key=os.getenv("DEEPSEEK_API_KEY")
    # )
    client = OpenAI()
    # split input
    inps = job.apply(inp)

    res = ""

    for index, inp in enumerate(inps):
        logger.info(f"处理第{index + 1}组歌词")
        logger.info(f"输入:\n{inp}")
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompts.sys_prompt},
                {"role": "user", "content": prompts.examples[0][0]},
                {"role": "assistant", "content": prompts.examples[0][1]},
                {"role": "user", "content": inp},
            ],
        )
        res += completion.choices[0].message.content + "\n"

    return res


def main():
    parser = argparse.ArgumentParser(description="将日文歌词解析为易于练习演唱的格式。")
    parser.add_argument("file", type=str, help="歌词文件")

    args = parser.parse_args()
    filename = args.file
    with open(filename, "r", encoding="UTF-8") as f:
        content = f.read()
    print("歌词转换中……")
    transformed = transform(content, SplitJob(5, 4))
    base_name, extension = os.path.splitext(filename)
    new_filename = f"{base_name}_transformed.{extension}"
    with open(new_filename, "a", encoding="UTF-8") as f:
        f.write(transformed)

    print(f"歌词转换完毕，输出到{new_filename}")


if __name__ == "__main__":
    main()
