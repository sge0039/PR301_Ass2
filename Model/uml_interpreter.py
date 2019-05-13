try:
    from my_error import MyError
except ImportError:
    print(ImportError)


class UmlInterpreter:
    def uml_decoder(self, uml_content):
        uml_list = []
        class_dict = {}
        attr_list = []
        method_list = []
        relationship = []
        for line in uml_content:
            if self.is_class(line):
                class_dict['class'] = self.uml_class(line)
            elif self.is_method(line):
                method_list.append(self.uml_method(line))
            elif self.is_class_end(line):
                class_dict['attribute'] = attr_list
                class_dict['method'] = method_list
                temp_dict = class_dict.copy()
                uml_list.append(temp_dict)
                class_dict.clear()
                method_list = []
                attr_list = []
            elif self.is_relationship(line):
                relationship.append(self.uml_relationship(line))
            elif self.is_attribute(line):
                attr_list.append(self.uml_attribute(line))
        return self.place_relationship(relationship, uml_list)

    def is_class(self, line):
        return 'class' in line

    def is_method(self, line):
        return '(' in line and ')' in line

    def is_attribute(self, line):
        return '(' not in line and ')' not in line and '@' not in line and len(line) > 1

    def is_relationship(self, line):
        return '--' in line

    def is_class_end(self, line):
        return '}' in line

    def uml_relationship(self, new_line):
        try:
            remove_list = [' ', '', '\n', '\t']
            temp_relationship = self.char_remover(new_line, remove_list)
            # raise MyError("test: raise an exception")
        except ValueError as err:
            print("The exception is: ", err)
        except MyError as err:
            print(err)
        except:
            print("An unexpected exception just happened.")
        else:
            print("No exception is raised")
            return temp_relationship.split('--')
        finally:
            print("This is the end")

    def place_relationship(self, new_relationship, new_uml_list):
        relationship_list = []
        for item in new_uml_list:
            for relationship in new_relationship:
                if relationship[0] in item['class'] or relationship[1] in item['class']:
                    for i, att in enumerate(item['attribute']):
                        if relationship[0] in att:
                            relationship_list.append(att)
                            del item['attribute'][i]
            if relationship_list:
                item['relationship'] = relationship_list
                relationship_list = []
        return new_uml_list

    def uml_class(self, new_line):
        """
        >>> line = 'class LevelEditor{\\n'
        >>> interpreter = UmlInterpreter()
        >>> interpreter.uml_class(line)
        'LevelEditor'
        """
        remove_list = ['class', ' ', '{', '\t', '\n']
        return self.char_remover(new_line, remove_list)

    def uml_method(self, new_line):
        """
        >>> line = '  getBlock()\\n'
        >>> interpreter = UmlInterpreter()
        >>> interpreter.uml_class(line)
        'getBlock()'
        """
        remove_list = ['\n', '\t', ' ']
        return self.char_remover(new_line, remove_list)

    def uml_attribute(self, new_line):
        """
        >>> line = '  allMyBlocks\\n'
        >>> interpreter = UmlInterpreter()
        >>> interpreter.uml_class(line)
        'allMyBlocks'
        """
        remove_list = ['\n', '\t', '(', ')', ' ']
        return self.char_remover(new_line, remove_list)

    def char_remover(self, string_input, remove_list):
        """
        >>> string = '  getBlock()\\n'
        >>> r_list = ['\\n', '\\t', ' ']
        >>> interpreter = UmlInterpreter()
        >>> interpreter.char_remover(string, r_list)
        'getBlock()'
        """
        for item in remove_list:
            string_input = string_input.replace(item, '')
        return string_input


if __name__ == "__main__":
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)
