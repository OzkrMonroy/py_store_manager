class ParentModel:
    def get_element_index(self, el, elements) -> int | None:
        index = None
        for i, element in enumerate(elements):
            if int(element.id) == int(el.id):
                index = i
        return index

    def get_element_index_in_file(self, el, file_lines) -> int | None:
        index = None
        for i, element in enumerate(file_lines):
            element = element.split(",")
            if int(element[0]) == int(el.id):
                index = i

        return index
