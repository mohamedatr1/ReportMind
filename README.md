<div align="center">

```
  ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗    ███╗   ███╗██╗███╗   ██╗██████╗
  ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ████╗ ████║██║████╗  ██║██╔══██╗
  ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║       ██╔████╔██║██║██╔██╗ ██║██║  ██║
  ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║       ██║╚██╔╝██║██║██║╚██╗██║██║  ██║
  ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║       ██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
  ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝
```

**AI-Powered Research Agent · Real-Time Web Search · Auto-Generated Reports**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Tavily](https://img.shields.io/badge/Tavily-Search_API-0EA5E9?style=for-the-badge)](https://tavily.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/mohamedatr1/ReportMind?style=for-the-badge&color=FBBF24)](https://github.com/mohamedatr1/ReportMind/stargazers)

<br/>

> **One query. Seconds. A complete, evidence-grounded research report.**

</div>



https://github.com/user-attachments/assets/d0e6df85-ed6a-4d0b-a30d-acc4e163667d




---

## 📖 What is ReportMind?

**ReportMind** is a command-line research agent that takes a single query, scours the web in real time, synthesizes what it finds, and saves a polished Markdown report — all automatically.

It combines the speed of **Groq's inference engine**, the reasoning of **LLaMA 3.3 70B**, and the search power of **Tavily** into a single, fast pipeline. No manual browsing. No copy-pasting. Just ask and get a report.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Real-Time Web Search** | Searches up to 5 live sources per query via Tavily |
| 🧠 **LLaMA 3.3 70B Reasoning** | State-of-the-art open model hosted on Groq for near-instant inference |
| 📄 **Auto Report Generation** | Reports saved as timestamped `.md` files in a `reports/` folder |
| 🎨 **Rich Terminal UI** | Beautiful progress bars, tables, and styled output via Rich |
| ⚡ **CLI-First Design** | Pass queries directly or enter them interactively |
| 🔧 **Verbose Mode** | Inspect every reasoning step and tool call with `--verbose` |
| 🌍 **Cross-Platform** | Works on Windows, macOS, and Linux |

---

## 🎬 Demo

```
$ python reportmind.py "Latest breakthroughs in quantum computing 2025"

  ✓ Agent initialized
  ✓ Search completed          ████████████████ 100%
  ✓ Analysis completed
  ✓ Report generated

  ╔══════════════════════════════════════════════╗
  ║  ✅ Report successfully generated!           ║
  ║  reports/Report_2025-06-10_14-32-01.md       ║
  ╚══════════════════════════════════════════════╝
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     ReportMind CLI                      │
│                   (reportmind.py)                       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              LangGraph ReAct Agent                      │
│         (Orchestrates reasoning + tool use)             │
└──────────────┬──────────────────────┬───────────────────┘
               │                      │
               ▼                      ▼
┌─────────────────────┐   ┌───────────────────────────────┐
│   Groq Inference    │   │       Tavily Search API        │
│  LLaMA 3.3 70B      │   │  (Real-time web retrieval)     │
│  (Ultra-fast LLM)   │   │  Up to 5 results per query    │
└─────────────────────┘   └───────────────────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  reports/Report_     │
              │  YYYY-MM-DD_HH.md   │
              └──────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+**
- A **Groq API key** → [Get one free](https://console.groq.com)
- A **Tavily API key** → [Get one free](https://tavily.com)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/mohamedatr1/ReportMind.git
cd ReportMind

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API keys
cp .env.example .env
```

Edit `.env` and fill in your keys:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### Dependencies

```
langchain-groq
langchain-community
langgraph
tavily-python
rich
colorama
python-dotenv
```

---

## 💻 Usage

### Interactive Mode

```bash
python reportmind.py
```

You'll be prompted to enter your query in a styled terminal interface.

### Direct Query Mode

```bash
python reportmind.py "Impact of AI on the job market in 2025"
```

### Verbose Mode (see reasoning steps)

```bash
python reportmind.py "Best open-source LLMs right now" --verbose
```

### Examples

```bash
# Research a topic
python reportmind.py "State of renewable energy adoption globally"

# Competitive analysis
python reportmind.py "Compare GPT-4o vs Claude 3.5 vs Gemini 1.5 capabilities"

# News research
python reportmind.py "Latest developments in the Israel-Hamas conflict"

# Technical deep-dive
python reportmind.py "How does Retrieval Augmented Generation work in production"
```

---

## 📁 Project Structure

```
ReportMind/
├── reportmind.py        # Main entry point
├── .env.example         # Environment variable template
├── requirements.txt     # Python dependencies
├── reports/             # Auto-created; stores generated reports
│   └── Report_YYYY-MM-DD_HH-MM-SS.md
└── README.md
```

---

## ⚙️ Configuration

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Groq API key for LLaMA inference | ✅ |
| `TAVILY_API_KEY` | Tavily API key for web search | ✅ |

You can also adjust `max_results` in `TavilySearchResults(max_results=5)` to control how many web sources are retrieved per query.

---

## 🛣️ Roadmap

- [ ] Support for custom output formats (PDF, DOCX)
- [ ] Multi-query batch processing
- [ ] Configurable LLM models and temperatures
- [ ] Web UI via Streamlit or Gradio
- [ ] Report templates (executive summary, technical brief, news digest)
- [ ] Source citation formatting (APA, MLA)
- [ ] Slack / email report delivery integration

---

## 🤝 Contributing

Contributions are welcome. Here's how to get involved:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please keep pull requests focused and well-described. Open an issue first for large changes.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com) — Agent orchestration framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) — ReAct agent runtime
- [Groq](https://groq.com) — Ultra-fast LLM inference
- [Tavily](https://tavily.com) — Search API built for AI agents
- [Rich](https://github.com/Textualize/rich) — Terminal formatting

---

<div align="center">

Made with focus and care by [@mohamedatr1](https://github.com/mohamedatr1)

⭐ **Star this repo if it saved you time** ⭐

</div>
