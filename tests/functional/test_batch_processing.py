"""
批量处理功能测试
测试AI模型的批量处理功能
"""
import pytest
import sys
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient


class TestBatchProcessing:
    """批量处理测试类"""
    
    # def setup_method(self):
    #     """测试前置准备"""
    #     self.client = AIModelClient(model_name="batch_model")
    
    def test_batch_sentiment_analysis(self, model_client, sample_texts):
        """测试批量情感分析"""
        # texts = [
        #     "我很喜欢",
        #     "我很讨厌",
        #     "一般般"
        # ]
        
        results = model_client.batch_process(sample_texts, operation="sentiment")
        
        assert len(results) == len(sample_texts)
        for i, result in enumerate(results):
            assert "sentiment" in result
            assert result["text"] == sample_texts[i]
    
    def test_empty_batch(self, model_client):
        """测试空批量处理"""
        results = model_client.batch_process([], operation="sentiment")
        assert len(results) == 0
    
    def test_large_batch(self, model_client):
        """测试大批量处理"""
        texts = [f"测试文本{i}" for i in range(100)]
        results = model_client.batch_process(texts, operation="sentiment")
        
        assert len(results) == 100
        for result in results:
            assert "sentiment" in result or "error" in result
    
    def test_batch_consistency(self, model_client):
        """测试批量处理的一致性"""
        text = "测试文本"
        texts = [text] * 10
        
        results = model_client.batch_process(texts, operation="sentiment")
        
        # 验证所有结果都有相同的文本
        for result in results:
            assert result["text"] == text
