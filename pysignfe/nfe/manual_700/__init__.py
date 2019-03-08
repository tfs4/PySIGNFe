# -*- coding: utf-8 -*-


ESQUEMA_ATUAL = u'PL_009_V4'

#
# Envelopes SOAP
#
from .soap_400 import SOAPEnvio as SOAPEnvio_400
from .soap_400 import SOAPRetorno as SOAPRetorno_400

#
# Emissão de NF-e 4.00
#
from .nfe_400 import NFe as NFe_400
from .nfe_400 import NFRef as NFRef_400
from .nfe_400 import Det as Det_400
from .nfe_400 import DI as DI_400
from .nfe_400 import Adi as Adi_400
from .nfe_400 import Med as Med_400
from .nfe_400 import Arma as Arma_400
from .nfe_400 import Reboque as Reboque_400
from .nfe_400 import Vol as Vol_400
from .nfe_400 import Lacres as Lacres_400
from .nfe_400 import Dup as Dup_400
from .nfe_400 import ObsCont as ObsCont_400
from .nfe_400 import ObsFisco as ObsFisco_400
from .nfe_400 import ProcRef as ProcRef_400

#
# Envio de lote de NF-e
#
from .envinfe_400 import EnviNFe as EnviNFe_400
from .envinfe_400 import RetEnviNFe as RetEnviNFe_400

#
# Consulta do recibo do lote de NF-e
#
from .consrecinfe_400 import ConsReciNFe as ConsReciNFe_400
from .consrecinfe_400 import RetConsReciNFe as RetConsReciNFe_400
from .consrecinfe_400 import ProtNFe as ProtNFe_400
from .consrecinfe_400 import ProcNFe as ProcNFe_400

#
# Cancelamento de NF-e
#
from .cancnfe_400 import CancNFe as CancNFe_400
from .cancnfe_400 import RetCancNFe as RetCancNFe_400
from .cancnfe_400 import ProcCancNFe as ProcCancNFe_400

#
# Cancelamento de NF-e por EVENTO

from .cancnfe_evento import EventoCancNFe as EventoCancNFe_400
from .cancnfe_evento import EnvEventoCancNFe as EnvEventoCancNFe_400
from .cancnfe_evento import RetEnvEventoCancNFe as RetEnvEventoCancNFe_400
from .cancnfe_evento import ProcEventoNFeCancNFe as ProcEventoNFeCancNFe_400

#
# Carta de Correção EVENTO

from .carta_correcao import EventoCCe as EventoCCe_400
from .carta_correcao import EnvEventoCCe as EnvEventoCCe_400
from .carta_correcao import RetEnvEventoCCe as RetEnvEventoCCe_400
from .carta_correcao import ProcEventoNFeCCe as ProcEventoNFeCCe_400

#
# EPEC EVENTO
#
from .epec_evento import EventoEPEC as EventoEPEC_400
from .epec_evento import EnvEventoEPEC as EnvEventoEPEC_400
from .epec_evento import RetEnvEventoEPEC as RetEnvEventoEPEC_400
from .epec_evento import ProcEventoNFeEPEC as ProcEventoNFeEPEC_400

#
# Inutilização de NF-e
#
from .inutnfe_400 import InutNFe as InutNFe_400
from .inutnfe_400 import RetInutNFe as RetInutNFe_400
from .inutnfe_400 import ProcInutNFe as ProcInutNFe_400

#
# Consulta a situação de NF-e
#
from .conssitnfe_400 import ConsSitNFe as ConsSitNFe_400
from .conssitnfe_400 import RetConsSitNFe as RetConsSitNFe_400

#
# Consulta a situação do serviço
#
from .consstatserv_400 import ConsStatServ as ConsStatServ_400
from .consstatserv_400 import RetConsStatServ as RetConsStatServ_400

#
# Consulta cadastro

from .conscad_400 import ConsCad as ConsCad_400
from .conscad_400 import RetConsCad as RetConsCad_400

