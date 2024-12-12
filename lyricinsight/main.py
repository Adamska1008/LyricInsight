import argparse
from openai import OpenAI
from . import prompts


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


def main():
    parser = argparse.ArgumentParser(description="将日文歌词解析为易于练习演唱的格式。")
    parser.add_argument("file", type=str, help="歌词文件")

    args = parser.parse_args()
    filename = args.file

    with open(filename, "r") as f:
        content = f.read()
    print("歌词转换中……")
    transformed = transform(content)
    print(transformed)


if __name__ == "__main__":
    main()
