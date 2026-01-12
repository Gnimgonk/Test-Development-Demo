# 使用指南

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

#### 运行所有测试
```bash
pytest
```

#### 运行功能测试
```bash
pytest tests/functional/ -v
```

#### 运行性能测试
```bash
pytest tests/performance/ -v
```

#### 生成HTML测试报告
```bash
pytest --html=reports/report.html --self-contained-html
```

#### 使用便捷脚本运行
```bash
python run_tests.py
python run_tests.py --html  # 生成HTML报告
```

## 测试用例说明

### 功能测试

#### 1. 情感分析测试 (`test_sentiment_analysis.py`)
- ✅ 正面情感识别
- ✅ 负面情感识别
- ✅ 中性情感识别
- ✅ 参数化测试
- ✅ 边界值测试（空文本、长文本）
- ✅ 数据驱动测试
- ✅ 响应结构验证
- ✅ 置信度范围验证

#### 2. 文本分类测试 (`test_text_classification.py`)
- ✅ 单文本分类
- ✅ 分类分数验证
- ❌ 空分类列表处理
- ✅ 模型信息获取

#### 3. 批量处理测试 (`test_batch_processing.py`)
- ✅ 批量情感分析
- ✅ 空批量处理
- ✅ 大批量处理
- ✅ 批量处理一致性

### 性能测试

#### 1. 响应时间测试 (`test_response_time.py`)
- ✅ 单请求响应时间
- ✅ 平均响应时间
- ✅ 批量处理响应时间
- ✅ 不同文本长度的响应时间

#### 2. 吞吐量测试 (`test_throughput.py`)
- ❌ 顺序处理吞吐量 
- ❌ 批量处理吞吐量
- ✅ 并发请求吞吐量

#### 3. 稳定性测试 (`test_stability.py`)
- ✅ 重复调用稳定性
- ✅ 模型状态一致性
- ✅ 错误处理

## 测试用例设计方法

本项目采用了以下测试用例设计方法：

### 1. 等价类划分
将输入数据分为有效等价类和无效等价类：
- 有效等价类：正常的情感文本
- 无效等价类：空字符串、超长文本等

### 2. 边界值分析
测试输入数据的边界条件：
- 空字符串
- 超长文本（1000字符以上）
- 最短文本（单个字符）

### 3. 错误推测
基于经验设计错误场景：
- 混合情感的文本
- 特殊字符处理
- 并发访问场景

### 4. 场景测试
真实业务场景的端到端测试：
- 批量处理场景
- 高并发场景
- 长时间运行场景

## 扩展开发

### 添加新的测试用例

1. 在相应的测试目录下创建新的测试文件
2. 继承测试基类或使用pytest fixtures
3. 编写测试方法（以`test_`开头）

示例：
```python
def test_new_feature():
    """测试新功能"""
    client = AIModelClient()
    result = client.new_method("input")
    assert result["status"] == "success"
```

### 添加新的测试数据

1. 在`data/`目录下创建JSON文件
2. 使用`TestDataManager`加载数据
3. 在测试中使用数据驱动测试

示例：
```python
def test_with_data(data_manager):
    test_data = data_manager.load_test_data("new_test_data.json")
    for case in test_data:
        # 执行测试
        pass
```

## CI/CD

项目已配置GitHub Actions自动测试：

1. 代码推送到main/master/develop分支时自动触发
2. 支持多个Python版本（3.8, 3.9, 3.10, 3.11）
3. 自动生成测试报告
4. 测试结果作为Artifact保存

## 测试报告

测试报告包含：
- 测试执行概览
- 通过的测试用例
- 失败的测试用例
- 错误信息和堆栈追踪
- 执行时间统计

查看报告：
```bash
# 在浏览器中打开
open reports/report.html  # macOS
xdg-open reports/report.html  # Linux
start reports/report.html  # Windows
```
