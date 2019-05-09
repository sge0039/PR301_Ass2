from View.view import View  # pragma: no cover
from Model.my_error import MyError  # pragma: no cover


class ClassMaker:
    def file_name(self, new_file_name):
        """
        >>> name = ''
        >>> c_maker = ClassMaker()
        >>> c_maker.file_name(name)
        This is the beginning.
        No exception is raised
        This is the end
        ''

        >>> name = 'LevelDesigner'
        >>> c_maker.file_name(name)
        This is the beginning.
        No exception is raised
        This is the end
        'level_designer'
        """
        return self.name_to_lower(new_file_name)

    def class_maker(self, new_class_name):
        """
        >>> name = 'LevelDesigner'
        >>> c_maker = ClassMaker()
        >>> c_maker.class_maker(name)
        This is the beginning.
        No exception is raised
        This is the end
        'class LevelDesigner:\\n'

        >>> name = 'gamePlayer'
        >>> c_maker.class_maker(name)
        This is the beginning.
        No exception is raised
        This is the end
        'class GamePlayer:\\n'

        >>> name = 'filehandler'
        >>> c_maker.class_maker(name)
        This is the beginning.
        No exception is raised
        This is the end
        'class Filehandler:\\n'
        """
        try:
            print("This is the beginning.")
            class_name = new_class_name.replace(new_class_name[0], new_class_name[0].upper(), 1)
        except ValueError as err:
            print("The exception is: ", err)
        except MyError as err:
            print(err)
        except:
            print("An unexpected exception just happened.")
        else:
            print("No exception is raised")
            return 'class ' + class_name + ':' + View.newline()
        finally:
            print("This is the end")

    def attribute_maker(self, new_attributes):
        attributes = ''
        if len(new_attributes) > 0:
            attributes = View.tab() + 'def __init__(self):' + View.newline()
            self_attributes = ''
            for attribute in new_attributes:
                data_type = ''
                if ':' in attribute:
                    list_temp = attribute.split(':')
                    att_name = self.name_to_lower(list_temp[0])
                    data_type = ': ' + self.get_data_type(list_temp[1])
                else:
                    att_name = self.name_to_lower(attribute)
                self_attributes += View.tab() + View.tab() + 'self.' + att_name + data_type + View.newline()
            attributes += self_attributes
        return attributes

    def get_data_type(self, new_data):
        """
        >>> data = 'String'
        >>> c_maker = ClassMaker()
        >>> c_maker.get_data_type(data)
        'str'

        >>> data = 'Interger'
        >>> c_maker.get_data_type(data)
        'int'

        >>> data = 'Boolean'
        >>> c_maker.get_data_type(data)
        'bool'

        >>> data = 'List'
        >>> c_maker.get_data_type(data)
        '[]'

        >>> data = 'Tuple'
        >>> c_maker.get_data_type(data)
        '()'

        >>> data = 'Dict'
        >>> c_maker.get_data_type(data)
        '{}'

        >>> data = 'NotDataType'
        >>> c_maker.get_data_type(data)
        'not_data_type'
        """
        data_type_dict = {'String': 'str', 'Interger': 'int', 'Float': 'float', 'Boolean': 'bool', 'List': '[]',
                          'Tuple': '()', 'Dict': '{}'}
        if new_data in data_type_dict.keys():
            return data_type_dict[new_data]
        else:
            return 'not_data_type'

    def get_rel_type(self, new_relationship):
        try:
            print("This is the beginning.")
            relationships = []
            for relationship in new_relationship:
                relationships.append(relationship.replace(':', ': '))
            # raise MyError("test: raise an exception")
        except ValueError as err:
            print("The exception is: ", err)
        except MyError as err:
            print(err)
        except:
            print("An unexpected exception just happened.")
        else:
            print("No exception is raised")
            return relationships
        finally:
            print("This is the end")

    def relationship_maker(self, new_relationship):
        relationships = ''
        for relationship in new_relationship:
            relationships += View.tab() + View.tab() + 'self.' + relationship + View.newline()
        return relationships

    def method_maker(self, new_methods):
        methods = ''
        for method in new_methods:
            method_name_arg_data_type = []
            if ':' in method:
                method_name_arg_data_type = method.split(':')
                method_name_arg = method_name_arg_data_type[0].replace(')', '').split('(')
            else:
                method_name_arg = method.replace(')', '').split('(')
            method_name = self.name_to_lower(method_name_arg[0])
            method_args = method_name_arg[1].split(',')
            methods += View.tab() + 'def ' + method_name + '(self'
            for arg in method_args:
                if len(arg) > 0:
                    methods += ', ' + self.name_to_lower(arg)
            if len(method_name_arg_data_type) > 1:
                return_type = 'return ' + self.get_data_type(method_name_arg_data_type[1])
            else:
                return_type = 'pass'
            methods += '):' + View.newline()
            methods += View.tab() + View.tab() + return_type + View.newline() + View.newline()
        return methods

    def class_designer(self, new_dict):
        file_name = self.file_name(new_dict['class'])
        class_name = self.class_maker(new_dict['class'])
        methods = self.method_maker(new_dict['method'])
        attributes = self.attribute_maker(new_dict['attribute'])
        if 'relationship' in new_dict.keys():
            relationships = self.get_rel_type(new_dict['relationship'])
            attributes += self.relationship_maker(relationships)
        attributes += View.newline()
        temp_dict = {'file_name': file_name, 'file_content': class_name + attributes + methods}
        return temp_dict

    def name_to_lower(self, new_name):
        """
        >>> name = ''
        >>> c_maker = ClassMaker()
        >>> c_maker.name_to_lower(name)
        This is the beginning.
        No exception is raised
        This is the end
        ''

        >>> name = 'allMyBlocks'
        >>> c_maker.name_to_lower(name)
        This is the beginning.
        No exception is raised
        This is the end
        'all_my_blocks'

        >>> name = 'AllMyBlocks'
        >>> c_maker.name_to_lower(name)
        This is the beginning.
        No exception is raised
        This is the end
        'all_my_blocks'

        >>> name = 'allmyblocks'
        >>> c_maker.name_to_lower(name)
        This is the beginning.
        No exception is raised
        This is the end
        'allmyblocks'
        """
        try:
            print("This is the beginning.")
            name = ''
            for i, char in enumerate(new_name):
                if char.isupper():
                    x = ''
                    if i != 0:
                        x = '_'
                    char = x + char.lower()
                name += char
        except ValueError as err:
            print("The exception is: ", err)
        except MyError as err:
            print(err)
        except:
            print("An unexpected exception just happened.")
        else:
            print("No exception is raised")

        finally:
            print("This is the end")
        return name


if __name__ == "__main__":  # pragma: no cover
    import doctest  # pragma: no cover
    # doctest.testmod()
    doctest.testmod(verbose=True)  # pragma: no cover
