"""
AI模型客户端封装
模拟AI模型API接口，用于测试
"""
from typing import Dict, List, Any
import time
import random


class AIModelClient:
    """AI模型客户端，封装模型调用逻辑"""
    
    def __init__(self, model_name: str = "default"):
        self.model_name = model_name
        self.call_count = 0
    
    def sentiment_analysis(self, text: str) -> Dict[str, Any]:
        """
        情感分析
        
        Args:
            text: 待分析文本
        
        Returns:
            分析结果字典
        """
        # 模拟API调用延迟
        time.sleep(random.uniform(0.1, 0.5))
        self.call_count += 1
        
        # 简单的模拟逻辑（实际项目中调用真实API）
        positive_keywords = ["喜欢", "好", "棒", "优秀", "满意", "推荐"]
        negative_keywords = ["讨厌", "差", "糟糕", "失望", "不推荐"]
        
        text_lower = text.lower()
        positive_count = sum(1 for kw in positive_keywords if kw in text_lower)
        negative_count = sum(1 for kw in negative_keywords if kw in text_lower)
        
        if positive_count > negative_count:
            sentiment = "positive"
            confidence = min(0.9, 0.5 + positive_count * 0.1)
        elif negative_count > positive_count:
            sentiment = "negative"
            confidence = min(0.9, 0.5 + negative_count * 0.1)
        else:
            sentiment = "neutral"
            confidence = 0.6
        
        return {
            "text": text,
            "sentiment": sentiment,
            "confidence": round(confidence, 2),
            "model": self.model_name
        }
    
    def text_classification(self, text: str, categories: List[str]) -> Dict[str, Any]:
        """
        文本分类
        
        Args:
            text: 待分类文本
            categories: 分类类别列表
        
        Returns:
            分类结果
        """
        time.sleep(random.uniform(0.1, 0.3))
        self.call_count += 1
        
        # 模拟分类逻辑
        category_scores = {}
        for category in categories:
            category_scores[category] = round(random.uniform(0.1, 0.95), 2)
        
        predicted_category = max(category_scores, key=category_scores.get)
        
        return {
            "text": text,
            "predicted_category": predicted_category,
            "category_scores": category_scores,
            "model": self.model_name
        }
    
    def batch_process(self, texts: List[str], operation: str = "sentiment") -> List[Dict[str, Any]]:
        """
        批量处理
        
        Args:
            texts: 文本列表
            operation: 操作类型
        
        Returns:
            处理结果列表
        """
        results = []
        for text in texts:
            if operation == "sentiment":
                result = self.sentiment_analysis(text)
            else:
                result = {"text": text, "error": "Unknown operation"}
            results.append(result)
        return results
    
    def get_model_info(self) -> Dict[str, Any]:
        """获取模型信息"""
        return {
            "model_name": self.model_name,
            "call_count": self.call_count,
            "status": "active"
        }
