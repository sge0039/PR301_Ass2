class ValidateData:
    def __init__(self, new_data):
        self.data = new_data

    def is_validate_date(self):
        if self.check_start_uml():
            if self.check_end_uml():
                if self.check_class_count():
                    return True
        return False

    def check_start_uml(self):
        """
        >>> data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        >>> validate = ValidateData(data)
        >>> validate.check_start_uml()
        True

        >>> data = ['class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        >>> validate = ValidateData(data)
        >>> validate.check_start_uml()
        False
        """
        for line in self.data:
            if '@startuml' in line:
                return True
        return False

    def check_end_uml(self):
        """
        >>> data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        >>> validate = ValidateData(data)
        >>> validate.check_end_uml()
        True

        >>> data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n']
        >>> validate = ValidateData(data)
        >>> validate.check_end_uml()
        False
        """
        for line in self.data:
            if '@enduml' in line:
                return True
        return False

    def check_class_count(self):
        """
        >>> data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', \
                    'class GamePlayer{\\n', 'myPosition', '}\\n', '@enduml']
        >>> validate = ValidateData(data)
        >>> validate.check_class_count()
        True

        >>> data = ['@startuml\\n', 'class LevelEditor{\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n', '@enduml']
        >>> validate = ValidateData(data)
        >>> validate.check_class_count()
        True

        >>> data = ['@startuml\\n', '  allMyBlocks\\n', '  getBlock()\\n', '}\\n']
        >>> validate = ValidateData(data)
        >>> validate.check_class_count()
        False
        """
        class_count = 0
        for line in self.data:
            if 'class' in line:
                class_count += 1
        if class_count > 0:
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # doctest.testmod(verbose=True)
