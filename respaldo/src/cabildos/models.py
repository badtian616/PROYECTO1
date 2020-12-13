from django.db import models
from django.forms import ModelForm
from datetime import datetime, date
from multiselectfield import MultiSelectField


# Create your models here.

class Cabildo(models.Model):
    CATEGORIAS = (
        ('Valores', 'Valores'),
        ('Derechos', 'Derechos'),
        ('Deberes', 'Deberes'),
        ('Instituciones', 'Instituciones'),
    )

    Valores = (
        ('Valores Derechos', 'Valores Derechos'), ('Amistad civica', 'Amistad civica'), ('Autonomia libertad', 'Autonomia libertad'), ('Bien comun comunidad', 'Bien comun comunidad'), ('Buen vivir', 'Buen vivir'), ('Ciudadania', 'Ciudadania'), ('Democracia', 'Democracia'), ('Desarrollo', 'Desarrollo'), ('Desarrollo sustentable', 'Desarrollo sustentable'), ('Descentralizacion', 'Descentralizacion'), ('Dignidad', 'Dignidad'), ('Diversidad', 'Diversidad'), ('Emprendimiento libre', 'Emprendimiento libre'), ('Equidad de gÃ©nero', 'Equidad de gÃ©nero'), ('Estado de derecho', 'Estado de derecho'), ('Estado garante', 'Estado garante'), ('Estado laico', 'Estado laico'), ('Estado solidario', 'Estado solidario'), ('Familia', 'Familia'), ('Felicidad', 'Felicidad'), ('Fraternidad', 'Fraternidad'), ('Identidad cultural', 'Identidad cultural'), ('Igualdad', 'Igualdad'), ('Igualdad de oportunidades', 'Igualdad de oportunidades'), ('Inclusion', 'Inclusion'), ('Innovacion creatividad', 'Innovacion creatividad'), ('Integracion', 'Integracion'), ('Justicia', 'Justicia'), ('Justicia social', 'Justicia social'), ('Medio ambiente', 'Medio ambiente'), ('Multiculturalidad', 'Multiculturalidad'), ('Participacion ciudadana', 'Participacion ciudadana'), ('Patriotismo', 'Patriotismo'), ('Paz convivencia pacifica', 'Paz convivencia pacifica'), ('Pluralismo', 'Pluralismo'), ('Plurinacionalismo', 'Plurinacionalismo'), ('Probidad', 'Probidad'), ('Republica', 'Republica'), ('Respeto', 'Respeto'), ('Respeto conservacion de la naturaleza o medio ambiente', 'Respeto conservacion de la naturaleza o medio ambiente'), ('Seguridad', 'Seguridad'), ('Soberania', 'Soberania'), ('Soberania popular', 'Soberania popular'), ('Solidaridad', 'Solidaridad'), ('Subsidiaridad', 'Subsidiaridad'), ('Tolerancia', 'Tolerancia'), ('Transparencia', 'Transparencia'), ('Transparencia y publicidad', 'Transparencia y publicidad'), ('Unidad', 'Unidad')
        )
    Derechos = (
        ('A huelga', 'A huelga'), ('A la educacion', 'A la educacion'), ('A la honra, al honor', 'A la honra, al honor'), ('A la identidad cultural', 'A la identidad cultural'), ('A la informacion', 'A la informacion'), ('A la integracion de discapacidad', 'A la integracion de discapacidad'), ('A la integridad fisica y psiquica', 'A la integridad fisica y psiquica'), ('A la nacionalidad', 'A la nacionalidad'), ('A la participacion', 'A la participacion'), ('A la salud', 'A la salud'), ('A la seguridad social', 'A la seguridad social'), ('A la seguridad vida sin violencia', 'A la seguridad vida sin violencia'), ('A la vida', 'A la vida'), ('A la vida digna', 'A la vida digna'), ('A la vivienda digna', 'A la vivienda digna'), ('A sindicalizarse y a la negociacion colectiva', 'A sindicalizarse y a la negociacion colectiva'), ('A sufragio votar', 'A sufragio votar'), ('Acceso a informacion publica', 'Acceso a informacion publica'), ('Acceso a la cultura', 'Acceso a la cultura'), ('Al agua', 'Al agua'), ('Al salario equitativo', 'Al salario equitativo'), ('Al trabajo', 'Al trabajo'), ('Articulo 19', 'Articulo 19'), ('De los pueblos indigenas', 'De los pueblos indigenas'), ('De peticion ante las autoridades', 'De peticion ante las autoridades'), ('De propiedad', 'De propiedad'), ('Derecho al agua', 'Derecho al agua'), ('Derecho de asociacion', 'Derecho de asociacion'), ('Derechos del niño, niña y adolescente', 'Derechos del niño, niña y adolescente'), ('Igualdad ante la ley', 'Igualdad ante la ley'), ('Igualdad ante las cargas publicas', 'Igualdad ante las cargas publicas'), ('Igualdad ante los tributos', 'Igualdad ante los tributos'), ('Igualdad de acceso a la justicia debido proceso', 'Igualdad de acceso a la justicia debido proceso'), ('Igualdad de genero', 'Igualdad de genero'), ('Jubilacion digna', 'Jubilacion digna'), ('Libertad ambulatoria', 'Libertad ambulatoria'), ('Libertad de conciencia', 'Libertad de conciencia'), ('Libertad de culto', 'Libertad de culto'), ('Libertad de enseñanza', 'Libertad de enseñanza'), ('Libertad de expresion', 'Libertad de expresion'), ('Libertad de trabajo', 'Libertad de trabajo'), ('Libertad personal', 'Libertad personal'), ('Libertad religiosa', 'Libertad religiosa'), ('Libre iniciativa economica, libre empresa', 'Libre iniciativa economica, libre empresa'), ('No discriminacion', 'No discriminacion'), ('Privacidad e intimidad', 'Privacidad e intimidad'), ('Proteccion judicial de los derechos', 'Proteccion judicial de los derechos'), ('Respeto a la naturaleza medio ambiente', 'Respeto a la naturaleza medio ambiente'), ('Reunion pacifica', 'Reunion pacifica'), ('Seguridad social', 'Seguridad social'), ('Ser elegido en cargos publicos', 'Ser elegido en cargos publicos'), ('Sexuales y reproductivos', 'Sexuales y reproductivos'), ('Trabajo digno', 'Trabajo digno')
        )
    Deberes = (
        ('Cumplimiento de las leyes y normas', 'Cumplimiento de las leyes y normas'), ('Cumplimiento de obligaciones fiscales', 'Cumplimiento de obligaciones fiscales'), ('Cumplimiento de tratados y obligaciones internacionales', 'Cumplimiento de tratados y obligaciones internacionales'), ('De proteccion y conservacion de patrimonio historico y cultural', 'De proteccion y conservacion de patrimonio historico y cultural'), ('De satisfacer cargas publicas', 'De satisfacer cargas publicas'), ('Deber de transparencia en los actos de gobierno', 'Deber de transparencia en los actos de gobierno'), ('Deberes de proteccion de conservacion de la naturaleza', 'Deberes de proteccion de conservacion de la naturaleza'), ('Educacion civica', 'Educacion civica'), ('Ejercicio legitimo y no abusivo de los derechos', 'Ejercicio legitimo y no abusivo de los derechos'), ('Promocion de los derechos fundamentales', 'Promocion de los derechos fundamentales'), ('Proteccion, promocion y respeto de los derechos humanos y fundamentales', 'Proteccion, promocion y respeto de los derechos humanos y fundamentales'), ('Respeto de derechos de otros', 'Respeto de derechos de otros'), ('Respeto por la constitucion', 'Respeto por la constitucion'), ('Responsabilidad', 'Responsabilidad'), ('Responsabilidad civica', 'Responsabilidad civica'), ('Servicio a la comunidad', 'Servicio a la comunidad'), ('Unidad nacional y respeto por chile', 'Unidad nacional y respeto por chile'), ('Voto obligatorio', 'Voto obligatorio')
        )
    Instituciones = (
        ('Asamblea constituyente', 'Asamblea constituyente'), ('Banco central', 'Banco central'), ('Cambio o reforma constitucional', 'Cambio o reforma constitucional'), ('Congreso o parlamento, estructura y funciones', 'Congreso o parlamento, estructura y funciones'), ('Congreso unicameral', 'Congreso unicameral'), ('Contraloria general tribunales de cuentas', 'Contraloria general tribunales de cuentas'), ('Defensor del pueblo ciudadano', 'Defensor del pueblo ciudadano'), ('Division territorial', 'Division territorial'), ('Estado de excepcion', 'Estado de excepcion'), ('Fiscalizacion', 'Fiscalizacion'), ('Forma de estado, federalismo autonomias regionales', 'Forma de estado, federalismo autonomias regionales'), ('Fuerzas armadas', 'Fuerzas armadas'), ('Gobierno local municipal', 'Gobierno local municipal'), ('Gobierno nacional estructura y funciones', 'Gobierno nacional estructura y funciones'), ('Gobierno provincial', 'Gobierno provincial'), ('Gobierno regional', 'Gobierno regional'), ('Iniciativa popular de ley', 'Iniciativa popular de ley'), ('Jefatura de gobierno', 'Jefatura de gobierno'), ('Juicio politico, acusacion constitucional', 'Juicio politico, acusacion constitucional'), ('Justicia constitucional', 'Justicia constitucional'), ('Justicia electoral', 'Justicia electoral'), ('Ministerio de educacion', 'Ministerio de educacion'), ('Ministerio de la familia', 'Ministerio de la familia'), ('Ministerio de salud', 'Ministerio de salud'), ('Ministerio pÃºblico, defensoria publica', 'Ministerio pÃºblico, defensoria publica'), ('Partidos politicos', 'Partidos politicos'), ('Plebiscitos, referendos y consultas', 'Plebiscitos, referendos y consultas'), ('Poder judicial, estructura y funciones', 'Poder judicial, estructura y funciones'), ('Poderes del estado', 'Poderes del estado'), ('Presidencia de la repÃºblica', 'Presidencia de la repÃºblica'), ('Regimen de gobierno presidencial semi-presidencial parlamentario', 'Regimen de gobierno presidencial semi-presidencial parlamentario'), ('Tribunal constitucional', 'Tribunal constitucional'), ('Tribunal de defensa de la libre competencia', 'Tribunal de defensa de la libre competencia')
        )

    categoria = models.CharField(max_length=200, null=True, choices=CATEGORIAS)
    etiquetas = MultiSelectField(max_length=300, choices=Valores)

    #if categoria == "Valores":
    #    etiquetas = MultiSelectField(max_length=300, choices=Valores)
    #elif  categoria == "Derechos":
    #    etiquetas = MultiSelectField(max_length=300, choices=Derechos)
    #elif  categoria == "Deberes":
    #    etiquetas = MultiSelectField(max_length=300, choices=Deberes)
    #elif  categoria == "Instituciones":
    #    etiquetas = MultiSelectField(max_length=300, choices=Instituciones)

    nombre = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=False)
    link = models.CharField('Link ',max_length=200)

    def __str__(self):
        return self.nombre



'''sql 
    id
    etiquetas = conceptos = temas constitucionales # filtar el archivo bachele 2016
    nombre
    fecha
    hora
    #link
    realizado True False
    conclusion = str
    aprobacion = %


lista_categorias = ['Valores','Derechos','Deberes','Instituciones']
'''