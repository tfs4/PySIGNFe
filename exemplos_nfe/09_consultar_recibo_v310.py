# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, os.path.abspath(".."))

from pysignfe.nf_e import nf_e

if __name__ == '__main__':
    nova_nfe = nf_e()
    
    #Associacao.pfx nao e valido, utilize um certificado valido
    caminho_certificado = "certificado/Associacao.pfx"
    with open(caminho_certificado, 'rb') as f:
        arquivo = f.read()
    
    info_certificado = nova_nfe.extrair_certificado_a1(arquivo, "associacao")
    
    processo = nova_nfe.consultar_recibo(numero_recibo=u'310000051122111', cert=info_certificado['cert'], key=info_certificado['key'], versao=u'4.00', ambiente=2, estado=u'SP', n_tentativas=3)
    
    print('Status: ' + processo.resposta.cStat.valor)
    print('Motivo: ' + processo.resposta.xMotivo.valor)
    print('Razao: ' + processo.resposta.reason)
    