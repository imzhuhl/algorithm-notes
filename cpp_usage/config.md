# C++ 配置

vscode c++ 配置

## build

自动编译 c++ 文件，配置 tasks.json，Linux g++ 为例：

```json
"version": "2.0.0",
"tasks": [
    {
        "type": "shell",
        "label": "g++ build for debug",
        "command": "/usr/bin/g++",
        "args": ["-std=c++11", "-g", "${file}", "-o", "${fileDirname}/${fileBasenameNoExtension}.out"],
        "options": {
            "cwd": "${workspaceFolder}"
        },
        "problemMatcher": ["$gcc"],
        "group": {
            "kind": "build",
            "isDefault": true  // use ctrl+shift+B to build
        },
    },
    {
        "type": "shell",
        "label": "g++ build for run",
        "command": "/usr/bin/g++",
        "args": ["-std=c++11", "${file}", "-o", "${fileDirname}/${fileBasenameNoExtension}.out"],
        "options": {
            "cwd": "${workspaceFolder}"
        },
        "problemMatcher": ["$gcc"],
        "group": {
            "kind": "build",
            "isDefault": true  // use ctrl+shift+B to build
        },
    },
],
```

第一个 task 使用 -g 参数，为了后续的调试。

## debug

debug 需要配置 launch.json 文件：

```json
"version": "0.2.0",
"configurations": [
    {
        "name": "C++ build & debug",
        "type": "cppdbg",
        "request": "launch",
        "program": "${fileDirname}/${fileBasenameNoExtension}.out",
        "args": [],
        "environment": [],
        "cwd": "${workspaceFolder}",
        "MIMode": "gdb",
        "setupCommands": [
            {
                "description": "Enable pretty-printing for gdb",
                "text": "-enable-pretty-printing",
                "ignoreFailures": true
            }
        ],
        "preLaunchTask": "g++ build for debug",  // tasks.json label
    }
]

```
