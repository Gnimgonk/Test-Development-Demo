"""
测试框架基类
提供测试用例的基础功能和通用方法
"""
import time
import json
from typing import Dict, Any, List, Optional
import requests
from abc import ABC, abstractmethod

class TestBase(ABC):
    """测试基类，所有测试用例应继承此类"""
    
    def __init__(self):
        self.base_url = "http://localhost:8000"  # API基础URL
        self.timeout = 30  # 默认超时时间
        self.headers = {
            "Content-Type": "application/json"
        }
    
    def send_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                    headers: Optional[Dict] = None) -> Dict[str, Any]:
        """
        发送HTTP请求
        
        Args:
            method: 请求方法 (GET, POST, PUT, DELETE)
            endpoint: API端点
            data: 请求数据
            headers: 请求头
        
        Returns:
            响应数据字典
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}
        
        try:
            response = requests.request(
                method=method,
                url=url,
                json=data,
                headers=request_headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return {
                "status_code": response.status_code,
                "data": response.json() if response.content else {},
                "headers": dict(response.headers)
            }
        except requests.exceptions.RequestException as e:
            return {
                "status_code": 0,
                "error": str(e),
                "data": {}
            }
    
    def measure_response_time(self, method: str, endpoint: str, 
                             data: Optional[Dict] = None) -> float:
        """
        测量API响应时间
        
        Args:
            method: 请求方法
            endpoint: API端点
            data: 请求数据
        
        Returns:
            响应时间（秒）
        """
        start_time = time.time()
        self.send_request(method, endpoint, data)
        end_time = time.time()
        return end_time - start_time
    
    def assert_status_code(self, response: Dict, expected_code: int):
        """断言状态码"""
        assert response["status_code"] == expected_code, \
            f"Expected status code {expected_code}, got {response['status_code']}"
    
    def assert_field_exists(self, data: Dict, field: str):
        """断言字段存在"""
        assert field in data, f"Field '{field}' not found in response"
    
    def assert_field_value(self, data: Dict, field: str, expected_value: Any):
        """断言字段值"""
        assert field in data, f"Field '{field}' not found"
        assert data[field] == expected_value, \
            f"Expected {field}={expected_value}, got {data[field]}"
    
    @abstractmethod
    def setup(self):
        """测试前置准备"""
        pass
    
    @abstractmethod
    def teardown(self):
        """测试后置清理"""
        pass
