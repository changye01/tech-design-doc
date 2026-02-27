#!/usr/bin/env python3
"""检查技术设计文档的完整性"""

import sys
import re

REQUIRED_SECTIONS = [
    "背景",
    "方案设计",
    "接口定义",
    "实现计划"
]

def validate(filepath: str) -> list[str]:
    """验证文档，返回缺失的章节列表"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 - {filepath}")
        sys.exit(2)
    except Exception as e:
        print(f"错误：无法读取文件 - {e}")
        sys.exit(2)

    missing = []
    for section in REQUIRED_SECTIONS:
        # 匹配 ## 背景 或 ## 1. 背景 或 ## 一、背景 等格式
        pattern = rf'^##\s*(\d+\.|\S、)?\s*{section}'
        if not re.search(pattern, content, re.MULTILINE):
            missing.append(section)

    return missing

def main():
    if len(sys.argv) != 2:
        print("用法: python validate_doc.py <文档路径>")
        print("示例: python validate_doc.py my-feature-design.md")
        sys.exit(1)

    filepath = sys.argv[1]
    missing = validate(filepath)

    if missing:
        print(f"❌ 文档不完整，缺少以下章节：")
        for section in missing:
            print(f"   - {section}")
        sys.exit(1)
    else:
        print("✅ 文档结构完整，包含所有必需章节")
        sys.exit(0)

if __name__ == "__main__":
    main()
