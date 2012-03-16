import itertools

def export_all(exports)
	return list(itertools.chain(*[obj.export() for obj in exports]))

class Exportable():
    def export_content(self):
    	"""
    	DEPRECATED: use export_after instead
    	"""
        return []

    def export_before(self):
    	"""
    	This function should return a list of all models to export before this model
    	"""
        return []

    def export_after(self):
    	"""
    	This function should return a list of all models to export after this model
    	"""
        return []


    def export(self):
        return (
        	export_all(self.export_before())
            +
            [self]
            +
        	export_all(self.export_content() + self.export_after())
        )
