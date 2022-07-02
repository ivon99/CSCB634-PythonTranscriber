"""Module for saving transcriptions to text files.

The module has one class - FileWriter.
"""
from datetime import datetime 

class FileWriter(object):
	"""Class for saving input text to text files.
	
	The class can save text to files with automatically generated filenames from date and time of creation or with inputted from user filenames.
	
	Attributes:
		text: A string of text to be saved in file.
		filepath: A string of filepath to directory where to save the text file.
	"""
	def __init__(self, text_to_save, filepath) -> None:
		"""Initializes FileWriter object with given text to save and filepath to where to save"""
		self.text= text_to_save
		self.filepath= filepath
	
	def save_text_automatic_filename(self) -> str:
		"""Saves text to file with automatically generated filename from current date and time"""
		curr_time = datetime.now()
		curr_time_str = curr_time.strftime("%y-%m-%d_%H:%M:%S")
		filename= self.filepath +'/'+ curr_time_str
		f = open(filename, 'w')
		f.write(self.text)
		f.close()
		return filename
	
	def save_text_inputted_filename(self, in_filename) -> None:
		"""Saves text to file with given filename"""
		filename= self.filepath+ '/' + in_filename
		f = open(filename,'a')
		f.write(" ")
		f.write(self.text)
		f.close()
			
