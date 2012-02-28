# -*- coding: utf-8 -*-
from django.db import connection, transaction
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

    YEAR = {
                       '2006': 2006,
                       '2007': 2007,
                       '2008': 2008,
                       '2009': 2009,
                       '2010': 2010,
    }

    TIPO = {
                       '1': 'FATAL',
                       '2': 'GRAVE',
                       '3': 'LEVE',
    }

    cursor = connection.cursor()

    cantidad = request.GET.get('cantidad', 15)
    tipo = request.GET.get('tipofilter', None)
    year = request.GET.get('yearfilter', None)
	
    tipo = str(tipo)
    year = str(year)
    
    if not YEAR.has_key(year):
        year = None    

    if not TIPO.has_key(tipo):
	   tipo = None
    else:
	   tipo = TIPO[tipo]


    if tipo is not None:
	    if year is not None:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente where year = %s and tipo = %s group by calle, cruce having cantidad >= %s order by year desc, cantidad desc;", [year, tipo, cantidad])
		rows = cursor.fetchall()
	    else:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente where tipo = %s group by calle, cruce having cantidad >= %s order by year desc, cantidad desc;", [tipo, cantidad])
		rows = cursor.fetchall()
    else:
	    if year is not None:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente where year = %s group by calle, cruce having cantidad >= %s order by year desc, cantidad desc;", [year, cantidad])
		rows = cursor.fetchall()
	    else:
		cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, year, latititud, longitude from accidentes_accidente group by calle, cruce having cantidad >= %s order by year desc, cantidad desc;", [cantidad, ])
		rows = cursor.fetchall()	


    output = "["
    for row in rows:
		output += "['Aqui hubo " + unicode(row[2]) + " Accidentes.', " + unicode(row[4]) + ", " + unicode(row[5]) + "],"
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
	cursor.execute("select nombre_calle, nombre_cruce, count(*) as cantidad, longitude, latititud from accidentes_accidente group by calle, cruce order by cantidad desc limit 20;")
	rows = cursor.fetchall()
	variables = dict()
	variables['rows'] = rows
	t = get_template('ranking.html')
	html = t.render(RequestContext(request, variables))
	return HttpResponse(html)
