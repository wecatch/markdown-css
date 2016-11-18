#!/usr/bin/env bash

markdown_py index.md -f index.html

filecontent=`cat index.html`

$html_head='<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width">
    <title>markdown-css</title>
</head>
<body>'

$html_end='</body>
</html>'
echo $html_end
# echo $html_head$filecontent$html_end >> index.html

markdown-css index.html --style=simple.css

cp public/index.html .

