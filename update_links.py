#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新所有HTML文件中的about-us.html和final-project.html链接
移动到 assets/about-us/index.html 和 assets/final-project/index.html
"""

import os
import re

# 需要更新的文件列表
files_to_update = [
    'index.html',
    'assets/dailyhomework/index.html',
    'assets/dailyhomework/assignment-0/index.html',
    'assets/dailyhomework/assignment-1/index.html',
    'assets/dailyhomework/assignment-2/index.html',
    'assets/dailyhomework/assignment-3/index.html',
    'assets/dailyhomework/assignment-4/index.html',
    'assets/about-us/index.html',  # 移动后的about-us页面
    'assets/final-project/index.html',  # 移动后的final-project页面
]

# 链接替换规则
replacements = [
    # index.html (根目录) -> assets/about-us/index.html 和 assets/final-project/index.html
    (r'href="about-us\.html"', 'href="assets/about-us/index.html"'),
    (r'href="final-project\.html"', 'href="assets/final-project/index.html"'),
    
    # assets/dailyhomework/index.html (深2层) -> ../../assets/about-us/index.html
    (r'href="\.\./\.\./about-us\.html"', 'href="../../assets/about-us/index.html"'),
    (r'href="\.\./\.\./final-project\.html"', 'href="../../assets/final-project/index.html"'),
    
    # assets/dailyhomework/assignment-X/index.html (深3层) -> ../../../assets/about-us/index.html
    (r'href="\.\./\.\./\.\./about-us\.html"', 'href="../../../assets/about-us/index.html"'),
    (r'href="\.\./\.\./\.\./final-project\.html"', 'href="../../../assets/final-project/index.html"'),
    
    # assets/about-us/index.html 内部链接 -> 同级 final-project/index.html
    (r'href="final-project\.html"', 'href="../final-project/index.html"'),
    
    # assets/final-project/index.html 内部链接 -> 同级 about-us/index.html
    (r'href="about-us\.html"', 'href="../about-us/index.html"'),
]

def update_file(file_path):
    """更新单个文件中的链接"""
    if not os.path.exists(file_path):
        print(f"⚠️  文件不存在: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 已更新: {file_path}")
        return True
    else:
        print(f"ℹ️  无需更新: {file_path}")
        return False

def main():
    print("开始更新链接...\n")
    
    updated_count = 0
    for file_path in files_to_update:
        if update_file(file_path):
            updated_count += 1
    
    print(f"\n✅ 完成！共更新了 {updated_count} 个文件")

if __name__ == '__main__':
    main()
