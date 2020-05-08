# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то
# HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая,
#т. е не через img = Image(), а через фабричный метод или фабрику, например factory.create_tag(name).»


#рожитель
class Tag(object):
    def show(self):
        pass

#тег изображение
class Image(Tag):
    def show(self):
        print('<img></img>')

    def shatr(self):
        print('<img src=""></img>')

#текст
class Text(Tag):
    def show(self):
        print('<p></p>')

    def shatr(self):
        print('<p align=""></p>')

#ссылка
class Link(Tag):
    def show(self):
        print('<a></a>')

    def shatr(self):
        print('<a href=""></a>')

#
class Input(Tag):
    def show(self):
        print('<input></input>')

    def shatr(self):
        print('<input value=""></input>')




class CreateTag:
    def gethtml(self, type_):
        if type_ == 'image' or type_ == 'src':
            return Image()
        elif type_ == 'input' or type_ == 'val':
            return Input()
        elif type_ == 'text' or type_ == 'al':
            return Text()
        elif type_ == 'link' or type_ == 'href':
            return Link()


html = CreateTag()
html.gethtml('src').shatr()
html.gethtml('input').show()
html.gethtml('al').shatr()
html.gethtml('link').show()
html.gethtml('href').shatr()

