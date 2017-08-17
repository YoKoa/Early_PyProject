#coding: utf8
import cocos
from cocos.sprite import Sprite
from pyaudio import PyAudio, paInt16
import struct
from person import person
from Block import Block
from idlelib import Percolator

class VoiceGame(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(VoiceGame, self).__init__(255, 255, 255, 255, 800, 600)
        
        self.NUM_SAMPLES = 1000  # pyAudio内部缓存的块的大小
        self.LEVEL = 1500  # 声音保存的阈值
        
        self.voicebar = Sprite('block.jpg', color=(0, 0, 255))
        self.voicebar.position = 20, 450
        self.voicebar.scale_y = 0.1
        self.voicebar.image_anchor = 0, 0
        self.add(self.voicebar)
        
        self.floor = cocos.cocosnode.CocosNode()
        self.add(self.floor)
        pos = 0, 100
        for i in range(0,100):
            b = Block(pos)
            self.floor.add(b)
            pos = b.x + b.width, b.height
        self.p = person()
        self.add(self.p)
        
        pa = PyAudio()
        SAMPLING_RATE = int(pa.get_device_info_by_index(0)['defaultSampleRate'])
        self.stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, frames_per_buffer=self.NUM_SAMPLES)
        
        self.schedule(self.update)#容器
    
    def collide(self):
        px = self.p.x - self.floor.x
        for b in self.floor.get_children():
            if b.x <= px + self.p.width * 0.8 and px + self.p.width * 0.2 <= b.x + b.width:
                if self.p.y < b.height:
                    self.p.land(b.height)
                    break
    
    
    def update(self, dt):
        # 读入NUM_SAMPLES个取样
        string_audio_data = self.stream.read(self.NUM_SAMPLES)
        k = max(struct.unpack('1000h', string_audio_data))
        #print k
        self.voicebar.scale_x = k / 10000.0
        # print k
        if k > 3000:
            self.floor.x -= min((k / 20.0), 150) * dt #以相对与声音的速度向后，加即使向前走
        if k > 8000:
            self.p.jump((k - 8000) / 1000.0)
        self.collide()
    
    
    def reset(self):
        self.floor.x = 0
        

cocos.director.director.init(caption="Let's Go! WoWoWO!")
cocos.director.director.run(cocos.scene.Scene(VoiceGame()))