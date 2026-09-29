class Scale:

    allow_sharp=["G", "D", "A", "E", "B", "F#","e", "b", "f#", "c#", "g#", "d#","C","a"]
    allow_flat=["F", "Bb", "Eb", "Ab", "Db", "Gb","d", "g", "c", "f", "bb", "eb"]
    sharp_list=["A", "A#", "B","C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    flat_list=["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
    def __init__(self, tonic):
        self.tonic=tonic
        self.chromatic()
        self.interval("MmMMmAm")
        
        
    def chromatic(self):
        seq=[]
        
        if self.tonic in self.allow_sharp:
            tonic=self.tonic[0].upper()+ self.tonic[1:]
            index_sharp=self.sharp_list.index(tonic)
            seq=self.sharp_list[index_sharp:] + self.sharp_list[:index_sharp]
        elif self.tonic in self.allow_flat:
            tonic=self.tonic[0].upper()+ self.tonic[1:]
            index_flat=self.flat_list.index(tonic)
            seq=self.flat_list[index_flat:] + self.flat_list[:index_flat]
        return seq



    def interval(self, intervals):
        tonic=self.tonic
        
        if tonic in self.allow_sharp:
            notes=self.sharp_list
            tonic=self.tonic[0].upper()+ self.tonic[1:]
        else:
            notes=self.flat_list
            tonic=self.tonic[0].upper()+ self.tonic[1:]
        index=notes.index(tonic)
        result=[]
        result.append(tonic)
        for i in intervals:
            if i=="M":
               index=(index+2)%12
               result.append(notes[index])
            elif i=="m":
               index=(index+1)%12
               result.append(notes[index]) 
            elif "A":
                index=(index+3)%12
                result.append(notes[index]) 
        return result

scale=Scale("a").chromatic()
scaleInter=Scale("d").interval("MmMMmAm")
print(scale)
print(scaleInter)