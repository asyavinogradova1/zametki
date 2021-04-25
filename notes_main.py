#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QInputDialog,QWidget,QHBoxLayout, QVBoxLayout,QLabel, QPushButton,QTextEdit
from PyQt5.QtWidgets import QRadioButton,QGroupBox,QListWidget,QLineEdit
import json 


a={
    "заметка 1":{
        "текст":"тут что то должно быть",
        "теги":["тек1","тег2"]}
}
def create_notes():
    new_win,tmp=QInputDialog.getText(win,"test1","test2")
    a[new_win]=dict()
    a[new_win] ["текст"]=text_note.toPlainText()
    a[new_win] ["теги"]=[]
    zametki.clear()
    zametki.addItems(a)
    with open ("basa.json","w", encoding='utf-8')as file:
        json.dump(a,file,ensure_ascii=False)

def show_note():
    s=zametki.selectedItems()[0].text()
    text_note.setText(a[s]["текст"])
    teg_list.clear()
    teg_list.addItems(a[s]["теги"])

def del_note():
        if len(zametki.selectedItems()) >0:
                s=zametki.selectedItems()[0].text()
                del a[s]
                zametki.clear()
                zametki.addItems(a)
                with open ("basa.json","w", encoding='utf-8')as file:
                        json.dump(a,file,ensure_ascii=False)
        else:
                print("Кушать то что?")

def save_note():
        if len(zametki.selectedItems()) >0:
                s=zametki.selectedItems()[0].text()
                a[s] ["текст"] = text_note.toPlainText()

                with open ("basa.json","w", encoding='utf-8')as file:
                        json.dump(a,file,ensure_ascii=False)
        else:
                print("сохранить куда?? то что?")

#with open ("basa.json","r", encoding='utf-8')as file:
#   a=json.load(file)

app=QApplication([])
win=QWidget()
main_line = QHBoxLayout()
thrird_line=QHBoxLayout() 

push = QPushButton("сохранить приготовленную заметку")
push.clicked.connect(save_note)
create_push=QPushButton("приготовить заметку")
create_push.clicked.connect(create_notes)
dell_push=QPushButton("скушать заметку")
dell_push.clicked.connect(del_note)
thrird_line.addWidget(create_push)
thrird_line.addWidget(dell_push)




second_line=QVBoxLayout()
text_note=QTextEdit()
zametki=QListWidget()
zametki.addItems(a)
zametki.itemClicked.connect(show_note)
teg_list=QListWidget()

main_line.addWidget(text_note)
main_line.addLayout(second_line)
banana=QLabel("Холодильник")
second_line.addWidget(banana)
second_line.addWidget(zametki) 
second_line.addLayout(thrird_line)
second_line.addWidget(push)
grape=QLabel("Список съедобных  тегов")
second_line.addWidget(grape)
second_line.addWidget(teg_list)
teg_imput=QLineEdit("Введи теги")
second_line.addWidget(teg_imput)
four_line = QHBoxLayout()
second_line.addLayout(four_line)
addteg = QPushButton("Добавить тег к заметке")
dellteg = QPushButton(" Открепить тег  от заметки")
four_line.addWidget(addteg)
four_line.addWidget(dellteg)
find_note = QPushButton("Искать заметку по тегу")
second_line.addWidget(find_note)



win.setLayout(main_line)
win.show()
app.exec()
