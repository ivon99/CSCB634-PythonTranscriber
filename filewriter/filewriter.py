from datetime import datetime 

class FileWriter(object):
	def __init__(self, text_to_save, filepath) -> None:
		self.text= text_to_save
		self.filepath= filepath
	
	def save_text_automatic_filename(self) -> None:
		curr_time = datetime.now()
		curr_time_str = curr_time.strftime("%H:%M:%S_%d-%m-%y")
		filename= self.filepath +'/'+ curr_time_str
		try:
			f = open(filename, 'w')
			f.write(self.text)
			f.close()
			print("Succesfully saved transcription in file", filename)
		except:
			print("Error in trying to write to file",filename)
	
	def save_text_inputted_filename(self, in_filename):
		filename= self.filepath+ '/' + in_filename
		try:
			f = open(filename,'a')
			f.write(" ")
			f.write(self.text)
			f.close()
			print("Succesfully apended transcription to file", filename)
		except:
			print("Error in trying to write to file", filename)
			
