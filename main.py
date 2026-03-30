import os
import platform
import subprocess
import sys
from pathlib import Path

import streamlit as st


def run_command(command: list[str]) -> str:
    try:
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return "not found"
    except subprocess.CalledProcessError as exc:
        return (exc.stderr or exc.stdout or str(exc)).strip()
    return (completed.stdout or completed.stderr).strip()


st.set_page_config(
    page_title="WSL + Git Workshop Demo",
    page_icon=":hammer_and_wrench:",
    layout="centered",
)

st.title("WSL + Git + 环境配置 Workshop Demo")
st.caption("如果你能看到这个页面，说明 git clone、conda、pip、streamlit 这条链路已经跑通。")

student_name = st.text_input("输入你的名字", "Student")
if student_name:
    st.success(f"你好，{student_name}。你已经成功跑起一个 GitHub 项目。")

st.subheader("环境检查")
st.code(
    "\n".join(
        [
            f"Python: {sys.version.split()[0]}",
            f"Executable: {sys.executable}",
            f"Platform: {platform.platform()}",
            f"Current directory: {Path.cwd()}",
            f"Current file: {Path(__file__).name}",
            f"Conda env: {os.environ.get('CONDA_DEFAULT_ENV', '(not activated)')}",
            f"Git: {run_command(['git', '--version'])}",
        ]
    ),
    language="text",
)

st.subheader("课堂练习")
st.markdown(
    """
1. 把页面标题改成你自己的版本。
2. 把欢迎语改成你自己的名字。
3. 点击下面按钮，确认你修改后的页面已经生效。
4. 执行 `git status`、`git add .`、`git commit -m "Personalize demo"`。
"""
)

if st.button("点我放烟花"):
    st.balloons()
    st.info("如果你能看到这个效果，说明代码修改和页面交互都正常。")

st.subheader("为什么这个项目适合教学")
st.write(
    "它故意只有一个入口文件和一个依赖清单，方便初学者把注意力放在环境搭建、命令理解和 Git 基本流程上。"
)
