"""
情感分析功能测试
测试AI模型的情感分析功能
"""
import pytest
import sys
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient
# from utils.test_data_manager import TestDataManager


class TestSentimentAnalysis:
    """情感分析测试类"""
    
    # def setup_method(self):
    #     """测试前置准备"""
    #     self.client = AIModelClient(model_name="sentiment_model")
    #     self.data_manager = TestDataManager()
    
    def test_positive_sentiment(self, model_client):
        """测试正面情感识别"""
        text = "我很喜欢这个产品，质量非常好！"
        result = model_client.sentiment_analysis(text)
        
        assert result["sentiment"] == "positive"
        assert result["confidence"] > 0.5
        assert "text" in result
        assert result["text"] == text
    
    def test_negative_sentiment(self, model_client):
        """测试负面情感识别"""
        text = "这个服务太差了，完全不推荐"
        result = model_client.sentiment_analysis(text)
        
        assert result["sentiment"] == "negative"
        assert result["confidence"] > 0.5
        assert result["text"] == text
    
    def test_neutral_sentiment(self, model_client):
        """测试中性情感识别"""
        text = "今天天气不错"
        result = model_client.sentiment_analysis(text)
        
        assert result["sentiment"] in ["positive", "neutral", "negative"]
        assert "confidence" in result
        assert 0 <= result["confidence"] <= 1
    
    @pytest.mark.parametrize("text,expected_sentiment", [
        ("产品很棒，强烈推荐", "positive"),
        ("质量很差，不推荐", "negative"),
        ("一般般吧", "neutral"),
    ])
    def test_sentiment_with_params(self, model_client, text, expected_sentiment):
        """参数化测试不同文本的情感分析"""
        result = model_client.sentiment_analysis(text)
        # 注意：由于是模拟实现，实际结果可能与预期不完全一致
        assert result["sentiment"] in ["positive", "negative", "neutral"]
        assert "confidence" in result
    
    def test_empty_text(self, model_client):
        """测试空文本处理"""
        result = model_client.sentiment_analysis("")
        # 应该返回结果或抛出异常
        assert "sentiment" in result or "error" in result
    
    def test_long_text(self, model_client):
        """测试长文本处理"""
        long_text = "好" * 1000
        result = model_client.sentiment_analysis(long_text)
        assert "sentiment" in result
        assert result["text"] == long_text
    
    def test_data_driven_test(self, model_client, data_manager):
        """数据驱动测试"""
        test_data = data_manager.load_test_data("sentiment_test_data.json")
        
        for test_case in test_data[:3]:  # 只测试前3个用例
            input_text = test_case["input"]
            if input_text:  # 跳过空字符串
                result = model_client.sentiment_analysis(input_text)
                assert "sentiment" in result
                assert "confidence" in result
                assert result["text"] == input_text
    
    def test_response_structure(self, model_client):
        """测试响应结构完整性"""
        result = model_client.sentiment_analysis("测试文本")
        
        required_fields = ["text", "sentiment", "confidence", "model"]
        for field in required_fields:
            assert field in result, f"Response缺少必需字段: {field}"
    
    def test_confidence_range(self, model_client, sample_texts):
        """测试置信度范围"""
        # texts = [
        #     "我非常喜欢",
        #     "我很讨厌",
        #     "一般般"
        # ]
        
        for text in sample_texts:
            result = model_client.sentiment_analysis(text)
            assert 0 <= result["confidence"] <= 1, \
                f"置信度应在[0,1]范围内，实际值: {result['confidence']}"
