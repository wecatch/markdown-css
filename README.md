makrdown-css
=========

Markdown css is a command tool to convert css style into markdown inline style.

## Getting started

```bash
pip install markdown-css
mkdir public
touch style.css
markdown -h
markdown-css pub.html --style=style.css --out=public/
```

## Selector

markdown-css support css selector like these:

*element selector*

```css
p {
    margin: 10px 0;
}
```


*multi element selector*

```css
h1,p,h2,pre {
    color: #333;
}
```

*all element*

```css
* {
    font-size: 14px
}
```

