import requests
import random

libros = [
    'genesis',
    'exodo',
    'levitico',
    'numeros',
    'deuteronomio',
    'josue',
    'jueces',
    'rut',
    '1-samuel',
    '2-samuel',
    '1-reyes',
    '2-reyes',
    '1-cronicas',
    '2-cronicas',
    'esdras',
    'nehemias',
    'ester',
    'job',
    'salmos',
    'proverbios',
    'eclesiastes',
    'cantares',
    'isaias',
    'jeremias',
    'lamentaciones',
    'ezequiel',
    'daniel',
    'oseas',
    'joel',
    'amos',
    'abdias',
    'jonas',
    'miqueas',
    'nahum',
    'habacuc',
    'sofonias',
    'hageo',
    'zacarias',
    'malaquias',
    'mateo',
    'marcos',
    'lucas',
    'juan',
    'hechos',
    'romanos',
    '1-corintios',
    '2-corintios',
    'galatas',
    'efesios',
    'filipenses',
    'colosenses',
    '1-tesalonicenses',
    '2-tesalonicenses',
    '1-timoteo',
    '2-timoteo',
    'tito',
    'filemon',
    'hebreos',
    'santiago',
    '1-pedro',
    '2-pedro',
    '1-juan',
    '2-juan',
    '3-juan',
    'judas',
    'apocalipsis'
]

# Generar un número aleatorio para seleccionar un libro
random_index = random.randint(0, len(libros) - 1)  # Índices válidos en la lista
libro = libros[random_index]
print("Libro seleccionado: " + libro)

# Obtener el número de capítulos del libro seleccionado
url = f"https://bible-api.deno.dev/api/read/rv1960/{libro}/1"
capitulos_response = requests.get(url)

if capitulos_response.status_code == 200:  # Verifica que la solicitud fue exitosa
    data = capitulos_response.json()  # Convierte el contenido a un diccionario
    capitulos = str(data['num_chapters'])  # Convertir a string
    #print("Capítulos en el libro:", capitulos)
    random_index_capitulos = random.randint(1, data['num_chapters'])
    #print("random_index_capitulos:", random_index_capitulos)
else:
    print(f"Error al obtener capítulos: {capitulos_response.status_code}")
    exit()  # Finaliza el programa si hay un error

# Obtener versículos del último capítulo del libro seleccionado
url_versiculos = f"https://bible-api.deno.dev/api/read/rv1960/{libro}/{random_index_capitulos}"
versiculos_response = requests.get(url_versiculos)

if versiculos_response.status_code == 200:  # Verifica que la solicitud fue exitosa
    data_versiculos = versiculos_response.json()  # Convierte el contenido a un diccionario
    versiculos = data_versiculos
    random_index_versiculos = random.randint(1, len(versiculos['vers']))
    #print(f"cantidad de versiculos en el capitulo: {len(versiculos['vers'])}")
    print(f"{libro} {random_index_capitulos}:{versiculos['vers'][random_index_versiculos]['number']}")
    #print("numero versículo seleccionado:", versiculos['vers'][random_index_versiculos]['number'])
    print("versículo seleccionado:", versiculos['vers'][random_index_versiculos]['verse'])
else:
    print(f"Error al obtener versículos: {versiculos_response.status_code}")
