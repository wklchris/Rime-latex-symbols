# 用于 Rime 的 LaTeX 符号输入配置

*author: wklchris@github*

配置 <input-schema>.custom.yaml 文件来在 [RIME 输入法](https://rime.im/) 中使用 LaTeX 数学符号。

支持的符号：

- 常用数学符号，包括几何、微积分。
- 被 LaTeX 主数学宏包 amsmath/amssymb 支持的一些常用符号：
  * 运算符与关系符
  * 箭头符号
- 希腊字母与罗马数字
- 少量其他符号

## 使用方法

此处以 Windows 上的微软双拼 RIME（小狼毫 Weasel）用户为例：

1. 首先，将本文件复制到 RIME 程序文件夹下的 data 目录中：`RIME/weasel-0.xx/data`。

   或者，可以将本文件复制到同步盘，并用符号链接的形式来指向。这样的好处是可以在多个设备上同步该 yaml 文件的更改。例子：
   a. 复制文件到 Onedrive 下的 `Sync-Misc\Rime` 文件夹（示例）。该路径可以自定义。
   b. 以管理员身份运行 Powershell，并切换目录到 Rime 程序文件夹下的 `data` 子文件夹：
      ```
      cd "C:\MyApps\Rime\weasel-0.14.3\data"
      ```
   c. 创建一个指向在步骤 a 中复制到 Onedrive 的符号链接：
      ```
      New-Item -ItemType SymbolicLink -Path latexmath.yaml -Target "${env:onedrive}\Sync-Misc\Rime\latexmath.yaml"
      ```
2. 打开用户文件夹下的 custom 文件 'double_pinyin_mspy.custom.yaml'，更新键值：
   ```
   patch:
     punctuator/import_preset: latexmath
     recognizer/patterns:
       punct: "^/([0-9]0?|[A-Za-z]+)$"
   ```
3. 右键点击托盘区的 RIME 图标，点击“重新部署”以应用更改。

## 贡献与许可证

本配置的部分内容来自官方 Weasel 项目部署后的默认 data/symbols.yaml 文件。

许可证：[GPLv3](./LICENSE)
