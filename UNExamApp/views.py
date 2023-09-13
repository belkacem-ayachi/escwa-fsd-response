from django.shortcuts import render
from django.http import JsonResponse
from UNExamApp.v1.controllers import c_aggregate
from django.views.decorators.csrf import csrf_exempt
from UNExamApp.logger import logger
from json import loads, dumps

@csrf_exempt
def aggregate(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})
    
    logger.debug(request)
    body = loads(request.body)
    reporter = body.get("Reporter")
    partner = body.get("Partner")
    sector = body.get("Sector")

    if reporter is None and partner is None and sector is None:
        logger.critical("Nothing was passed")
        return JsonResponse({"status": 400, "message": "At least 1 is required: Reporter, Sector, Partner"})

    # Aggregate work
    result = c_aggregate(reporter=reporter, partner=partner, sector=sector)

    return JsonResponse(result, safe=False)

