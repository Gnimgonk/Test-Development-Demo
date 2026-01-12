"""
响应时间性能测试
测试AI模型的响应时间性能
"""
import pytest
import time
import sys
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient


class TestResponseTime:
    """响应时间测试类"""
    
    def setup_method(self):
        """测试前置准备"""
        # self.client = AIModelClient()
        self.max_response_time = 1.0  # 最大响应时间（秒）
    
    def test_single_request_time(self, model_client):
        """测试单个请求的响应时间"""
        start_time = time.time()
        model_client.sentiment_analysis("测试文本")
        end_time = time.time()
        
        response_time = end_time - start_time
        assert response_time < self.max_response_time, \
            f"响应时间 {response_time:.2f}s 超过阈值 {self.max_response_time}s"
    
    def test_average_response_time(self, model_client):
        """测试平均响应时间"""
        texts = ["测试文本"] * 10
        response_times = []
        
        for text in texts:
            start_time = time.time()
            model_client.sentiment_analysis(text)
            end_time = time.time()
            response_times.append(end_time - start_time)
        
        avg_time = sum(response_times) / len(response_times)
        assert avg_time < self.max_response_time, \
            f"平均响应时间 {avg_time:.2f}s 超过阈值 {self.max_response_time}s"
    
    def test_batch_processing_time(self, model_client):
        """测试批量处理的响应时间"""
        texts = ["测试文本"] * 50
        
        start_time = time.time()
        model_client.batch_process(texts, operation="sentiment")
        end_time = time.time()
        
        total_time = end_time - start_time
        avg_time_per_item = total_time / len(texts)
        
        # 批量处理时，每个项目的平均时间应该更短
        assert avg_time_per_item < self.max_response_time, \
            f"批量处理平均时间 {avg_time_per_item:.2f}s 超过阈值"
    
    @pytest.mark.parametrize("text_length", [10, 100, 1000])
    def test_response_time_by_text_length(self, model_client, text_length):
        """测试不同文本长度的响应时间"""
        text = "测试" * text_length
        
        start_time = time.time()
        model_client.sentiment_analysis(text)
        end_time = time.time()
        
        response_time = end_time - start_time
        # 对于长文本，允许更长的响应时间
        max_time = self.max_response_time * (1 + text_length / 1000)
        assert response_time < max_time, \
            f"响应时间 {response_time:.2f}s 超过阈值 {max_time:.2f}s"
