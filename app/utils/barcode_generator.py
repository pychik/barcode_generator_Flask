
from os import getcwd, listdir, remove, path
from barcode import Code128
from barcode.writer import ImageWriter
from datetime import datetime


folder = f'{getcwd()}/generated/'
options = dict(module_width=0.3, module_height=10, quiet_zone=2,text_distance=3,
               font_size=8, center_text=True)  
# font_type = ImageFont.truetype("arial.ttf", 18)

# barcode.writer.FONT = os.path.join("D:\PyCharm\\untitled1", 'DejaVuSansMono.ttf')

def get_numbers(filename):
    with open(filename,'r') as f:
        numbers_list = f.read().split('\n')[:-1]
        return numbers_list

def creator(numbers):
    writer = ImageWriter()
    # writer.FONT = f'{os.getcwd()}/DejaVuSansMono.ttf'
    try:
        for n in numbers:
            my_code = Code128(n, writer=writer)
            my_code.save(f'{folder}{n}',options)
    except Exception as e:
        print(f"Exception error: {e}")

def clear_folder():
    filelist = [ f for f in listdir(folder) if f.endswith(".png") ]
    
    for f in filelist:
       remove(path.join(folder, f))

def report(numbers):
    with open("inner_report.txt", 'a') as f:
        data_obj = '\n' + '\n'.join(str(num) for num in numbers)
        final_str = f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}{data_obj}"
        final_str += '\n\n'
        f.write(final_str)
        


def make_mes(message: str):
    return f"    ##{'#'*len(message)}##\n    # {message} #\n    ##{'#'*len(message)}##"
# def print_barcodes(numbers):
#     for n in numbers:
#         os.startfile(f"{n}.png", "print") 


if __name__== '__main__':
    while True:
        f = input("1.Нажмите ENTER, чтобы начать процедуру c чтением номеров из файла numbers.txt,\n\n\
2.Введите \"+\" и Нажмите ENTER, чтобы начать процедуру c вводом номеров в окне программы,\n\n\
3.Напечатайте del и нажмите ENTER! \n\
чтобы очистить директорию со штрикодами!\n\n\
4.Напечатайте exit и нажмите  ENTER Чтобы выйти!\n")
        if f == 'del':
            clear_folder()
            message = f"ПАПКА {folder} ОЧИЩЕНА"
            
            print(f"\n\n{make_mes(message)}\n\n")
        if f == 'exit':
            break
        if f == '':
            clear_folder()
            numbers = get_numbers(filename='numbers.txt')
            creator(numbers)
            message = f"{len(numbers)} ШТРИХ-КОДА(ОВ) СГЕНЕРИРОВАНЫ И ПОМЕЩЕНЫ В ПАПКУ \"barcodes_ready\"!"
            print(f'\n\n{make_mes(message)}\n\n')
        if f == '+':
            numbers = []
            while True:
                number_unit = input("Введите очередной номер и нажмите ENTER,\nчтобы закончить нажмите ENTER: \n")
                if number_unit == '':
                    break
                if len(number_unit) >= 2:
                    numbers.append(number_unit)
                    
            print(numbers)
            clear_folder()
            creator(numbers)
            report(numbers)
            message = f"{len(numbers)} ШТРИХ-КОДА(ОВ) СГЕНЕРИРОВАНЫ И ПОМЕЩЕНЫ В ПАПКУ \"barcodes_ready\"! Отчет добавлен в \"inner_report.txt\""
            print(f'\n\n{make_mes(message)}\n\n')  
    
