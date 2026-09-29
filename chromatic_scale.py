class Scale:
    def __init__(self, tonic):
        self.tonic=tonic
        self.chromatic()

    def chromatic(self):
        seq=[]
        allow_sharp=["G", "D", "A", "E", "B", "F#","e", "b", "f#", "c#", "g#", "d#"]
        allow_flat=["F", "Bb", "Eb", "Ab", "Db", "Gb","d", "g", "c", "f", "bb", "eb"]
        sharp_list=["A", "A#", "B","C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
        flat_list=["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
 
        if self.tonic in allow_sharp:

            tonic=self.tonic[0].upper()+ self.tonic[1:]
            index_sharp=sharp_list.index(tonic)
            seq=sharp_list[index_sharp:] + sharp_list[:index_sharp]
        elif self.tonic in allow_flat:
            tonic=self.tonic[0].upper()+ self.tonic[1:]
            index_flat=flat_list.index(tonic)
            seq=flat_list[index_flat:] + flat_list[:index_flat]
        print(seq)



    def interval(self, intervals):
        pass

scale=Scale("F")