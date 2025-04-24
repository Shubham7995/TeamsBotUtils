from setuptools import setup, find_packages

setup(
    name="teams_bot_utils",
    version="1.0.5",  # Increment version for new features
    description="Text and content extraction from various file types including images",
    author="Shubham Shinde",
    author_email="shubham.shinde@ecolab.com",
    url="https://ecolabinstitutional.visualstudio.com/Enterprise%20Copilot%20Platform/_artifacts/feed/CopilotSystem/PyPI/teams_bot_utils/overview/1.0.5",
    packages=find_packages(),
    install_requires=[
        "mixpanel",
        "httpx>=0.24.0",
        "botbuilder-core",
        "pydantic",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "black",
            "mypy",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
