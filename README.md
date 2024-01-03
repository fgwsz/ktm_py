# ktm(keyboard to mouse)
使用键盘快捷键来模拟鼠标操作（适用于Windows/MacOs/Linux操作系统）。
开启本应用之后，会在终端窗口中实时显示用户输入的全局键盘信息和应用调试信息，
并实时将键盘快捷键映射为对应的鼠标操作。

# 安装
因用户系统环境可能存在差异，本项目不发布可执行文件，
需用户安装环境依赖，自行构建可执行文件。  
所需环境依赖：  
`python3`  
`pynput`  
`pyautogui`  
`pyinstaller`  

## pyinstaller 构建
鼠标左键双击`pyinstaller_build.ps1`构建生成可执行文件并运行。

# 鼠标移动/滚轮滑动距离
默认鼠标移动/滚轮滑动距离为32个像素，
也就是说默认情况下，每一次鼠标移动/每一次鼠标滚轮滑动的距离为32个像素。
可以通过快捷键来实时增加/减少此距离。

# 键盘快捷键说明
如下快捷键均表示：按住`LeftAlt`键的情况下再按一次某个键。

注意：`LeftAlt`键指的是空格键左边的Alt键；字母键不区分大小写，大小写通用。

`LeftAlt H` 鼠标向左移动

`LeftAlt J` 鼠标向下移动

`LeftAlt K` 鼠标向上移动

`LeftAlt L` 鼠标向右移动

`LeftAlt O` 鼠标左键单击

`LeftAlt A` 鼠标左键双击

`LeftAlt X` 鼠标右键单击

`LeftAlt B` 鼠标滚轮上滑

`LeftAlt N` 鼠标滚轮下滑

`LeftAlt G` 鼠标左键按下

`LeftAlt I` 鼠标右键按下

`LeftAlt U` 鼠标左/右键松开

`LeftAlt 2` 鼠标移动/滚轮滑动距离翻倍（重复按效果可叠加）

`LeftAlt -` 鼠标移动/滚轮滑动距离减半（重复按效果可叠加，最低削减到1个像素）

`LeftAlt Q` 退出应用程序
