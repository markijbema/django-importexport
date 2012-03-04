import itertools
class Exportable():
    # this function should return a list of subobjects which should be exported if this object is exported
    def export_content(self):
        return []

    def export(self):
        return (
            [self]
            +
            list(itertools.chain(*[obj.export() for obj in self.export_content()]))
        )
