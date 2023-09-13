from UNExamApp.logger import logger
from UNExamApp.v1.interactions import send_request
from UNExamApp.exceptions import EscwaException

def c_aggregate(reporter=None, partner = None, sector = None):
    logger.info("Aggregating")
    try:
        resp = send_request("/DeltaLakeReader/escwa?Reporter=Algeria&name=ETDP/Total%20Trades%20by%20Sector", "GET")
        aggregated = []
        for entry in resp:
            if reporter is not None and entry.get("Provider", "") == reporter:
                aggregated.append(entry)
            if partner is not None and entry.get("Partner", "") == partner:
                aggregated.append(entry)
            if sector is not None and entry.get("Sector", "") == sector:
                aggregated.append(entry)
        return resp
    except EscwaException as e:
        logger.critical("Escwa exception caught")
        logger.critical(e)
        raise e
    except Exception as e:
        logger.critical("Unhandled exception caught")
        logger.critical(e)
        raise EscwaException("server_error", "UNHANDLED EXCEPTION")