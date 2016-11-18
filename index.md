
makrdown-css
=========

Markdown-css 是一个命令行工具，用来把 css 样式转换成 html 内联样式。


# 为什么是 markdown-css ？

可能吧的阿禅的在[可能吧的文章是如何排版的？](http://mp.weixin.qq.com/s?__biz=MjM5ODQwMjA4MA==&mid=2649293603&idx=1&sn=57f38200555dcba76d6358594416c089&mpshare=1&scene=1&srcid=1106ssUPcBWLZUq7D9vqXEkj#rd)中介绍了他是如何排版公众号文章的。思路就是用 markdown 写作，然后使用专门的工具导出为 html 文件，最后把自定义的样式应用到导出的文件，复制粘贴内容到微信公众号。想要自定义样式在微信公众号起作用，这些样式必须是内联的 `inline-style`，所以才有了 `markdown-css`。

markdown-css  可以一键把 css 样式转换成内联样式，并输出 html 文件，就像这样:

```shell
mkdir public
markdown-css demo.html --style=style.css
```

默认生成同名的 html 文件并存放在当前目录的 public 中，双击用浏览器打开输出的文件，然后复制粘贴到公众号的编辑中，一次自定义排版就完成了。

# 如何使用


markdown-css  是用 Python 编写的，想要使用 markdown-css，最好在 linux 或 mac 系统下，这些系统都自带了 Python，很容易安装。


## 安装

在 macOS 中安装


```shell
xcode-select --install
pip install markdown-css
```

在 Ubuntu 中安装


```shell
apt-get install libxml2-dev libxslt1-dev python-dev
apt-get install python-lxml
pip install markdown-css
```

markdown-css 没有在 windows 下测试过，为了获得最佳体验，最好使用 macOS 和 linux。


## 使用

安装完 markdown-css，打开终端，键入 `markdown-css -h` 查看是否正确安装。虽然 markdown-css 提供一键转换的功能，但是那些漂亮的 css 还是需要自己去编写的。如果你不太懂，可以请教一下身边的程序员同学，如果你身边没有可爱的程序员，请把你的使用情况反馈给我们。


# 注意事项


1. 大多数 markdown 写作工具都支持导出 html 文件，为了让自定义样式充分发挥作用，最好导出的是无样式 html 文件，[typora](http://www.typora.io/) 这款 markdown 工具就支持。

2. makrdown-css 现在只支持非常简单的 css 选择器，但对于 markdown 文件导出的 html 来说已经足够了，具体见 [Doc](https://github.com/wecatch/markdown-css#selector)。


# 反馈

- 在 github 提 issue 给我们反馈 [issues](https://github.com/wecatch/markdown-css/issues)
- 发邮件给我们 wecatch.me@gmail.com

