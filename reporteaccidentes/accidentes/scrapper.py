# -*- coding: utf-8 -*-
import shapefile
import geo
from reporteaccidentes.accidentes.models import Accidente
from django.conf import settings
from django.template import Context, Template
from django.template.loader import get_template
from django.utils.translation import ugettext as _
import codecs

def scrapdata():
	sf = shapefile.Reader("/home/serge/ReporteDeAccidentes/reporteaccidentes/accidentes/accidentes/accidentes")
	iterator_number = 0
	for rec in sf.records():
		accident = Accidente()
		accident.calle = rec[0]
		accident.cruce = rec[1]
		accident.tipo = rec[2]
		accident.year = rec[3]
		accident.nombre_calle = rec[4]
		accident.nombre_cruce = rec[5]
		accident.esquina = rec[6]
		accident.latititud, accident.longitude = geo.utmToLatLng(21, sf.shape(iterator_number).points[0][0], sf.shape(iterator_number).points[0][1], False)
		accident.save()
		iterator_number += 1


def generate():
	#All
	todos_accidentes = Accidente.objects.all()
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": todos_accidentes})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/todos_accidentes.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass


	#2006
	accidentes_2006 = Accidente.objects.filter(year='2006')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_2006})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_2006.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass

	#2007
	accidentes_2007 = Accidente.objects.filter(year='2007')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_2007})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_2007.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass


	accidentes_2008 = Accidente.objects.filter(year='2008')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_2008})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_2008.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass

	accidentes_2009 = Accidente.objects.filter(year='2009')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_2009})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_2009.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass


	accidentes_2010 = Accidente.objects.filter(year='2010')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_2010})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_2010.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass

	accidentes_graves = Accidente.objects.filter(year='GRAVE')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_graves})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_graves.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass

	accidentes_leve = Accidente.objects.filter(year='LEVE')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_leve})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_leve.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass

	accidentes_fatal = Accidente.objects.filter(year='FATAL')
	t = get_template('javascrip_markers.html')
	c = Context({"accidentes": accidentes_fatal})
	output = t.render(c)
	try:
		gendir = "/home/serge/ReporteDeAccidentes/reporteaccidentes/templates/generated/accidentes_fatal.inc"
		f = codecs.open(filename=gendir, mode="w", encoding='utf-8')
		try:
		    f.write(output) # Write a string to a file
		finally:
		    f.close()
	except IOError:
		pass
