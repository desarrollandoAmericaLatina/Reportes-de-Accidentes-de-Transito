# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from reporteaccidentes.accidentes.models import Accidente

def index(request):
    variables = dict()
    t = get_template('index.html')
    html = t.render(RequestContext(request, variables))
    return HttpResponse(html)


def get_top(request):
    YEAR = (
                       ('2006', 2006),
                       ('2007', 2007),
                       ('2008', 2008),
                       ('2008', 2009),
                       ('2010', 2010),
    )

    TIPO = (
                       ('1', 'FATAL'),
                       ('2', 'GRAVE'),
                       ('3', 'LEVE'),
    )


    from django.db import connection, transaction
    cursor = connection.cursor()
    year = None
    cantidad = None
    tipo = None

    cantidad = request.GET.get('cantidad', 15)
    tipo = request.GET.get('tipofilter', None)
    year = request.GET.get('yearfilter', None)

    if year not in YEAR:
	year = None

    if tipo not in TIPO:
	tipo = None

    if tipo is not None:
	    if year is not None:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente group by calle, cruce where year = %s and tipo = %s having cantidad > %s order by year desc, cantidad desc;", [year, tipo, cantidad])
		rows = cursor.fetchall()
	    else:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente group by calle, cruce where tipo = %s having cantidad > %s order by year desc, cantidad desc;", [cantidad, tipo])
		rows = cursor.fetchall()
    else:
	    if year is not None:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente group by calle, cruce where year = %s having cantidad > %s order by year desc, cantidad desc;", [year,cantidad])
		rows = cursor.fetchall()
	    else:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente group by calle, cruce having cantidad > %s order by year desc, cantidad desc;", [cantidad,])
		rows = cursor.fetchall()	


    output = "["
    for row in rows:
		output += "['Aqui hubo " + unicode(row[2]) + " Accidentes.', " +  unicode(row[4])  + ", " +  unicode(row[5])  + "],"
    output += "];"
    return HttpResponse(output)


def about(request):
    variables = dict()
    t = get_template('acerca-de.html')
    html = t.render(RequestContext(request, variables))
    return HttpResponse(html)


def top(request):
	from django.db import connection, transaction
	cursor = connection.cursor()
	cursor.execute("select nombre_calle, calle, nombre_cruce, cruce, count(*) as cantidad, longitude, latititud from accidentes_accidente group by calle, cruce order by cantidad desc limit 20;")
	rows = cursor.fetchall()
	variables = dict()
	variables['rows'] = rows
	t = get_template('ranking.html')
	html = t.render(RequestContext(request, variables))
	return HttpResponse(html)
