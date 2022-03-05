from pocketsphinx import LiveSpeech, AudioFile, get_model_path
import os

'''
Microphone Speech to Text function - SanskritSTTlive:
Parameters:   
    1- sampling_rate:
    Sampling rate for the input voice. (Default = 16000)
    
    2- buffer_size:
    Buffer size for speech recognition. (Default = 2048)
    
    
.wav file Speech to Text function - SanskritSTTwav:
Parameters:   
    1- wav_file:
    Path of the .wav file to convert to text.
    
    2- buffer_size:
    Output buffer size. (Default = 2048)
    
Instructions:
1- Use a 'for' loop to continuously input voice and receive output from SanskritSTTlive function, as this is a generator function.
'''

MODEL_PATH = get_model_path()  #To be changed to sanskrit model


def SanskritSTTlive(sampling_rate: int = 16000, buffer_size: int = 2048) -> str:      
    speech = LiveSpeech(
            verbose=False,
            sampling_rate=sampling_rate,
            buffer_size=buffer_size,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(MODEL_PATH, 'en-us'),
            lm=os.path.join(MODEL_PATH, 'en-us.lm.bin'),
            dic=os.path.join(MODEL_PATH, 'cmudict-en-us.dict')
            )
    
    for phrase in speech:
        yield phrase
            

def SanskritSTTwav(wav_file: str, buffer_size: int = 2048) -> str:
    speech = AudioFile(
            verbose = False,
            audio_file = wav_file,
            buffer_size = buffer_size,
            no_search = False,
            full_utt = False,
            hmm = os.path.join(MODEL_PATH, 'en-us'),
            lm = os.path.join(MODEL_PATH, 'en-us.lm.bin'),
            dict = os.path.join(MODEL_PATH, 'cmudict-en-us.dict')
            )
    
    output = ''        
    for phrase in speech:
        output += str(phrase) + ' '
        
    return output.strip()
            


#--------------Example-----------------

if __name__ == '__main__':
    for phrase in SanskritSTTlive():
        print(phrase, end=" ")      
    
    # print(SanskritSTTwav('E:\\Documents\\Chaitanya\\Projects\\Sanskrit_Speech_to_Text\\audio.wav'))