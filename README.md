# 🤖➡️👤 AI Humanizer

> Transform AI-generated text into authentic, human-like content that bypasses AI detection systems.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Required-green.svg)](https://ollama.ai/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/Mohit1053/Humanizer)](https://github.com/Mohit1053/Humanizer/issues)
[![GitHub Stars](https://img.shields.io/github/stars/Mohit1053/Humanizer)](https://github.com/Mohit1053/Humanizer/stargazers)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 📋 Overview

AI Humanizer is a powerful tool that transforms AI-generated text into natural, human-sounding content. Built on research findings about what bypasses AI detectors in 2025, it focuses on:

- **Perplexity variation** - Unpredictable word choices
- **Burstiness** - Mixing short and long sentences dramatically
- **Human quirks** - Contractions, filler words, incomplete thoughts
- **Emotional authenticity** - Personal voice and natural speech patterns

## ✨ Features

- 🎯 **High Success Rate** - Designed to achieve <10% AI detection scores
- 🔄 **Batch Processing** - Process entire CSV files efficiently
- 💾 **Resume Support** - Continue from where you left off if interrupted
- 🧪 **Testing Scripts** - Verify your setup before full runs
- 📊 **Progress Tracking** - Real-time progress bars with tqdm
- 🎨 **Multiple Prompt Versions** - Optimized prompts for different use cases

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Ollama** installed and running ([Download here](https://ollama.ai/))
3. **Llama3 model** pulled in Ollama

```powershell
# Install Ollama, then run:
ollama pull llama3:8b
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mohit1053/Humanizer.git
cd Humanizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Verify your setup:
```bash
python test_humanizer.py
```

## 📖 Usage

### Basic Usage

1. **Quick Test (5 samples)**
   ```bash
   python test_humanizer.py
   ```
   Test the humanizer on 5 sample rows to verify everything works.

2. **Generate Test Samples**
   ```bash
   python generate_test_samples.py
   ```
   Creates formatted samples ready for AI detection testing.

3. **Full CSV Processing**
   ```bash
   python humanize_v2.py
   ```
   Process your entire CSV file with humanized text.

### Configuration

Edit the configuration section in any script:

```python
# Input/Output
INPUT_CSV = "your_input_file.csv"
OUTPUT_CSV = "your_output_file.csv"

# Model Settings
MODEL = 'llama3:8b'
BATCH_SIZE = 50

# Processing
START_ROW = 0  # Resume from a specific row
DELAY_MIN = 0.5  # Rate limiting
DELAY_MAX = 1.0
```

## 📁 Project Structure

```
Humanizer/
├── humanize_v2.py              # Main humanizer script (optimized)
├── test_humanizer.py           # Quick test script (5 samples)
├── generate_test_samples.py    # Generate formatted test samples
├── generate_samples.py         # Alternative sample generator
├── quick_test.py              # Quick testing utilities
├── single_test.py             # Test single text transformation
├── optimize_prompts.py        # Prompt optimization experiments
├── humanize_csv.py            # Legacy version
├── final_pledges_merged.csv   # Sample input data
├── test_results.csv           # Test output results
├── TEST_SAMPLES_READY.md      # Pre-generated test samples
└── README.md                  # This file
```

## 🧪 Testing AI Detection

After humanizing your text, test it at:

- [GPTZero](https://gptzero.me/) - Goal: <10% AI detection
- [ZeroGPT](https://zerogpt.com/) - Goal: <10% AI detection

See [TEST_SAMPLES_READY.md](TEST_SAMPLES_READY.md) for pre-generated samples ready for testing.

## 🎯 How It Works

The humanizer uses carefully crafted prompts that instruct the LLM to:

1. **Preserve exact emotional meaning** - Keep the core message intact
2. **Add natural speech patterns** - "honestly", "like", "you know", "I mean"
3. **Use heavy contractions** - I'm, can't, won't, it's, that's, don't
4. **Mix sentence lengths** - Very short (3-5 words) to long rambling ones
5. **Sound conversational** - Like venting to a close friend
6. **Include self-doubt** - Natural human uncertainty

### Example Transformation

**Original (AI-generated):**
> Surgery prep is torture, thinking through every step as if it's my final test. Each incision, each stitch might mean life or death.

**Humanized:**
> Honestly, prep for surgery is just brutal, you know? Like, I'm literally thinking through every single step like it's my final exam or something. Each incision, each stitch - I mean, what if I mess up and someone dies on the table?

## 📊 Performance

- **Processing Speed**: ~50 rows per minute (with rate limiting)
- **AI Detection Score**: Typically 0-10% on GPTZero and ZeroGPT
- **Batch Efficiency**: Resume capability prevents data loss
- **Model Used**: Llama3 8B (free, runs locally)

## 🛠️ Scripts Overview

| Script | Purpose | Use When |
|--------|---------|----------|
| `test_humanizer.py` | Quick 5-row test | First-time setup verification |
| `humanize_v2.py` | Main production script | Processing full datasets |
| `generate_test_samples.py` | Create test samples | Need samples for AI detector testing |
| `single_test.py` | Test single text | Experimenting with individual texts |
| `optimize_prompts.py` | Prompt experiments | Developing new prompt versions |

## 🔧 Troubleshooting

### Ollama Not Found
```bash
# Check if Ollama is running
ollama list

# Start Ollama service if needed
ollama serve
```

### Model Not Installed
```bash
# Pull the required model
ollama pull llama3:8b

# Verify installation
ollama list
```

### CSV Processing Errors
- Check CSV file path is correct
- Ensure the pledge column name matches your CSV
- Try testing with `test_humanizer.py` first

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Share prompt improvements

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:
- How to fork and set up the project
- Code style guidelines
- Commit message format
- Pull request process

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and research purposes. Always ensure your use case complies with relevant terms of service and ethical guidelines.

## 🙏 Acknowledgments

- Built with [Ollama](https://ollama.ai/) for local LLM inference
- Uses Meta's [Llama3](https://ai.meta.com/llama/) model
- Research-based approach to AI detection bypassing

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

Made with ❤️ by [Mohit1053](https://github.com/Mohit1053)
