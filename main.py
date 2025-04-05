# capture audio with microphone
# process audio [...]
# convert audio to text

# capture audio with microphone

# 

from modules.sqlqueue import SqlQueue


import os

db_path = r"D:\SentientLabs\Sentinel S0\data\tmp\async_deepgram_sr.queue.db"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

voicedata = SqlQueue(db_path)



while True:
    print(voicedata.get())