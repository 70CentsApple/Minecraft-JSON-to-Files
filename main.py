import os.path
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from ui_mainwindow import Ui_Main
import resource


class Converter(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.obj_path = None
        self.json_path = None
        self.out_path = None

        self.bt_obj.clicked.connect(self.select_obj)
        self.bt_json.clicked.connect(self.select_json)
        self.bt_out.clicked.connect(self.select_out)
        self.bt_start.clicked.connect(self.start)

    def select_obj(self):
        self.obj_path = QFileDialog.getExistingDirectory(caption='选择objects文件夹', filter='objects')
        if self.obj_path:
            self.lb_obj.setText('已选择ヾ(≧▽≦*)o')
            print("Selected obj path:", self.obj_path)
            if os.path.basename(self.obj_path) != 'objects':
                QMessageBox.warning(self, '小问题', '您刚选择的文件夹名称不为objects，\n这是有意而为之吗？若确保无误请选择忽略\n您也可以再次进行选择(●\'◡\'●)')

    def select_json(self):
        self.json_path = QFileDialog.getOpenFileName(caption='选择Minecraft版本json文件', filter='*.json')[0]
        if self.json_path:
            self.lb_json.setText('已选择φ(゜▽゜*)♪')
            print("Selected json file:", self.json_path)
            import json
            with open(self.json_path, 'r') as f:
                info = json.load(f)
                print("Json File:", info)

                # 计算文件预计大小
                count = 0
                for key in list(info['objects'].keys()):
                    count += info['objects'][key]['size']
                self.lb_disk.setText('预计所需磁盘空间：{}字节({}MB)-(°▽°*)'.format(count, int(count / 1048576)))

    def select_out(self):
        self.out_path = QFileDialog.getExistingDirectory(caption='选择输出文件夹')
        self.lb_path.setText(self.out_path)
        print("Selected export path:", self.out_path)

    def start(self):
        # QMessageBox.warning(self, '请注意：', '卡顿为正常现象，请务关闭程序( •̀ ω •́ )✧\n点击OK继续(´▽`ʃ♡ƪ)')
        self.lb_disk.setText('卡顿为正常现象，请勿关闭程序(·̀ ω·́ )✧')
        QApplication.processEvents()  # 分配多个线程
        with open(self.json_path, 'r') as f:
            import json
            info = json.load(f)
            for key in list(info['objects'].keys()):
                hsh = info['objects'][key]['hash']
                file = key
                # print('From ', self.obj_path + '/' + hsh[0] + hsh[1] + '/' + hsh, '\n',
                #       ' To ', self.out_path + '/' + file)

                source = self.obj_path + '/' + hsh[0] + hsh[1] + '/' + hsh
                target = self.out_path + '/' + file

                from shutil import copyfile
                if not os.path.exists(self.out_path + '/' + os.path.dirname(file)):
                    os.makedirs(self.out_path + '/' + os.path.dirname(file))
                copyfile(source, target)
            # QMessageBox.information(self, '完成！', '好东西就要来了ㄟ(≧V≦)ㄏ', button='打开文件位置')

            msg_box = QMessageBox(self)
            msg_box.setWindowTitle('完成！')
            msg_box.setText('好东西就要来了ㄟ(≧V≦)ㄏ')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_yes = msg_box.button(QMessageBox.Yes)
            button_yes.setText('打开文件夹')
            button_no = msg_box.button(QMessageBox.No)
            button_no.setText('关闭对话框')
            msg_box.exec_()

            if msg_box.clickedButton() == button_yes:
                os.system("start explorer {}".format(self.out_path.replace('/', '\\')))  # 打开文件夹


if __name__ == '__main__':
    from sys import argv, exit
    app = QApplication(argv)
    window = Converter()
    exit(app.exec_())
