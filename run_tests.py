#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试运行脚本
提供便捷的测试执行入口
"""
import sys
import pytest
from pathlib import Path


def main():
    """主函数"""
    # 添加src目录到Python路径  
    src_path = Path(__file__).parent / "src"
    sys.path.insert(0, str(src_path))
    
    # pytest参数
    args = [
        "tests/",
        "-v",  # 详细输出
        "--tb=short",  # 简短的错误追踪
        "-s",  # 显示print输出
    ]
    
    # 如果指定了报告参数，生成HTML报告
    if "--html" in sys.argv or "-h" in sys.argv:
        # 检查pytest-html是否可用
        try:
            import pytest_html
        except ImportError:
            print("=" * 60)
            print("错误: pytest-html 插件未安装")
            print("=" * 60)
            print("\n请运行以下命令安装:")
            print("  python -m pip install pytest-html")
            print("\n或者重新安装所有依赖:")
            print("  python -m pip install -r requirements.txt")
            print("\n注意: 如果直接使用 pip 报路径错误，请使用 python -m pip")
            print("\n或者使用文本报告（无需额外插件）:")
            print("  pytest -v --tb=short > reports/test_report.txt")
            print("\n详细说明请查看: FIX_HTML_REPORT.md")
            print("=" * 60)
            sys.exit(1)
        
        report_dir = Path("reports")
        report_dir.mkdir(exist_ok=True)
        args.extend([
            "--html=reports/report.html",
            "--self-contained-html"
        ])
    
    # 运行pytest
    exit_code = pytest.main(args)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
