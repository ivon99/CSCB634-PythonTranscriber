import pyaudio 
import time
from transcriber import *
 
class AudioStreamer(object):
	def __init__(self, format, channels, rate, input, frames_per_buffer) -> None:
		self._audio = pyaudio.PyAudio()
		self._stream = None
		self.frames = []
		self.format= format
		self.channels=channels
		self.rate= rate
		self.input = input
		self.frames_per_buffer=frames_per_buffer
	
	def start_streaming(self) -> None:
		self._stream.start_stream()
		
	def finish_recording(self) -> None:
		 self._stream.stop_stream()
		 self._stream.close()
		 self._audio.terminate()
		 print('Recording has finished')
	
	def record_till_keyboard_interrupt(self, transcriber) -> None:
		try:
			self._stream = self._audio.open(
			format=self.format,
			channels= self.channels,
			rate=self.rate,
			input=self.input,
			frames_per_buffer= self.frames_per_buffer,
			stream_callback= self.audio_processing(transcriber))
			print('Audio recording started. When done press Ctrl-C ...')
			self.start_streaming()
			try: 
				while self._stream.is_active():
					time.sleep(0.1)
			except KeyboardInterrupt:
				self.finish_recording()
		except:
			print("Error while trying to record audio!")
		 
	def audio_processing(self, transcriber):
		def callback(in_data, frame_count, time_info, status):
			transcriber.transcribe(in_data)
			transcriber.debug()
			return (in_data, pyaudio.paContinue)
		return callback
