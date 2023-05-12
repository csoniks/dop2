
from pydub import AudioSegment
sound = AudioSegment.from_file("music.wav")

def speed_change(sound, speed):
    #Вручную переопределяем значение частоты кадров. Это сообщает компьютеру, сколько сэмплы(звуковых фрагментов)для воспроизведения в секунду
    sound_newchastota = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})#частоту на скорость
    # звук с изменением частоты кадров
    return sound_newchastota
    #return sound_newchastota.set_frame_rate(sound.frame_rate)#звук со стандартной частотой
slow_sound = speed_change(sound, 0.5)
fast_sound = speed_change(sound, 2.0)

slow_sound.export('slow.wav', format = 'wav')
fast_sound.export('fast.wav', format = 'wav')
