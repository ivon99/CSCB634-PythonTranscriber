from datetime import datetime 

class FileWriter(object):
	def __init__(self, text_to_save, filepath) -> None:
		self.text= text_to_save
		self.filepath= filepath
	
	def save_text_automatic_filename(self) -> str:
		curr_time = datetime.now()
		curr_time_str = curr_time.strftime("%y-%m-%d_%H:%M:%S")
		filename= self.filepath +'/'+ curr_time_str
		f = open(filename, 'w')
		f.write(self.text)
		f.close()
		return filename
	
	def save_text_inputted_filename(self, in_filename) -> None:
		filename= self.filepath+ '/' + in_filename
		f = open(filename,'a')
		f.write(" ")
		f.write(self.text)
		f.close()
			
