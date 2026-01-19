def parse_response(content: str):
    html = content.split("-html-")[1].split("-css-")[0].strip()
    css = content.split("-css-")[1].split("-js-")[0].strip()
    js = content.split("-js-")[1].strip()
    return html, css, js
