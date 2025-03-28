#!/usr/bin/env python3
import re

# 权限修复步骤模板
permission_fix_step = '''      - name: Fix permissions for run-on-arch
        run: |
          chmod +x .github/set-permissions.sh
          .github/set-permissions.sh
'''

# 读取工作流文件
with open('.github/workflows/flutter-build.yml', 'r') as f:
    content = f.read()

# 在每个run-on-arch-action之前添加权限修复步骤
pattern = r'(\s+- uses: rustdesk-org/run-on-arch-action@amd64-support)'
replacement = f'\n{permission_fix_step}\\1'
modified_content = re.sub(pattern, replacement, content)

# 写回文件
with open('.github/workflows/flutter-build.yml', 'w') as f:
    f.write(modified_content)

print("已成功修改工作流文件，在每个run-on-arch-action之前添加权限修复步骤。") 