import minimongo as mm

class AttrDict(mm.AttrDict):
    #sample how to use class variables
    def __init__(self, *args,**kwargs):
        cls_mbr = self.__class__.__dict__.copy()
        _clss = self.__class__.__base__
        while _clss.__name__ != 'AttrDict':
            cls_mbr.update(_clss.__dict__)
            _clss = _clss.__base__
        filter_mbr = [i for i in cls_mbr if not i.startswith('_')]
        class_members = {key: cls_mbr[key] for key in filter_mbr}
        self.update(class_members)
        super(AttrDict, self).__init__(*args,**kwargs)

class Model(mm.Model):
    #sample how to use class variables
    def __init__(self, *args,**kwargs):
        cls_mbr = vars(self.__class__).copy() #get class members
        _clss = self.__class__.__base__ 
        while _clss.__name__ != 'Model': #get cls members of all bases of a branch
            cls_mbr.update(_clss.__dict__) #until a class specified
            clss = _clss.__base__
        filter_mbr = [k for k in cls_mbr if not callable(cls_mbr[k]) and \
            not k.startswith('_') and not k.startswith('conn') and \
            not isinstance(cls_mbr[k],staticmethod)]
        class_members = {key: cls_mbr[key] for key in filter_mbr}
        self.update(class_members)
        super(Model, self).__init__(*args,**kwargs)
    class Meta:
        database = 'mDB'


