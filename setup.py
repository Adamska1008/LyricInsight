from setuptools import setup, find_packages

setup(
    name="lyricinsight",  # 包名
    version="0.1.0",  # 版本号
    description="A tool to process Japanese lyrics into a practice-friendly format.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # 让 PyPI 显示 markdown 格式的 README
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/lyricinsight",  # 替换为实际的项目地址
    license="MIT",
    packages=find_packages(),
    include_package_data=True,  # 包含非代码文件
    install_requires=[
        "openai==1.57.2",
    ],
    entry_points={
        "console_scripts": [
            "lyricinsight=lyricinsight.main:main",  # 定义可执行命令
        ]
    },
    python_requires=">=3.13",  # 限定支持的 Python 版本
)
