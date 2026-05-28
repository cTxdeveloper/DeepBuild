# DeepBuild Agent OS

A fully autonomous multi-agent development operating system built with CrewAI, LiteLLM, ChromaDB, and a modular plugin ecosystem.

## Features

- Goal-driven autonomous execution
- Persistent memory with ChromaDB
- Tiered multi-model routing
- Plugin & skill ecosystem
- Web search, browser, HTTP, vision, terminal, and YouTube transcript tools
- SQLite-backed persistent task queue
- Android / Termux compatibility
- Self-improving error learning system

## Project Structure

```text
agent-builder/
├── config/
├── plugins/
├── src/
│   ├── memory/
│   ├── plugins/
│   ├── tools/
│   └── utils/
├── requirements.txt
├── requirements-termux.txt
└── .env.example
```

## Installation

### Standard Environment

```bash
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
python src/main.py
```

### Android / Termux

```bash
pkg update && pkg upgrade
pkg install python git clang make binutils
pip install -r requirements-termux.txt
python src/main.py
```

## Usage

```bash
python src/main.py
```

Commands:

```text
/goal <description>
/status
/help
/exit
```

## Environment Variables

```ini
DEEPSEEK_API_KEY=
OPENROUTER_API_KEY=
GOOGLE_AI_STUDIO_KEY=
COMPOSIO_API_KEY=
SERPER_API_KEY=
TASK_DB_PATH=tasks.db
```

## License

MIT
