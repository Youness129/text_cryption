import flet as ft

def main(page: ft.Page):
    page.title = "txtCryption V0.1"
    page.overlay.append(ft.Text(value="Devloped by Youness Ben Daoud",bottom=5, right=5, theme_style="bodySmall", color="red300"))

    def copy_text(e):
        page.set_clipboard(open("txt.txt", "r").read())
        page.update()

    def btn_click(e):
        a = None
        b = None

        try:
            KEY = int(key.value)
            a = True
        except:
            key.error_text = "integer please"
            a = False
            page.update()
            
        if not txt.value:
            txt.error_text = "please inter text"
            b = False
            page.update()
        else:
            TXT = txt.value
            b = True

        if a and b:
            page.clean()

            encryption_text = []
            for i in range(len(TXT)):
                encryption_text.append( chr( ord(TXT[i]) - KEY ) )
            encryption_text_str = ""
            for i in encryption_text:
                encryption_text_str += i
            encryption_text_file = open("txt.txt", "w")
            encryption_text_file.write(encryption_text_str)
            encryption_text_file.close()

            page.add(ft.IconButton(icon="copy", on_click=copy_text), ft.Text(encryption_text_str))

    txt = ft.TextField(label="inter text")
    key = ft.TextField(label="inter key")
    

    page.add(txt, key, ft.ElevatedButton("cryption", on_click=btn_click))


if __name__ == "__main__":
    ft.app(main)
