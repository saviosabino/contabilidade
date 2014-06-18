# coding: utf-8

import minimongo as mm

class Credito(mm.AttrDict):
    def __init__(self, *args, **kwargs):
        self.nome = ''
        self.periodo = ''
        self.valor = 0
        super(Credito, self).__init__(*args, **kwargs)

class Pagamento(mm.AttrDict):
    def __init__(self, *args, **kwargs):
        self.vencimento = ''
        self.nome = ''
        self.tipo = []
        self.valor = 0
        self.pago = False
        super(Pagamento, self).__init__(*args, **kwargs)

class Contabilidade(mm.Model):
    class Meta:
        database = 'mDB'
        indices = [mm.Index('seq')]
        
    def __init__(self, *args, **kwargs):
        self.creditos = []
        self.pagamentos = []
        self.periodo = ''
        super(Contabilidade, self).__init__(*args, **kwargs)
        if not self.has_key('seq'):
            self.seq = self.collection.count()+1
            self.save()

    def creditar(self, **kwargs):
        cred = Credito(seq=len(self.creditos)+1,**kwargs)
        self.creditos.append(cred)
        return cred

    def pagar(self, **kwargs):
        pag = Pagamento(seq=len(self.pagamentos)+1,**kwargs)
        self.pagamentos.append(pag)
        return pag

    def calcTotalPagar(self):
        tot=0
        for x in self.pagamentos:
            tot = tot + x.valor
        return tot

    def calcTotalCredito(self):
        tot=0
        for x in self.creditos:
            tot = tot + x.valor
        return tot

    def calcBalanco(self):
        debito = self.calcTotalPagar()
        credito = self.calcTotalCredito()
        return credito - debito, credito,debito

    @staticmethod
    def get_periodos():
        periodos = list(Contabilidade.collection.find().sort('seq'))
        for per in periodos:
            per.encapsulate()    
        return periodos

    def encapsulate(self):
        for icr,cr in enumerate(self.creditos):
            self.creditos[icr] = Credito(cr)
        for ip,pag in enumerate(self.pagamentos):
            self.pagamentos[ip] = Pagamento(pag)
        self.balanco = self.calcBalanco()
        return self

    @staticmethod
    def get_list():
        return range(1,Contabilidade.collection.count()+1)

    @staticmethod
    def str_periodos():
        from mako.template import Template
        ctpl = Template(filename='contabilidade.txt',
            output_encoding='utf-8')
        p = Contabilidade.get_periodos()
        return ctpl.render(periodos=p)

class Periodo(dict):
    def __getitem__(self, key):
        if key == 'lista':
            return self.get_list()
        else:
            return self.get_contab(key)

    def __getattr__(self, attr):
        return self[attr]

    def get_list(self):
        return range(1,Contabilidade.collection.count()+1)

    def get_contab(self, key):
        return Contabilidade.collection.\
            find_one({'seq':int(key)}).encapsulate()

class Root(dict):
    def __init__(self,request):
        self['periodo'] = Periodo()
        #periodo.__parent__ = self
        
'''
prototype urlmap:
url                     desc
-------------------------------------------------
/                       index - welcome 
/periodo                list_periodos - situações
/periodo/int            default de uma contab
/periodo/new            add
/periodo/int/edit       edit
'''



