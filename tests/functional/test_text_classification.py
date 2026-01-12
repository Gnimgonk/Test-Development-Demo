"""
文本分类功能测试
测试AI模型的文本分类功能
"""
import pytest
import sys
from pathlib import Path

# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# from models.ai_model_client import AIModelClient


class TestTextClassification:
    """文本分类测试类"""
    
    # def setup_method(self):
    #     """测试前置准备"""
    #     self.client = AIModelClient(model_name="classification_model")
    
    def test_single_classification(self, model_client):
        """测试单个文本分类"""
        text = "这是一条科技新闻"
        categories = ["科技", "体育", "娱乐", "财经"]
        
        result = model_client.text_classification(text, categories)
        
        assert "predicted_category" in result
        assert result["predicted_category"] in categories
        assert "category_scores" in result
        assert len(result["category_scores"]) == len(categories)
    
    def test_category_scores(self, model_client):
        """测试分类分数"""
        text = "测试文本"
        categories = ["类别1", "类别2", "类别3"]
        
        result = model_client.text_classification(text, categories)
        
        # 验证所有类别都有分数
        for category in categories:
            assert category in result["category_scores"]
            score = result["category_scores"][category]
            assert 0 <= score <= 1, f"分数应在[0,1]范围内，实际值: {score}"
    
    def test_empty_categories(self, model_client):
        """测试空分类列表"""
        text = "测试文本"
        categories = []
        
        result = model_client.text_classification(text, categories)
        assert "error" in result
        assert result["error"] == "分类列表不能为空"
        # assert "category_scores" in result
        # assert len(result["category_scores"]) == 0
    
    def test_model_info(self, model_client):
        """测试模型信息"""
        info = model_client.get_model_info()
        
        assert info["model_name"] == "test_model"
        assert "call_count" in info
        assert info["status"] == "active"
