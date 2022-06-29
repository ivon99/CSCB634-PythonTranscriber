from datetime import datetime 

class FileWriter(object):
	def __init__(self, text_to_save, filepath) -> None:
		self.text= text_to_save
		self.filepath= filepath
	
	def save_text_to_file(self) -> None:
		curr_time = datetime.now()
		curr_time_str = curr_time.strftime("%H:%M:%S_%d-%m-%y")
		filename= self.filepath +'/'+ curr_time_str
		try:
			f = open(filename, 'w')
			f.write(self.text)
			f.close()
			print("Succesfully saved transcription in file", filename)
		except:
			print("Error in trying to save file!")
