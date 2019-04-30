try:
    from Model.file_handler import FileHandler
    from Model.class_maker import ClassMaker
    from Model.uml_interpreter import UmlInterpreter
    from Model.validate_data import ValidateData
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    print(ImportError)


def start():
    print('start')
    file_handler = FileHandler()
    file_content = file_handler.load_from_file()
    validate = ValidateData(file_content)
    if validate.is_validate_date():
        interpreter = UmlInterpreter()
        uml_list = interpreter.uml_decoder(file_content)
        class_maker = ClassMaker()
        all_my_classes = []
        for item in uml_list:
            all_my_classes.append(class_maker.class_designer(item))
        file_handler.get_folder_dir()
        for item in all_my_classes:
            # file_name = root.directory + '/' + item['file_name']
            file_handler.write_to_file(item['file_name'], item['file_content'])
            file_handler.write_to_pickle(item['file_name'], item['file_content'])
    print('end')
    # test = 'String'
    # test_dict = {'String': 'str'}
    # print(test_dict[test])


if __name__ == '__main__':
    start()
