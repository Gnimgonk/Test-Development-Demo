# 快速开始指南

## 5分钟快速体验

### 步骤1: 安装依赖

```bash
python -m pip install -r requirements.txt
```

**注意1**: 如果直接使用 `pip install` 报路径错误，请使用 `python -m pip install` 代替。

**注意2**: 如果生成HTML报告时出错（提示 `unrecognized arguments: --html`），请确保已安装 `pytest-html`：

```bash
python -m pip install pytest-html
```

或者重新安装所有依赖：

```bash
python -m pip install -r requirements.txt --upgrade
```

### 步骤2: 运行测试

```bash
# 运行所有测试（最简单的方式）
pytest

# 或者使用便捷脚本
python run_tests.py
```

### 步骤3: 查看测试结果

测试会自动执行，你会看到类似以下的输出：

```
tests/functional/test_sentiment_analysis.py::TestSentimentAnalysis::test_positive_sentiment PASSED
tests/functional/test_sentiment_analysis.py::TestSentimentAnalysis::test_negative_sentiment PASSED
...
```

### 步骤4: 生成测试报告（可选）

#### 方式1: HTML报告（需要pytest-html）

```bash
pytest --html=reports/report.html --self-contained-html
```

然后在浏览器中打开 `reports/report.html` 查看详细的测试报告。

**如果遇到错误**: 请先安装 `pytest-html`：
```bash
pip install pytest-html
```

#### 方式2: 文本报告（无需额外插件）

```bash
pytest \tests -v --tb=short > reports/test_report.txt
```

查看文本报告：
```bash
type reports\test_report.txt  # Windows
cat reports/test_report.txt    # Linux/Mac
```

## 项目文件说明

### 核心代码
- `src/framework/test_base.py` - 测试框架基类
- `src/models/ai_model_client.py` - AI模型客户端（模拟）
- `src/utils/test_data_manager.py` - 测试数据管理

### 测试用例
- `tests/functional/` - 功能测试用例
- `tests/performance/` - 性能测试用例

### 配置文件
- `requirements.txt` - Python依赖包
- `.github/workflows/ci.yml` - CI/CD配置

### 文档
- `README.md` - 项目说明
- `USAGE.md` - 详细使用指南
- `PROJECT_SUMMARY.md` - 项目总结和设计思路

## 常见问题

### Q: 测试失败怎么办？
A: 本项目使用模拟的AI模型客户端，所有测试都应该能通过。如果失败，请检查Python版本（需要3.8+）和依赖是否正确安装。

### Q: 生成HTML报告时提示 "unrecognized arguments: --html" 怎么办？
A: 这是因为 `pytest-html` 插件没有安装。请运行：
```bash
python -m pip install pytest-html
```
或者使用文本报告方式（见步骤4的方式2）。

### Q: 如何修改测试用例？
A: 在 `tests/functional/` 或 `tests/performance/` 目录下找到对应的测试文件，按照pytest规范修改即可。

### Q: 如何添加新的测试？
A: 参考现有的测试文件，创建新的测试文件，使用 `test_` 开头的函数名即可。

## 下一步

1. 阅读 `USAGE.md` 了解详细使用方法
2. 阅读 `PROJECT_SUMMARY.md` 了解项目设计思路
3. 查看代码，理解测试框架的设计
4. 尝试添加自己的测试用例
