import argparse
from openai import OpenAI
import prompts


def transform(input: str) -> str:
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompts.sys_prompt},
            {"role": "user", "content": prompts.examples[0][0]},
            {"role": "assistant", "content": prompts.examples[0][1]},
            {"role": "user", "content": input},
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将日文歌词解析为易于练习演唱的格式。")
    parser.add_argument("file", type=str, help="歌词文件")

    args = parser.parse_args()
    filename = args.file

    with open(filename, "r") as f:
        content = f.read()

    transformed = transform(content)
    print("歌词转换中……")
    print(transformed)
