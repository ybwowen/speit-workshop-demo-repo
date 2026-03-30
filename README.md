# SPEIT Workshop Demo

这个仓库故意设计成很小，但安装流程故意完整走一遍：

`apt -> git clone -> conda -> pip -> streamlit run`

## 仓库结构

```text
.
├── README.md
├── main.py
└── requirements.txt
```

## Review

- `apt`：安装系统工具，例如 `git`、`curl`、`wget`
- `git`：从 GitHub 拉代码
- `conda`：创建独立 Python 环境
- `pip`：安装当前项目依赖

如果这四件事混在一起，后面很容易出错。

## 在 WSL / MacOS 里安装基础工具

先把系统工具装好，这一步明确使用 `apt`。

命令：

```bash
sudo apt update
sudo apt install -y git curl wget
```

为什么：

- 没有 `git`，你无法 `git clone`
- 没有 `wget`，你不方便下载 Miniconda
- 没有 `curl`，你不方便检查服务端口

## 克隆这个仓库

代码应该来自远程仓库，而不是手工复制粘贴文件。

命令：

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/your-org/wsl-git-python-workshop-demo.git
cd wsl-git-python-workshop-demo
```

为什么：

这一步让你真实体验工程项目的起点：先把代码拿到本地。

如果你已经拿到了老师发的整个 `workshop-package/` 文件夹，也可以直接进入本地目录先跑：

```bash
cd <path-to-workshop-package>/demo-repo
```

## 安装 Miniconda

这个项目推荐用 conda 创建独立环境，不建议直接污染系统 Python。

命令：

```bash
cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
conda --version
```


不同项目可能需要不同 Python 版本。conda 的价值就是隔离环境。

## 配置国内镜像

### pip 镜像

国内网络环境下，先切 `pip` 镜像通常更稳。

命令：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip config list
```

### conda 镜像

如果你所在网络环境访问 conda 官方源较慢，建议直接修改 `.condarc`。

命令：

```bash
cat > ~/.condarc <<'EOF'
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
EOF

conda clean -i
```


这样可以降低 conda 创建环境时的下载失败率。

## 5. 创建 conda 环境

解释：

每个项目尽量单独一个环境。

命令：

```bash
conda create -n workshop-demo python=3.11 -y
conda activate workshop-demo
which python
python --version
```

为什么：

如果 `python` 和 `pip` 不在你想要的环境里，后面很容易出现“装了包但运行还是报错”。

## 安装 Python 依赖

解释：

项目依赖在 `requirements.txt` 里，由 `pip` 负责安装。

命令：

```bash
pip install -r requirements.txt
```

区分：

- `git` 拉的是代码
- `pip` 装的是代码依赖

## 运行项目

解释：

这个仓库是一个最小 Streamlit app，启动方式如下。

命令：

```bash
streamlit run main.py
```

为什么：

如果浏览器成功打开页面，说明你的整条链路已经通了。

## 验证项目是否真的跑起来

解释：

有时候浏览器没弹出，但服务其实已经启动了。

命令：

```bash
curl -I http://127.0.0.1:8501
```

为什么：

这是最简单的服务存活检查。

## 课堂练习

做下面三件事：

1. 修改 `main.py` 里的标题。
2. 把输入框默认名字改成你自己的名字。
3. 重新启动应用，确认页面变化。

然后执行：

```bash
git status
git diff
git add .
git commit -m "Personalize demo app"
```

### Git 扩展练习 (Optional)

#### 练习 1：看提交历史

不要只会提交，还要会回头看历史。

命令：

```bash
git log --oneline --graph --decorate -5
```

为什么：

这能帮助你建立“仓库是有时间线的”这个概念。

#### 练习 2：新建并切换分支

解释：

真实项目里，很少所有人都直接在 `main` 上改。

命令：

```bash
git checkout -b add-my-name
```

或者：

```bash
git switch -c add-my-name
```

为什么：

你会开始理解分支是“独立修改线”。

#### 练习 3：切回主分支

解释：

`checkout` 和 `switch` 都可以切换分支。网上老教程通常写 `checkout`，所以你必须认识它。

命令：

```bash
git checkout main
```

或者：

```bash
git switch main
```

为什么：

以后你读教程和项目文档时会频繁看到这些命令。

#### 练习 4：理解 push 和 pull

解释：

本地 commit 完成后，并不会自动出现在 GitHub 上。

命令：

```bash
git push origin main
git pull
```

为什么：

- `push`：把本地提交发到远程
- `pull`：把远程更新拿到本地

课堂提醒：

如果你 clone 的是老师的仓库，你通常没有 push 权限。这一步更适合老师演示。

#### 练习 5：理解 cherry-pick

解释：

如果你只想把某一个提交单独拿过来，可以用 `cherry-pick`。

命令：

```bash
git log --oneline --graph --decorate -5
git cherry-pick <commit-id>
```

为什么：

这在真实项目里很常见，例如只摘一个 bug fix。

#### 练习 6：理解 rebase

解释：

`rebase` 常用于把当前分支的提交整理到最新的 `main` 后面。

命令：

```bash
git checkout add-my-name
git rebase main
```

为什么：

以后团队里有人让你“先 rebase 一下”，你至少知道它是在整理提交历史。

课堂提醒：

`rebase` 会改历史。公共分支不要随便乱用。

#### 练习 7：理解 reset

解释：

`reset` 可以撤回本地 commit，但不同模式影响不同。

命令：

```bash
git reset --soft HEAD~1
git reset HEAD~1
```

为什么：

- `--soft`：撤回 commit，但保留暂存区
- 默认 mixed：撤回 commit，也撤回暂存区，但保留工作区

课堂强提醒：

```bash
git reset --hard HEAD~1
```

会直接丢工作区改动。不要在没搞清楚前乱用。

## 常见问题

### 问题 1：`conda: command not found`

执行：

```bash
~/miniconda3/bin/conda init bash
source ~/.bashrc
conda --version
```

### 问题 2：`CondaError: Run 'conda init' before 'conda activate'`

执行：

```bash
conda init bash
source ~/.bashrc
conda activate workshop-demo
```

### 问题 3：`pip install -r requirements.txt` 很慢

先确认：

```bash
pip config list
```

如果没切镜像，重新执行：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题 4：浏览器打不开页面

先确认服务是不是活着：

```bash
curl -I http://127.0.0.1:8501
```

如果端口冲突，换端口：

```bash
streamlit run main.py --server.port 8502
```

### 问题 5：`git clone` 失败

先确认：

```bash
git --version
ping -c 2 github.com
```

如果 GitHub 网络不稳定，直接使用讲师提供的 zip 包继续课堂。

## 11. 课堂不翻车建议

如果你是讲师，建议你额外准备：

- 一个本地 `Miniconda3-latest-Linux-x86_64.sh`
- 一个 `demo-repo.zip`
- 一个本地 `wheelhouse/`

提前下载 Python 依赖的方法：

```bash
pip download -r requirements.txt -d wheelhouse
```

离线安装方法：

```bash
pip install --no-index --find-links=wheelhouse -r requirements.txt
```
