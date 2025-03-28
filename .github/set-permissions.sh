#!/bin/bash

# 解决GitHub Actions运行时可能出现的权限问题
# 该脚本在run-on-arch-action之前运行

# 设置git safe.directory以避免"dubious ownership"错误
git config --global --add safe.directory "*"

# 确保所有文件都有执行权限
chmod -R 755 .

# 特别确保脚本有执行权限
find . -name "*.sh" -exec chmod +x {} \;

echo "权限已设置完成"
ls -la 