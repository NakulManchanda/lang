# Environment

## python

## pyenv

```
brew install pyenv
pyenv install 3.10
pyenv versions
export PATH="$PATH:~/.pyenv/versions/3.10.11/bin"
pyenv global 3.10.11
```

## pipenv

```
pip install --user pipenv
pipenv shell
# pipenv install including dev packages
pipenv install -d  
```

## python debug

python debug statement

```
python -m debugpy --listen 0.0.0.0:5678 extending-chatgpt/11_chroma-gettingstarted.py
```

## Git LFS
brew install git-lfs
git lfs install
git lfs track "*.png"
git lfs track "*.pdf"


# Random LLM Samples Hands-on

## Register for private keys
- OpenAI - credit card required
- HuggingFace - free
- SERP - free

## Lang Chain Starter Guide Samples
https://python.langchain.com/en/latest/getting_started/getting_started.html

## PDF Q&A
https://towardsdatascience.com/4-ways-of-question-answering-in-langchain-188c6707cc5a
https://github.com/sophiamyang/tutorials-LangChain/blob/main/LangChain_QA.ipynb
- raw
- using vector db - chroma
- using vectorindexer for retreival
- conversational with history

## Hugging Face Transformer Agents
- https://colab.research.google.com/drive/1c7MHD-T1forUPGcC_jlwsIptOzpG3hSj
- https://towardsdatascience.com/hugging-face-transformers-agent-3a01cf3669ac
- Agents can use LLM prompt, to decide on tooling, generate & run code all. 
- HF transformer use well transformer models to perform a task, compare to LangChain tools - they use all external APIs 