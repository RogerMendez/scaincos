from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,} ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'usuarios.views.index'),

    url(r'^admin/', include(admin.site.urls)),
    #USUARIOS
    url(r'^login/$', 'usuarios.views.login_user'),
    url(r'^logout/$', 'usuarios.views.logout_user'),
    url(r'^change/password/$', 'usuarios.views.change_password'),
    url(r'^user/info/$', 'usuarios.views.info_usuario'),

    #ADMINISTRATIVOS
    url(r'^adm/$', 'personal.views.index_administrativo'),
    url(r'^adm/new/$', 'personal.views.new_administrativo'),
    url(r'^adm/change/$', 'personal.views.change_administrativo'),
    url(r'^adm/(?P<persona_id>\d+)/update/$', 'personal.views.update_administrativo'),
    url(r'^adm/list/detail/$', 'personal.views.list_detail_administrativo'),
    url(r'^adm/(?P<id_adm>\d+)/detail/$', 'personal.views.detail_administrativo'),

    url(r'^pdf/adm/$', 'personal.views.pdf_administrativos'),

    #ESTUDIANTES
    url(r'^est/$', 'personal.views.index_estudiantes'),
    url(r'^est/new/$', 'personal.views.new_estudiante'),
    url(r'^est/list/change/$', 'personal.views.change_estudiante'),
    url(r'^est/(?P<est_id>\d+)/update/$', 'personal.views.update_estudiante'),
    url(r'^est/list/detail/$', 'personal.views.list_detail_estudiante'),
    url(r'^est/(?P<est_id>\d+)/detail/$', 'personal.views.detail_estudiante'),
    url(r'^est/pdf/list/$', 'personal.views.pdf_estudianes'),

    #DOCENTES
    url(r'^doc/$', 'personal.views.index_docente'),
    url(r'^doc/new/$', 'personal.views.new_docente'),
    url(r'^doc/change/$', 'personal.views.change_docente'),
    url(r'^doc/(?P<doc_id>\d+)/update/$', 'personal.views.update_docente'),
    url(r'^doc/list/detail/$', 'personal.views.list_detail_docente'),
    url(r'^doc/(?P<doc_id>\d+)/detail/$', 'personal.views.detail_docente'),
    url(r'^pdf/doc/$', 'personal.views.pdf_docentes'),

    #AULAS
    url(r'^aula/$', 'institucion.views.index_aula'),
    url(r'^aula/new/$', 'institucion.views.new_aula'),

    #GRUPOS
    url(r'^grupo/$', 'carrera.views.index_grupos'),
    url(r'^grupo/new/$', 'carrera.views.new_grupo'),

    #CARRERAS
    url(r'^carrera/$', 'carrera.views.index_carrera'),
    url(r'^carrera/new/$', 'carrera.views.new_carrera'),
    url(r'^carrera/change/$', 'carrera.views.change_carrera'),
    url(r'^carrera/(?P<carrera_id>\d+)/update/$', 'carrera.views.update_carrera'),
    url(r'^carrera/detail/list/$', 'carrera.views.list_detail_carrera'),
    url(r'^carrera/(?P<carrera_id>\d+)/detail/$', 'carrera.views.detail_carrera'),
    url(r'^carrera/list/plan/curricular/$', 'carrera.views.list_carrera_plan'),

    url(r'^carrera/(?P<carrera_id>\d+)/plan/curricular/$', 'carrera.views.pdf_plan_curricular'),
    url(r'^carrera/pdf/list/$', 'carrera.views.pdf_carreras'),

    #MATERIAS
    url(r'^materia/$', 'carrera.views.index_materia'),
    url(r'^materia/new/$', 'carrera.views.new_materia'),
    url(r'^materia/list/requisitos/$', 'carrera.views.list_materias_requisitos'),
    url(r'^materia/(?P<materia_id>\d+)/requisitos/$', 'carrera.views.requisitos_materia'),
    url(r'^materia/(?P<materia_id>\d+)/add/(?P<requisito_id>\d+)/requisisto/$', 'carrera.views.add_requisito'),
    url(r'^materia/remove/(?P<requisito_id>\d+)/requisisto/$', 'carrera.views.remove_requisito'),
    url(r'^materia/list/update/$', 'carrera.views.list_materias_update'),
    url(r'^materia/(?P<materia_id>\d+)/update/$', 'carrera.views.update_materia'),

    url(r'^ajax/materia/nivel/$', 'carrera.views.ajax_tiempo_carrera'),

    #GESTION
    url(r'^gestion/$', 'gestion.views.index_gestion'),
    url(r'^gestion/new/$', 'gestion.views.new_gestion'),
    url(r'^gestion/(?P<gestion_id>\d+)/change/$', 'gestion.views.change_gestion_session'),
    url(r'^gestion/list/carreras/$', 'gestion.views.list_carreras_gestion'),
    url(r'^gestion/add/(?P<carrera_id>\d+)/carrera/$', 'gestion.views.add_carrera_gestion'),
    url(r'^gestion/asignar/select/docente/$', 'gestion.views.asignar_select_docente'),
    url(r'^gestion/asignar/(?P<docente_id>\d+)/docente/materia/$', 'gestion.views.asignar_materia_docente'),
    url(r'^gestion/asignar/(?P<docente_id>\d+)/docente/(?P<materia_id>\d+)/materia/(?P<grupo_id>\d+)/$', 'gestion.views.add_materia_docente'),
    url(r'^gestion/asignar/remove/(?P<asign_id>\d+)/asignacion/$', 'gestion.views.remove_asignacion'),
    url(r'^gestion/docente/(?P<docente_id>\d+)/materias/$', 'gestion.views.materias_docente'),
    url(r'^gestion/pdf/docente/(?P<docente_id>\d+)/materias/$', 'gestion.views.pdf_materias_docente'),
    url(r'^gestion/materia/(?P<asig_id>\d+)/estudiantes/$', 'gestion.views.estudiantes_docente_materia'),
    url(r'^gestion/pdf/materia/(?P<asig_id>\d+)/estudiantes/$', 'gestion.views.pdf_estudiantes_docente_materia'),
    url(r'^gestion/docente/(?P<doc_id>\d+)/horario/$', 'gestion.views.horario_docente'),

    url(r'^ajax/materias/carrera/$', 'gestion.views.ajax_materias_carrera'),
    url(r'^ajax/materias/asig/docente/$', 'gestion.views.ajax_materias_asignadas_docente'),
    url(r'^ajax/gestion/materias/search/$', 'gestion.views.ajax_search_matter'),

    #INSCRIPCIONES
    url(r'^insc/$', 'inscripcion.views.index_inscripcion'),
    url(r'^insc/new/select/carrera/$', 'inscripcion.views.select_carrera_inscripcion'),
    url(r'^insc/new/estudiante/(?P<carrera_id>\d+)/carrera/$', 'inscripcion.views.new_estudiante'),
    url(r'^insc/new/info/(?P<carrera_id>\d+)/carrera/(?P<estu_id>\d+)/est/$', 'inscripcion.views.info_new_inscripxion'),
    url(r'^insc/new/confirm/(?P<carrera_id>\d+)/carrera/(?P<estu_id>\d+)/est$', 'inscripcion.views.confirm_new_inscripcion'),
    url(r'^insc/carrera/estudiante/all/$', 'inscripcion.views.estudiantes_carrera'),
    url(r'^insc/(?P<carrera_id>\d+)/carrera/estudiante/all/$', 'inscripcion.views.pdf_estudiantes_arrera'),

    #MATICULAS
    url(r'^matricula/$', 'inscripcion.views.index_matricula'),
    url(r'^matricula/new/select/carrera/$', 'inscripcion.views.select_carrera_new_matricula'),
    url(r'^matricula/new/info/(?P<carrera_id>\d+)/carrera/(?P<estu_id>\d+)/est/$', 'inscripcion.views.info_new_matricula'),
    url(r'^matricula/new/confirm/(?P<g_c_id>\d+)/carrera/(?P<estu_id>\d+)/est/$', 'inscripcion.views.confirm_new_matricula'),

    #HORARIOS
    url(r'^horario/select/aula/$', 'gestion.views.select_aula_horario'),
    url(r'^horario/(?P<aula_id>\d+)/aula/$', 'gestion.views.aula_view_horario'),
    url(r'^horario/add/(?P<aula_id>\d+)/aula/(?P<asig_id>\d+)/asignacion/$', 'gestion.views.add_materia_horario'),
    url(r'^horario/remove/(?P<horario_id>\d+)/horario/$', 'gestion.views.remove_materia_horario'),

    url(r'^ajax/horario/materia/asignacion/$', 'gestion.views.ajax_materia_horario'),
    url(r'^ajax/horario/search/docente/$', 'gestion.views.ajax_search_docente'),

    #ASISTENCIA
    url(r'^asistencia/$', 'asistencia.views.index'),
    url(r'^asistencia/new/$', 'asistencia.views.new_asistencia'),
    url(r'^asistencia/list/docentes/$', 'asistencia.views.asistencia_list_docente'),
    url(r'^asistencia/(?P<docente_id>\d+)/docentes/$', 'asistencia.views.asistencia_docente'),

    url(r'^asistencia/ajax/horario/docente/$', 'asistencia.views.ajax_horario_docente'),

    #MODULO ESTUDIANTE
    url(r'^estudiante/$', 'estudiante.views.index_estudiante'),
    url(r'^estudiante/programacion/$', 'estudiante.views.programacion'),
    url(r'^estudiante/programar/$', 'estudiante.views.programar'),
    url(r'^estudiante/notas/$', 'estudiante.views.notas'),

    #MODULO DOCENTE
    url(r'^docente/$', 'docente.views.index_docente'),
    url(r'^docente/mis/materias/$', 'docente.views.mis_materias'),
    url(r'^docente/materia/(?P<asig_id>\d+)/estudiantes/$', 'docente.views.estudiantes_materia'),
    url(r'^docente/materias/notas/$', 'docente.views.materias_docente_notas'),
    url(r'^docente/materia/(?P<asig_id>\d+)/estudiantes/notas/$', 'docente.views.estudiantes_materia_notas'),
    url(r'^docente/notas/(?P<pro_id>\d+)/(?P<asig_id>\d+)/estudiantes/subir/$', 'docente.views.subir_notas_pro'),

    #Preinsctipcion
    url(r'^pre/new/$', 'preinscripcion.views.new_preinscripcion'),
    url(r'^pre/list/$', 'preinscripcion.views.index_preinscripcion'),
    url(r'^pre/list/gestion/$', 'preinscripcion.views.list_preinscripciones_gestion'),
    url(r'^pre/new/estudiante/(?P<pre_id>\d+)/new/inscripcion/$', 'preinscripcion.views.new_inscripcion'),

    #NOTAS
    url(r'^notas/estudiante/all/$', 'estudiante.views.index_notas'),
    url(r'^notas/(?P<insc_id>\d+)/estudiante/notas/$', 'estudiante.views.notas_estudiante'),
    url(r'^notas/gestion/carrera/$', 'estudiante.views.notas_gestion_carreras'),
    url(r'^notas/(?P<gestion_id>\d+)/gestion/(?P<carrera_id>\d+)/carrera/(?P<nivel>\d+)/$', 'estudiante.views.pdf_notas_gestion_carrera'),
    url(r'^notas/estudios/finalizacion/$', 'estudiante.views.estudiantes_finalizacion'),
    url(r'^notas/(?P<insc_id>\d+)/estudiante/historial/$', 'estudiante.views.historial_notas'),
    url(r'^notas/(?P<insc_id>\d+)/estudiante/libro/folio/$', 'estudiante.views.crear_folio_libro'),
    url(r'^notas/(?P<insc_id>\d+)/certificado/calificaciones/pdf/$', 'estudiante.views.pdf_certificado_calificaciones'),

    url(r'^notas/ajax/estudiante/search/$', 'estudiante.views.ajax_buscar_estudiantes'),
    url(r'^notas/ajax/estudiante/notas/$', 'estudiante.views.ajax_notas_estudiante'),
    url(r'^notas/ajax/niveles/carrera/$', 'estudiante.views.ajax_niveles_carrera'),
    url(r'^notas/ajax//carrera/gestion/$', 'estudiante.views.ajax_notas_estudiantes_gestion_carrera'),

    #REPORTES
    url(r'^reporte/carreras/$', 'gestion.views.listado_carreras_reporte'),
    url(r'^ajax/reporte/carrera/docentes/$', 'gestion.views.ajax_docentes_nivel_carrera'),
    url(r'^ajax/reporte/carrera/docentes/select/$', 'gestion.views.ajax_docentes_nivel_carrera_select'),
    url(r'^ajax/reporte/carrera/docente/materias/$', 'gestion.views.ajax_docente_nivel_carrera_materias'),
    url(r'^ajax/reporte/carrera/docente/materias/select/$', 'gestion.views.ajax_docente_nivel_carrera_materias_select'),
    url(r'^ajax/reporte/carrera/docente/materia/estudiantes/$', 'gestion.views.ajax_docente_nivel_carrera_materia_estudiantes'),
)
