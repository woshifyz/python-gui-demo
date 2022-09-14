import os
import webview

from time import time


class Api(object):
    def fullscreen(self):
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def open_file_dialog(self):
        file_types = ('All files (*.*)',)
        result = webview.windows[0].create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)
        return result

    def ls(self):
        return os.listdir('.')


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../gui/index.html'):  # unfrozen development
        return '../gui/index.html'

    if exists('../Resources/gui/index.html'):  # frozen py2app
        return '../Resources/gui/index.html'

    if exists('./gui/index.html'):
        return './gui/index.html'

    raise Exception('No index.html found')


entry = get_entrypoint()

if __name__ == '__main__':
    s = webview.screens[0]
    window = webview.create_window('First App', entry, js_api=Api(),
                                   width=s.width * 0.9, height=s.height * 0.9)
    #webview.start(debug=True)
    webview.start(debug=False)
