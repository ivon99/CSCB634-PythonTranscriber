import pyaudio 
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
	
	def record(self, transcriber) -> None:
		self._stream = self._audio.open(
			format=self.format,
			channels= self.channels,
			rate=self.rate,
			input=self.input,
			frames_per_buffer= self.frames_per_buffer,
			stream_callback= self.audio_processing(transcriber))
		self.start_streaming()
		 
	def audio_processing(self, transcriber):
		def callback(in_data, frame_count, time_info, status):
			transcriber.transcribe(in_data)
			return (in_data, pyaudio.paContinue)
		return callback
	
	def is_active_stream(self) -> bool:
		return self._stream.is_active()
