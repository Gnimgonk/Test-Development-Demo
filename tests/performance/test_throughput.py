"""
吞吐量性能测试
测试AI模型的吞吐量性能
"""
import pytest
import time
import sys
import concurrent.futures
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient


class TestThroughput:
    """吞吐量测试类"""
    
    def setup_method(self):
        """测试前置准备"""
        # self.client = AIModelClient()
        self.min_throughput = 10  # 最小吞吐量（请求/秒）
    
    def test_sequential_throughput(self, model_client):
        """测试顺序处理的吞吐量"""
        texts = ["测试文本"] * 50
        
        start_time = time.time()
        for text in texts:
            model_client.sentiment_analysis(text)
        end_time = time.time()
        
        total_time = end_time - start_time
        throughput = len(texts) / total_time
        
        assert throughput >= self.min_throughput, \
            f"顺序处理吞吐量 {throughput:.2f} 请求/秒 低于阈值 {self.min_throughput} 请求/秒"
    
    def test_batch_throughput(self, model_client):
        """测试批量处理的吞吐量"""
        texts = ["测试文本"] * 100
        
        start_time = time.time()
        model_client.batch_process(texts, operation="sentiment")
        end_time = time.time()
        
        total_time = end_time - start_time
        throughput = len(texts) / total_time
        
        # 批量处理应该比顺序处理更高效
        assert throughput >= self.min_throughput, \
            f"批量处理吞吐量 {throughput:.2f} 请求/秒 低于阈值 {self.min_throughput} 请求/秒"
    
    def test_concurrent_requests_simulation(self, model_client):
        """模拟并发请求测试"""
        
        
        texts = ["测试文本"] * 20
        max_workers = 5
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(model_client.sentiment_analysis, text) 
                for text in texts
            ]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
        end_time = time.time()
        
        total_time = end_time - start_time
        throughput = len(texts) / total_time
        
        assert len(results) == len(texts)
        assert throughput >= self.min_throughput / 2, \
            f"并发处理吞吐量 {throughput:.2f} 请求/秒 低于阈值 {self.min_throughput / 2} 请求/秒"
