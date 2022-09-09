from os import listdir, remove, path, makedirs
from barcode import Code128
from barcode.writer import ImageWriter
from datetime import datetime

from app.config import Settings


class BarCoder:

    folder: str = Settings.folder
    options: dict = Settings.options

    def __init__(self, numbers: tuple, report_type: str = None):
        self.numbers = numbers
        self.report_type = report_type
        if not path.exists(self.folder):
            makedirs(self.folder)

    def create(self):
        writer = ImageWriter()
        try:
            for n in self.numbers:
                my_code = Code128(n, writer=writer)
                my_code.save(filename=f'{self.folder}{n}', options=self.options)
            return f"{len(self.numbers)} ШТРИХ-КОДА(ОВ) СГЕНЕРИРОВАНЫ И ПОМЕЩЕНЫ В ПАПКУ \"{self.folder}\"!<br>" \
                   f" Отчет добавлен в \"{self.folder}inner_report.txt\""
        except Exception as e:
            print(f"Exception error: {e}")
            return f"Exception error: {e}"

    def clear_folder(self):
        filelist = [f for f in listdir(self.folder) if f.endswith(".png")]

        for f in filelist:
            remove(path.join(self.folder, f))

    def report(self):
        with open("inner_report.txt", 'a') as f:
            data_obj = '\n' + '\n'.join(str(num) for num in self.numbers)
            final_str = f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}{data_obj}"
            final_str += '\n\n'
            f.write(final_str)
