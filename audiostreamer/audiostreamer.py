"""Module for recording an audio stream from microphone.

The module has one class- Audio Streamer which uses PyAudio library for creating and manipulating an audio stream.
"""
import pyaudio 

from transcriber import *
 
class AudioStreamer(object):
	"""Class for creating and manipulating an audio stream.
	
	The class uses PyAudio library to create, manipulate and close an audio stream.
	
	Attributes:
		_audio: Object instance for class PuAudio providing an interface for PortAudio.
		_stream: Object instace for PyAudio class Stream
		channels: An integer showing number of channels. (1 for mono, 2 for stereo)
		rate: An integer showing the microphone sampling rate in Hertz. 
		input: Boolean value specifying whether the stream is an input one. 
		frames_per_buffer: An integer specifying the number of frames per buffer.
	"""
	def __init__(self, format, channels, rate, input, frames_per_buffer) -> None:
		"""Initializes AudioStreamer object with given parameters"""
		self._audio = pyaudio.PyAudio()
		self._stream = None
		self.format= format
		self.channels=channels
		self.rate= rate
		self.input = input
		self.frames_per_buffer=frames_per_buffer
	
	def start_streaming(self) -> None:
		"""Starts the audio stream"""
		self._stream.start_stream()
		
	def finish_recording(self) -> None:
		"""Stops and terminates the audio stream and closes the session"""
		self._stream.stop_stream()
		self._stream.close()
		self._audio.terminate()
	
	def record(self, transcriber) -> None:
		"""Starts recording audio input"""
		self._stream = self._audio.open(
			format=self.format,
			channels= self.channels,
			rate=self.rate,
			input=self.input,
			frames_per_buffer= self.frames_per_buffer,
			stream_callback= self.audio_processing(transcriber))
		self.start_streaming()
		 
	def audio_processing(self, transcriber):
		"""Feeds audio stream data to transcriber"""
		def callback(in_data, frame_count, time_info, status):
			transcriber.transcribe(in_data)
			return (in_data, pyaudio.paContinue)
		return callback
	
	def is_active_stream(self) -> bool:
		"""Returns whether the audio stream is active"""
		return self._stream.is_active()
