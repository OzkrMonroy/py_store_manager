class ParentModel:
    def get_element_index(self, list, elements) -> int | None:
        index = None
        for i, element in enumerate(elements):
            if element.id == list[0]:
                index = i
        return index
