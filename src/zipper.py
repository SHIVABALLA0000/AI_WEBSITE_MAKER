import io
import zipfile

def create_zip(html, css, js):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zipf:
        zipf.writestr("index.html", html)
        zipf.writestr("style.css", css)
        zipf.writestr("script.js", js)
    return buffer.getvalue()
