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

    #MATERIAS
    url(r'^materia/$', 'carrera.views.index_materia'),
    url(r'^materia/new/$', 'carrera.views.new_materia'),
    url(r'^materia/list/requisitos/$', 'carrera.views.list_materias_requisitos'),
    url(r'^materia/(?P<materia_id>\d+)/requisitos/$', 'carrera.views.requisitos_materia'),
    url(r'^materia/(?P<materia_id>\d+)/add/(?P<requisito_id>\d+)/requisisto/$', 'carrera.views.add_requisito'),
    url(r'^materia/remove/(?P<requisito_id>\d+)/requisisto/$', 'carrera.views.remove_requisito'),
    url(r'^materia/list/update/$', 'carrera.views.list_materias_update'),
    url(r'^materia/(?P<materia_id>\d+)/update/$', 'carrera.views.update_materia'),

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

    url(r'^ajax/materias/carrera/$', 'gestion.views.ajax_materias_carrera'),
    url(r'^ajax/materias/asig/docente/$', 'gestion.views.ajax_materias_asignadas_docente'),

    #INSCRIPCIONES
    url(r'^insc/$', 'inscripcion.views.index_inscripcion'),
    url(r'^insc/new/select/carrera/$', 'inscripcion.views.select_carrera_inscripcion'),
    url(r'^insc/new/estudiante/(?P<carrera_id>\d+)/carrera/$', 'inscripcion.views.new_estudiante'),
    url(r'^insc/new/info/(?P<carrera_id>\d+)/carrera/(?P<estu_id>\d+)/est/$', 'inscripcion.views.info_new_inscripxion'),
    url(r'^insc/new/confirm/(?P<carrera_id>\d+)/carrera/(?P<estu_id>\d+)/est$', 'inscripcion.views.confirm_new_inscripcion'),

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
)
