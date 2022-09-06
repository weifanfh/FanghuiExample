def read_csv():
    import csv
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
def read_json():
    import json
    with open ("DaJi_retarget_1.3.5.json") as json_file:
        data = json_file.read()
    data = json.loads(data)
    for item in data:
        print(item)
def excel_file():
    import xlwings as xw
    app = xw.App(visible = True, add_book = False)
    workbook = app.books.add()

excel_file()


