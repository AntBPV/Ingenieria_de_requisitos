from actor import Actor
from base import session_factory

def consultar_actores():
    session=session_factory()
    lista_actores=session.query(Actor)
    session.close()
    for a in lista_actores:
        print(f'- id: {a.id} | nombre: {a.nombre} | nacionalidad: {a.nacionalidad} | biografia: {a.biografia}')
        
def actualizar_actor():
    session=session_factory()
    print('cual de los actores desas modificar: ')
    consultar_actores()
    id_del_actor_a_modificar=input('ingresa el id del actor que deseas modificar: ')
    nombre=input('ingrese el nombre del actor:')
    nacionalidad=input('ingrese la nacionalidad:')
    biografia=input('ingrese la biografia del actor:')
    
    session.query(Actor).filter(Actor.id==id_del_actor_a_modificar).update(
        {
            "nombre":nombre,
            "nacionalidad":nacionalidad,
            "biografia":biografia
        }
    )
    
    mi_actor=session.query(Actor).filter(Actor.id==id_del_actor_a_modificar).one()
    print(f'- id: {mi_actor.id} | nombre: {mi_actor.nombre} | nacionalidad: {mi_actor.nacionalidad} | biografia: {mi_actor.biografia}')
    session.commit()
    session.close()


def crear_actor():
    session=session_factory()
    nombre=input('ingrese el nombre del actor:')
    nacionalidad=input('ingrese la nacionalidad:')
    biografia=input('ingrese la biografia del actor:')
    
    mi_actor=Actor(nombre,nacionalidad,biografia)
    
    session.add(mi_actor)
    session.commit()
    session.close()
    
if __name__=='__main__':
    print('--sistema de gestion de peliculas--')
    print('vamos a crear un actor')
    crear_actor()
    print('vamos a ver los actores creados: ')
    consultar_actores()
    print('Vamos a actualizar un actor')
    actualizar_actor()