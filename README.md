## LangGraph101 - AI Agent 项目骨架

一个基于 LangGraph + LangChain 的 AI Agent 项目模板，内置本地 Ollama 模型适配与示例工具/Agent。

### 目录结构
```
src/langgraph101/
  agents/
    react_agent.py        # ReAct 风格 Agent 的构建
  cli/
    main.py               # 命令行入口
  config/
    settings.py           # 配置（Ollama 端点/模型等）
  models/
    ollama.py             # Ollama 模型工厂
  tools/
    weather.py            # 示例工具函数
  utils/
    messages.py           # 提取 Agent 返回结果的工具
  agent/
    agent.py              # 示例脚本（调用默认与个性化 Agent）
```

### 快速开始
1. 创建并激活虚拟环境
```bash
cd /Users/yishenchen/Project/AI/LangGraph101
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动/确认 Ollama 服务与模型
```bash
ollama pull llama3.2:latest
```

4. 运行示例脚本
```bash
PYTHONPATH=src python -m langgraph101.agent.agent
```

5. 使用命令行入口
```bash
PYTHONPATH=src python -m langgraph101.cli.main "what is the weather in sf"
PYTHONPATH=src python -m langgraph101.cli.main "what is the weather in sf" --user "John Smith"
```

### 配置
通过环境变量覆盖默认配置：
- OLLAMA_BASE_URL (默认 `http://127.0.0.1:11434`)
- OLLAMA_MODEL (默认 `llama3.2:latest`)
- OLLAMA_TEMPERATURE (默认 `0`)

### 开发
- 新增工具：在 `tools/` 编写函数，并在 `agents/` 的构建函数中将其加入 `tools=[...]`。
- 新增 Agent：在 `agents/` 新建构建函数，返回 `create_react_agent(...)` 或自定义图。
- 结果解析：使用 `utils/messages.py` 的 `extract_useful_info` 获取最终文本与工具调用/输出。

### 依赖
见 `requirements.txt`。


