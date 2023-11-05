class ParentModel:
    def get_element_index(self, el, elements) -> int | None:
        index = None
        for i, element in enumerate(elements):
            if str(element.id) == str(el.id):
                index = i
        return index

    def get_element_index_in_file(self, el, file_lines) -> int | None:
        index = None
        for i, element in enumerate(file_lines):
            element = element.split(",")
            if str(element[0]) == str(el.id):
                index = i

        return index
