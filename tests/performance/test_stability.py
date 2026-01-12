"""
稳定性测试
测试AI模型的稳定性
"""
import pytest
import sys
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient


class TestStability:
    """稳定性测试类"""
    
    # def setup_method(self):
    #     """测试前置准备"""
    #     self.client = AIModelClient()
    
    def test_repeated_calls(self, model_client):
        """测试重复调用的稳定性"""
        text = "测试文本"
        results = []
        
        # 重复调用100次
        for _ in range(100):
            result = model_client.sentiment_analysis(text)
            results.append(result)
        
        # 验证所有调用都成功
        assert len(results) == 100
        for result in results:
            assert "sentiment" in result
            assert "confidence" in result
    
    def test_model_state_consistency(self, model_client):
        """测试模型状态一致性"""
        initial_info = model_client.get_model_info()
        initial_count = initial_info["call_count"]
        
        # 执行多次调用
        for _ in range(10):
            model_client.sentiment_analysis("测试")
        
        final_info = model_client.get_model_info()
        final_count = final_info["call_count"]
        
        # 验证调用计数正确
        assert final_count == initial_count + 10
    
    def test_error_handling(self, model_client):
        """测试错误处理"""
        # 测试各种边界情况
        test_cases = [
            "",  # 空字符串
            "a" * 10000,  # 超长字符串
            "测试" * 1000,  # 长文本
        ]
        
        for text in test_cases:
            result = model_client.sentiment_analysis(text)
            # 应该返回结果或合理的错误处理
            assert isinstance(result, dict)
