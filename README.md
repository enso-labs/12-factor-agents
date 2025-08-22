# 🧪 12-Factor Agents

> Collection of AI Agent examples to weigh various framework benefits

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Contributors](https://img.shields.io/github/contributors/enso-labs/12-factor-agents)](https://github.com/enso-labs/12-factor-agents/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/enso-labs/12-factor-agents)](https://github.com/enso-labs/12-factor-agents/network/members)
[![Stars](https://img.shields.io/github/stars/enso-labs/12-factor-agents)](https://github.com/enso-labs/12-factor-agents/stargazers)

A comprehensive monorepo showcasing different AI agent frameworks and their capabilities. Perfect for developers looking to compare **LangGraph**, **hand-rolled solutions**, and other agent architectures in production-ready examples.

## 🚀 Why This Repository?

As AI agent frameworks rapidly evolve in 2025, choosing the right one for your project can be challenging. This repository provides:

- **Framework Comparison**: Side-by-side implementations using different approaches
- **Production Examples**: Real-world agent patterns, not just tutorials
- **12-Factor Compliance**: Scalable, maintainable architectures following industry best practices
- **Performance Insights**: Understand the trade-offs between different frameworks

## 🎯 Quick Start

```bash
# Clone the repository
git clone https://github.com/enso-labs/12-factor-agents.git
cd 12-factor-agents

# Update submodules
make update-submodules

# Choose your framework and follow the setup guide below
```

## 🏗️ Agent Examples

### 🌊 LangGraph Agent
**Location**: [`examples/langchain/langgraph_agent/`](examples/langchain/langgraph_agent/)

A state-based workflow agent demonstrating **LangGraph's** graph-based architecture:
- **Stateful Workflows**: Graph-based execution with conditional routing
- **Tool Integration**: Weather and stock price APIs with error handling
- **Streaming Responses**: Real-time output with Redis caching
- **Persistence Layer**: Built-in memory and fault tolerance

**Best For**: Complex multi-step tasks requiring precise control and state management

```bash
cd examples/langchain/langgraph_agent
uv sync
python src/langgraph_agent/main.py
```

### ⚡ Next.js Agent
**Location**: [`examples/nextjs/simple-af-agent/`](examples/nextjs/simple-af-agent/)

A hand-rolled agent implementation built with **Next.js 15** showcasing custom agent logic:
- **Streaming UI**: Real-time response generation with optimistic updates
- **Multi-Tool Execution**: Handle multiple API calls in parallel
- **Memory Management**: XML-based conversation context
- **Custom Classification**: Intent recognition without heavy frameworks

**Best For**: High-performance web applications with custom agent requirements

```bash
cd examples/nextjs/simple-af-agent
npm install
echo "OPENAI_API_KEY=your_key" > .env.local
npm run dev
```

### 🖥️ Terminal Agent
**Location**: [`examples/terminal/gilfoyle/`](examples/terminal/gilfoyle/)

A lightweight CLI agent built with **Ink** for terminal-based interactions:
- **Terminal UI**: Rich command-line interface with React components
- **Fast Startup**: Minimal dependencies for quick agent deployment
- **Cross-Platform**: Works on Windows, macOS, and Linux

**Best For**: Developer tools, automation scripts, and lightweight deployments

```bash
cd examples/terminal/gilfoyle
npm install
npm start
```

## 📊 Framework Comparison

| **Feature** | **LangGraph** | **Next.js (Hand-rolled)** | **Terminal (Ink)** |
|-------------|---------------|-------------------------|-------------------|
| **Learning Curve** | High | Medium | Low |
| **Control Level** | Precise | Full | Simple |
| **Performance** | Medium | High | High |
| **Streaming** | ✅ | ✅ | ⚠️ |
| **State Management** | Built-in | Custom | Minimal |
| **Tool Integration** | Framework | Custom | Basic |
| **Memory/Persistence** | Redis/Built-in | XML/Custom | In-memory |
| **Web Interface** | ❌ | ✅ | ❌ |
| **CLI Interface** | ⚠️ | ❌ | ✅ |
| **Production Ready** | ✅ | ✅ | ⚠️ |

## 🛠️ Development Setup

### Prerequisites

- **Node.js 18+** (for Next.js and Terminal agents)
- **Python 3.12+** (for LangGraph agent)
- **Redis** (for LangGraph persistence)
- **OpenAI API Key** (for AI functionality)

### Development Commands

```bash
# Update all submodules
make update-submodules

# Individual project setup
cd examples/[framework]/[project-name]
# Follow framework-specific setup in each directory
```

## 🏗️ Architecture Principles

All implementations follow the [12-factor app methodology](https://12factor.net/) ensuring:

- **📦 Dependencies**: Explicitly declared with lock files (`package-lock.json`, `uv.lock`)
- **⚙️ Config**: Environment variables for API keys and settings
- **🔌 Backing Services**: External APIs treated as attached resources
- **🚀 Processes**: Stateless execution with external state management
- **📝 Logs**: Structured logging to stdout/stderr
- **🔄 Disposability**: Graceful shutdown and fast startup

## 🎯 When to Use Each Framework

### Choose **LangGraph** when:
- Building complex, multi-step agent workflows
- Need built-in persistence and fault tolerance
- Require sophisticated state management
- Want framework-provided agent abstractions

### Choose **Hand-rolled (Next.js)** when:
- Need maximum performance and control
- Building web-based agent interfaces
- Require custom agent logic not supported by frameworks
- Want to minimize dependencies and framework overhead

### Choose **Terminal (Ink)** when:
- Building developer tools or CLI utilities
- Need lightweight, fast agent deployment
- Targeting terminal-based workflows
- Want simple, focused agent interactions

## 🚀 Monorepo Structure

```
12-factor-agents/
├── examples/
│   ├── langchain/
│   │   └── langgraph_agent/     # LangGraph implementation
│   ├── nextjs/
│   │   └── simple-af-agent/     # Next.js hand-rolled agent
│   └── terminal/
│       └── gilfoyle/            # Terminal CLI agent
├── Makefile                     # Monorepo automation
├── .gitmodules                  # Submodule configuration
└── README.md                    # This comprehensive guide
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### 🎯 Ways to Contribute

- **📝 Add New Framework Examples**: Implement agents using CrewAI, AutoGen, Semantic Kernel, etc.
- **🔧 Improve Existing Examples**: Enhance performance, add features, or fix bugs
- **📚 Documentation**: Improve setup guides, add tutorials, or create comparison docs
- **🐛 Bug Reports**: Find and report issues with clear reproduction steps
- **💡 Feature Requests**: Suggest new agent patterns or framework integrations

### 🚀 Development Workflow

1. **Fork** the repository and clone your fork
2. **Create** a feature branch: `git checkout -b feature/new-framework-example`
3. **Develop** your changes following our patterns:
   - Follow 12-factor app principles
   - Add comprehensive README for new examples
   - Include setup scripts and clear documentation
4. **Test** your implementation thoroughly
5. **Submit** a pull request with detailed description

### 📋 Guidelines for New Agent Examples

When adding a new framework implementation:

- **📁 Directory Structure**: `examples/[framework-category]/[project-name]/`
- **📝 Documentation**: Include comprehensive README with setup instructions
- **🔧 12-Factor Compliance**: Follow environment config, dependency management
- **🎯 Feature Parity**: Implement similar functionality to existing examples for comparison
- **⚡ Performance**: Consider streaming, tool integration, and memory management

### 💻 Local Development

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/12-factor-agents.git
cd 12-factor-agents

# Update submodules
make update-submodules

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
# Submit PR when ready
```

## 🌟 Community & Growth

### 📈 Project Stats

[![GitHub stars](https://img.shields.io/github/stars/enso-labs/12-factor-agents?style=social)](https://github.com/enso-labs/12-factor-agents)
[![GitHub forks](https://img.shields.io/github/forks/enso-labs/12-factor-agents?style=social)](https://github.com/enso-labs/12-factor-agents/network/members)
[![GitHub issues](https://img.shields.io/github/issues/enso-labs/12-factor-agents)](https://github.com/enso-labs/12-factor-agents/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/enso-labs/12-factor-agents)](https://github.com/enso-labs/12-factor-agents/pulls)

### 🎉 Recognition

⭐ **Star this repo** if it helps with your agent development!  
🍴 **Fork it** to create your own agent examples  
🔄 **Share it** with developers exploring AI agent frameworks

## 🛡️ Environment Variables

Each project uses environment variables for secure configuration:

| Variable | Required | Description | Used By |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | ✅ | OpenAI API access | All examples |
| `REDIS_URL` | ⚠️ | Redis connection | LangGraph |
| `DEBUG` | ❌ | Enable debug logging | All examples |
| `API_PORT` | ❌ | Custom port binding | Web examples |

> 💡 See individual project READMEs for framework-specific configuration

## 📚 Resources & Links

### 🔗 Framework Documentation
- [LangGraph Official Docs](https://langchain-ai.github.io/langgraph/)
- [Next.js 15 Documentation](https://nextjs.org/docs)
- [Ink CLI Framework](https://github.com/vadimdemedes/ink)

### 📖 Related Reading
- [12-Factor App Methodology](https://12factor.net/)
- [AI Agent Framework Comparison 2025](https://langwatch.ai/blog/best-ai-agent-frameworks-in-2025-comparing-langgraph-dspy-crewai-agno-and-more)
- [OpenAI Agent SDK](https://platform.openai.com/docs/agents)

## 📄 License

This project is open source and available under the [Apache 2.0 License](LICENSE).

## 💬 Support & Community

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/enso-labs/12-factor-agents/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/enso-labs/12-factor-agents/discussions)
- 📧 **Questions**: Open an issue with the `question` label

---

Built with ❤️ by the **[Enso Labs](https://github.com/enso-labs)** team and amazing contributors