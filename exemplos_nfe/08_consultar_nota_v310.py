# -*- coding: utf-8 -*-

import os, sys
from datetime import datetime
sys.path.insert(0, os.path.abspath(".."))

from pysignfe.nf_e import nf_e

if __name__ == '__main__':
    nova_nfe = nf_e()
    
    #Associacao.pfx nao e valido, utilize um certificado valido
    caminho_certificado = "certificado/Associacao.pfx"
    with open(caminho_certificado, 'rb') as f:
        arquivo = f.read()
    
    info_certificado = nova_nfe.extrair_certificado_a1(arquivo, "associacao")
    
    #Chave de acesso da NFe
    chave = u'31161011111111111111551010000000271543577682'
    
    #Consultar NFe
    processo = nova_nfe.consultar_nfe(chave=chave, cert=info_certificado['cert'], key=info_certificado['key'], versao=u'4.00', ambiente=2, estado=u'SP', contingencia=False)
    
    print('Status: ' + processo.resposta.cStat.valor)
    print('Motivo: ' + processo.resposta.xMotivo.valor)
    print('Razao: ' + processo.resposta.reason)