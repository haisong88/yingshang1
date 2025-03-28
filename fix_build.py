#!/usr/bin/env python3

"""
修复build.py文件中的语法错误和重复代码
"""

def fix_build_file():
    with open('build.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 查找并修复错误
    fixed_lines = []
    skip_next_else = False
    skip_duplicate_block = False
    
    for i, line in enumerate(lines):
        # 跳过多余的else块
        if skip_next_else and line.strip() == 'else:':
            skip_next_else = False
            continue
        
        # 当检测到第二个 chmod 行时，标记跳过下一个else
        if '确保所有的脚本都有执行权限' in line and i > 630:
            skip_next_else = True
        
        # 跳过重复的代码块
        if skip_duplicate_block and 'cp -a DEBIAN/* tmpdeb/DEBIAN/' in line:
            skip_duplicate_block = False
            continue
        
        # 当检测到重复的代码块开始时，标记跳过
        if 'cp -a DEBIAN/* tmpdeb/DEBIAN/' in line and i > 630:
            skip_duplicate_block = True
            continue
        
        if not skip_duplicate_block:
            fixed_lines.append(line)
    
    # 写回文件
    with open('build.py', 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print("修复完成！")

if __name__ == "__main__":
    fix_build_file() 