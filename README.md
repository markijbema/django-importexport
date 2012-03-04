## Usage

Lets say you have a Library of books, and if you export the library, you want to export the books as well, you could do this as follows:

'''
class Library(models.Model, Exportable):
	def export_content(self):
        return self.books.all()
	

class Book(modes.Model, Exportable)
    library = models.ForeignKey(Library, related_name='books')

'''

Now when you call ```library.export()``` you get the whole list of objects to serialize. You can then serialize those using the standard Django serialization methods. To ensure you can safely import the export elsewhere, be sure to use natural keys when exporting, and strip the pk's when importing.