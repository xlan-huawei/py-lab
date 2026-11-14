# Python 开发环境说明

本机 Python 环境由 DSH 会话于 2026-11-14 配置完成,所有内容都在 D 盘。

## 目录

| 用途 | 路径 |
|---|---|
| Python 解释器 | `D:\DevTools\Python314\python.exe`(3.14.10) |
| 项目虚拟环境 | `D:\PythonProject\.venv` |
| pip 缓存 | `D:\DevTools\pip-cache` |
| pip 临时目录 | `D:\DevTools\tmp` |
| 代码与测试 | `D:\PythonProject\main.py`、`D:\PythonProject\tests` |

## 日常使用

在 VS Code 里打开 `D:\PythonProject` 即可:解释器已指向 `.venv`,pytest 已启用,Ruff 负责格式化与检查。

命令行方式:

```powershell
cd D:\PythonProject
.\.venv\Scripts\Activate.ps1
python main.py
pytest -q
ruff check .
```

VS Code 终端会通过 `terminal.integrated.env.windows` 把 `TEMP` / `TMP` / `PIP_CACHE_DIR` 指到 D 盘。

## 两点已知限制

1. **Smart App Control 会拦截"无信誉"的新二进制**。`pandas 3.1.1` 的 `ops.cp314-win_amd64.pyd`
   被拦(`WinError 4551: 应用程序控制策略已阻止此文件`),因此锁定在 `pandas==3.1.0`。
   若将来 `pip install --upgrade pandas` 后导入报 `DLL load failed`,就是同一个原因,
   回退到 3.1.0 即可;或者等该版本建立信誉后再升级。
2. **PyPI 直连不稳定**(下载几 MB 就中断重试),`%APPDATA%\pip\pip.ini` 已改用清华镜像:

```ini
[global]
cache-dir = D:/DevTools/pip-cache
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
timeout = 60
retries = 5

[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```

需要恢复官方源时,编辑该文件即可。
