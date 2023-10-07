import os
import random
from pydub import AudioSegment, playback

def main():
    while True:
        absolute = os.path.dirname(__file__)
        mfile = random.choice(os.listdir(f'{absolute}\\music'))
        music = AudioSegment.from_file(f'{absolute}\\music\\{mfile}', format='mp3')
        
        for i in [.5, 1.5, 2.5, 3.5, 5]:
            playback.play(music[:i*1000])
            a = input(f'{i}s - Can you guess the song?\n')
            if a in mfile and a != '':
                print('Good job! Press CTRL+C to continue')
                break
            if a == "give up":
                break

        print(mfile)
        try:
            playback.play(music)
        except KeyboardInterrupt:
            continue


if __name__ == "__main__":
    main()