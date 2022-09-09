from .barcode import BarCoder


def qr_form_handler(report_type: str = None, numbers: str = None):
    print(numbers)
    if numbers:
        num_tuple = tuple(numbers.split('\r\n'))
        nums = num_tuple if num_tuple[-1] != '' else num_tuple[:-1]

        bc = BarCoder(nums)
        bc.clear_folder()
        message = bc.create()
        bc.report()
    else:
        message = "Нет серийных номеров для генерации. Введите серийные номера!"
    return message

