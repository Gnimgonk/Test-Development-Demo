"""
测试数据管理
提供测试数据的生成、加载和管理功能
"""
import json
import os
from typing import List, Dict, Any
from pathlib import Path


class TestDataManager:
    """测试数据管理器"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
    
    def load_test_data(self, filename: str) -> List[Dict[str, Any]]:
        """
        加载测试数据文件
        
        Args:
            filename: 数据文件名
        
        Returns:
            测试数据列表
        """
        filepath = self.data_dir / filename
        if not filepath.exists():
            return []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_test_data(self, filename: str, data: List[Dict[str, Any]]):
        """
        保存测试数据到文件
        
        Args:
            filename: 数据文件名
            data: 测试数据列表
        """
        filepath = self.data_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def generate_sentiment_test_data(self) -> List[Dict[str, Any]]:
        """
        生成情感分析测试数据
        
        Returns:
            测试数据列表
        """
        test_data = [
            {
                "input": "我很喜欢这个产品，质量非常好！",
                "expected_sentiment": "positive",
                "test_case": "正面情感-正常文本"
            },
            {
                "input": "这个服务太差了，完全不推荐",
                "expected_sentiment": "negative",
                "test_case": "负面情感-正常文本"
            },
            {
                "input": "今天天气不错",
                "expected_sentiment": "neutral",
                "test_case": "中性情感-正常文本"
            },
            {
                "input": "",  # 空字符串
                "expected_sentiment": None,
                "test_case": "边界值-空字符串"
            },
            {
                "input": "好" * 1000,  # 超长文本
                "expected_sentiment": "positive",
                "test_case": "边界值-超长文本"
            },
            {
                "input": "我喜欢这个产品，但是价格有点贵",
                "expected_sentiment": "positive",  # 或neutral，取决于模型
                "test_case": "混合情感-复杂文本"
            }
        ]
        return test_data
    
    def generate_performance_test_data(self, count: int = 100) -> List[str]:
        """
        生成性能测试数据
        
        Args:
            count: 数据数量
        
        Returns:
            文本列表
        """
        templates = [
            "这是一个测试文本",
            "产品质量很好",
            "服务态度不错",
            "价格合理",
            "推荐购买"
        ]
        return [f"{template}_{i}" for i in range(count) for template in templates][:count]
