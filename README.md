# AI模型质量保障平台

一个基于Python的AI模型自动化测试框架，用于AI平台产品的质量保障和测试流程管理。

## 项目简介

本项目是一个针对AI模型的质量保障平台，实现了完整的测试流程和自动化测试能力，包括功能测试、性能测试、测试用例管理等核心功能。

## 技术栈

- **Python 3.8+**: 主要开发语言
- **pytest**: 测试框架
- **pytest-html**: 测试报告生成
- **requests**: HTTP接口测试
- **pandas**: 测试数据管理
- **GitHub Actions**: CI/CD持续集成

## 项目结构

```
ai-test-platform/
├── tests/                    # 测试用例目录
│   ├── functional/          # 功能测试
│   ├── performance/         # 性能测试
│   └── conftest.py          # pytest配置文件
├── src/                     # 源代码目录
│   ├── framework/           # 测试框架核心
│   ├── models/              # AI模型封装
│   └── utils/               # 工具函数
├── data/                    # 测试数据
├── reports/                 # 测试报告输出
├── .github/
│   └── workflows/           # CI/CD配置
├── requirements.txt         # 依赖包
└── README.md
```

## 功能特性

### 1. 测试流程管理
- 标准化的测试流程（需求评审 → 用例设计 → 执行 → 报告）
- 测试用例管理（数据驱动测试）
- 测试结果追踪

### 2. 功能测试
- AI模型接口功能测试
- 输入验证测试
- 输出结果验证
- 边界值测试

### 3. 性能测试
- 响应时间测试
- 并发性能测试
- 吞吐量测试
- 资源使用监控

### 4. 自动化测试框架
- 基于pytest的测试框架
- 测试数据管理
- 测试报告自动生成
- 失败用例重试机制

## 快速开始

### 环境要求
- Python 3.8+
- pip

### 安装依赖

```bash
python -m pip install -r requirements.txt
```

**注意**: 如果直接使用 `pip install` 报路径错误，请使用 `python -m pip install` 代替。

### 运行测试

```bash
# 运行所有测试
pytest

# 运行功能测试
pytest tests/functional/

# 运行性能测试
pytest tests/performance/

# 生成HTML报告（需要pytest-html插件）
pytest --html=reports/report.html --self-contained-html

# 如果提示 "unrecognized arguments: --html"，请先安装：
# python -m pip install pytest-html

# 如果 pip install 报路径错误，请使用 python -m pip install

# 或者生成文本报告（无需额外插件）
pytest tests/ -v --tb=short > reports/test_report.txt
```

## 使用示例

### 功能测试示例

```python
def test_sentiment_analysis_positive():
    """测试情感分析-正面情感"""
    result = analyze_sentiment("我很喜欢这个产品")
    assert result['sentiment'] == 'positive'
    assert result['confidence'] > 0.8
```

### 性能测试示例

```python
def test_response_time():
    """测试响应时间"""
    response_time = measure_response_time(api_endpoint, test_data)
    assert response_time < 1.0  # 响应时间应小于1秒
```

## CI/CD

项目配置了GitHub Actions，实现自动化测试：
- 代码提交自动触发测试
- 测试报告自动生成
- 测试结果通知

## 测试用例设计方法

项目采用了以下测试用例设计方法：
1. **等价类划分**: 将输入数据分为有效和无效等价类
2. **边界值分析**: 测试输入数据的边界条件
3. **错误推测**: 基于经验的错误场景测试
4. **场景测试**: 真实业务场景的端到端测试

## 项目亮点

1. ✅ 完整的测试流程和自动化测试框架
2. ✅ AI模型专项测试（功能测试、性能测试）
3. ✅ 基于pytest的现代化测试框架
4. ✅ CI/CD持续集成配置
5. ✅ 清晰的测试用例设计和文档
6. ✅ 测试报告自动生成

## 测试覆盖

- **功能测试**: 覆盖AI模型的核心功能（情感分析、文本分类、批量处理）
- **性能测试**: 覆盖响应时间、吞吐量、稳定性测试
- **测试用例设计**: 采用等价类划分、边界值分析、错误推测、场景测试等方法
- **数据驱动测试**: 支持从JSON文件加载测试数据

## 项目特点

### 针对职位要求的设计

1. **测试流程和自动化测试** ✅
   - 完整的测试框架结构
   - 标准化的测试流程
   - 自动化测试执行

2. **AI平台产品测试** ✅
   - 针对AI模型的专项测试
   - 功能测试和性能测试
   - 批量处理和并发测试

3. **测试用例设计** ✅
   - 多种测试用例设计方法
   - 数据驱动测试
   - 参数化测试

4. **工具平台和框架开发** ✅
   - 可复用的测试框架
   - 测试工具封装
   - 测试数据管理

5. **CI/CD** ✅
   - GitHub Actions配置
   - 自动化测试流程
   - 多版本Python支持

## 技术实现亮点

- 使用pytest现代化测试框架
- 模块化设计，代码结构清晰
- 支持数据驱动测试
- 性能测试覆盖全面
- CI/CD自动化集成
- 详细的文档和使用指南

## 后续扩展建议

1. 集成真实的AI模型API（如OpenAI、百度文心等）
2. 添加更多的性能监控指标
3. 集成测试报告可视化
4. 添加API Mock服务
5. 支持分布式测试执行

## 作者

曹孔明
