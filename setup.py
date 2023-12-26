```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="SentimentAnalyzer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python-based tool for text sentiment analysis using OpenAI's language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SentimentAnalyzer",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```
