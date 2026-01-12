"""
pytest配置文件
定义测试的共享fixtures和配置
"""
import pytest
import sys
from pathlib import Path

# 添加src目录到Python路径
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from models.ai_model_client import AIModelClient
from utils.test_data_manager import TestDataManager


@pytest.fixture() # function scope
def model_client():
    """创建AI模型客户端实例"""
    return AIModelClient(model_name="test_model")


@pytest.fixture(scope="session")
def data_manager():
    """创建测试数据管理器实例"""
    manager = TestDataManager()
    # 生成测试数据文件
    sentiment_data = manager.generate_sentiment_test_data()
    manager.save_test_data("sentiment_test_data.json", sentiment_data)
    return manager


@pytest.fixture
def sample_texts():
    """提供示例文本数据"""
    return [
        "我很喜欢这个产品",
        "这个服务太差了",
        "今天天气不错"
    ]


@pytest.fixture
def cleanup():
    """清理fixture"""
    yield
    # 清理操作可以在这里添加
    pass
