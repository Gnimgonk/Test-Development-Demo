"""
项目安装配置文件
"""
from setuptools import setup, find_packages

setup(
    name="ai-test-platform",
    version="1.0.0",
    description="AI模型质量保障平台",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.4.0",
        "pytest-html>=3.2.0",
        "pytest-xdist>=3.3.1",
        "pytest-rerunfailures>=11.1.2",
        "requests>=2.31.0",
        "pandas>=2.0.3",
        "numpy>=1.24.3",
        "python-dateutil>=2.8.2",
    ],
)
