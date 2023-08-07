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
    
    ##Modificar os dados abaixo
    cnpj = u'99999999000191'
    #chave = u'35100910142785000190552000000000071946226632'
    lista_chaves = [u'35100910142785000190552000000000071946226632', u'13140311707347000195650030000004591064552496']
    
    ##Atualmente apenas o Ceará possui webservice para download de Nfes, por isso é mais seguro manter ambiente_nacional=True
    processo = nova_nfe.download_notas(cnpj=cnpj, lista_chaves=lista_chaves, ambiente_nacional=True, cert=info_certificado['cert'], key=info_certificado['key'], versao=u'4.00', ambiente=2, estado=u'SP', contingencia=False)
    
    print('Proc XML: ', processo.resposta.original)
    
    ##Para cada nota baixada
    for ret in processo.resposta.retNFe:
        print('Nota chave: ', ret.chNFe.valor)
        print('\tStatus nota: ', ret.cStat.valor)
        print('\tMotivo: ', ret.xMotivo.valor)
