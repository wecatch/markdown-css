from setuptools import setup, find_packages
import os


version = __import__('markdown_css').version

install_requires = [

]

for k in ['docopt', 'cssutils', 'pyquery']:
    try:
        __import__(k)
    except ImportError:
        install_requires.append(k)

kwargs = {}

readme_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(readme_path, 'README.rst')) as f:
    kwargs['long_description'] = f.read()

setup(
    name="markdown-css",
    version=version,
    author="sanyuesha",
    author_email="wecatch.me@gmail.com",
    url="http://github.com/wecatch/markdown-css",
    license="https://opensource.org/licenses/MIT",
    description="Markdown-css is a command tool to convert css style to markdown inline-style",
    keywords='markdown-css markdown css weixin',
    packages=find_packages(),
    install_requires=install_requires,
    scripts=['markdown_css/bin/markdown-css'],
    **kwargs
)
