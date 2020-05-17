# 2 class Editor-> ProEditor

# Editor:     view_document, edit_document -> print()
# ProEditor:  edit_document

# main() (if main...) =>
#     key = licence input
#     if key=licence (QS47DX-KJS7)
#         editor = Pro()
#     else
#         editor = free()

#     view_document
#     edit_document

class Editor:

    def view_document(self):
        print('view document')

    def edit_document(self):
        print('free version editor')


class ProEditor(Editor):

    def edit_document(self):
        print('full editor')


def main():
    key = input('Enter license key: ')
    if key == 'QS47DX-KJS7':
        print('Product activated.')
        editor = ProEditor()
    else:
        print('Incorrect license key, free version.')
        editor = Editor()

    editor.view_document()
    editor.edit_document()

if __name__ == '__main__':
    main()