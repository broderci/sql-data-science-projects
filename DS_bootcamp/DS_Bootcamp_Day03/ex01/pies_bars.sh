#!/bin/bash
pip install termgraph 

if [ -f "data.txt" ]; then
    termgraph data.txt --color {green,magenta} --space-between
else
    echo "Файл data.txt не найден!"
    exit 1
fi