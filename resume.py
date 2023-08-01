import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

###############
# Header
st.write('''
# Pablo Ramos Wilkins
##### *Análisis de Datos - Ciencia de Datos - Aprendizaje Automático*
''')

image = Image.open('yo.jpeg')
st.image(image)

st.markdown('## Resumen', unsafe_allow_html=True)
st.info('''
        Apasionado por la tecnología y con una fuerte inclinación hacia el análisis de datos 
        y la ciencia de datos, me entusiasma la posibilidad de formar parte de una empresa en 
        un rol de datos, como analista de datos o científico de datos. Aunque no cuento con 
        experiencia profesional formal en estos roles, mi pasión y dedicación por el análisis 
        de datos me han llevado a aprender y desarrollar mis habilidades a través de la ejecución 
        de proyectos prácticos.

        He realizado una variedad de tareas, incluyendo la exploración y análisis de datos (EDA), 
        creación de visualizaciones impactantes, desarrollo de dashboards web interactivos, modelado 
        con machine learning, y despliegue de modelos utilizando Streamlit. También he experimentado 
        con técnicas de clusterización para identificar patrones ocultos en los datos.

        Domino el lenguaje Python y me siento cómodo utilizando librerías como NumPy, Pandas, Flask, 
        Streamlit y scikit-learn para llevar a cabo mis proyectos con eficacia y precisión. Mi enfoque
         en la resolución de problemas me ha permitido abordar desafíos técnicos con creatividad y eficiencia.
        
        Me motiva la búsqueda constante de conocimiento y el impulso por seguir aprendiendo. Mi determinación 
        por explorar nuevas tecnologías y enfoques en el ámbito del análisis de datos me ha permitido desarrollar 
        habilidades sólidas y abordar proyectos apasionantes.

        Mi objetivo es colaborar con un equipo apasionado por la tecnología y enfocado en el avance constante. 
        Estoy seguro de que mi determinación y entusiasmo son activos valiosos para enfrentar nuevos desafíos y 
        contribuir al éxito de la empresa.

        ¡Me siento motivado y preparado para asumir el desafío de unirme a un equipo que comparta mi 
        pasión por el análisis de datos y la ciencia de datos!"
        ''')


############
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #2D4D6D">
  <a class="navbar-brand" target="_blank" href="/">Pablo Ramos W</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#educacion">Educación</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiencia">Experiencia</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#portafolio">Portafolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#habilidades">Habilidades</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contacto">Contacto</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4(a, b):
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(f'[Ver Proyecto]({b})')

#####################
st.markdown('''
## Educación
''')

txt('**Lic. en Ingeniería de Operaciones y Logística Empresarial**, *Universidad de Panamá*',
    '2022')

txt('**Técnico en Logística Empresarial**, *Universidad de Panamá*',
    '2022')


#####################
st.markdown('''
## Experiencia
''')

txt('**Auxiliar de Producción**, Nestlé, Natá',
    '2022 - presente')
st.markdown('''
- Apoyo en tareas de fabricación y ensamblaje de productos.
- Mantenimiento y limpieza del área de trabajo.
- Cumplimiento de instrucciones para asegurar la eficiencia y calidad en la producción.
''')
txt('**Supervisor**, Azucarera Nacional, S.A., El Roble, Aguadulce',
    '2020')
st.markdown('''
- Encargado de la supervisión del equipo para la extracción de producto terminado (azúcar) del almacén.
- Realización de registros y seguimiento de inventario.
- Análisis de datos utilizando Microsoft Excel.
''')



#####################
st.markdown('''
## Portafolio
''')
txt4('Despliegue de un modelo de Machine Learning como Aplicación Web', 'https://deploying-ml-app-ght4v3x8j4p.streamlit.app/')
txt4('Segmentación de Clientes para una Tienda Tipo Walmart', 'https://subsequent-spectrum-167.notion.site/Segmentaci-n-de-Clientes-para-una-Tienda-Tipo-Walmart-992c154312d74ec1b50bd297ef06ca71?pvs=4')
txt4('Pronóstico de Demanda de Pasajeros para una Aerolínea', 'https://subsequent-spectrum-167.notion.site/An-lisis-de-Serie-de-Tiempo-add61e2af3684495bc5cbece559fcb17?pvs=4')
txt4('Predicción de Abando de Clientes - Análisis Exploratorio de Datos', 'https://subsequent-spectrum-167.notion.site/Predicci-n-de-abandono-de-clientes-An-lisis-Exploratorio-de-Datos-7d4266304daa4b5f9474ca56fbfd209e?pvs=4')

#####################
st.markdown('''
## Habilidades
''')
txt3('Programming', '`Python`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/pablo-ramos-w')
txt2('Twitter', 'https://twitter.com/DataDevPablo')
txt2('GitHub', 'https://github.com/PabloJRW')

#####################
st.markdown('''
## Contacto
''')
txt2('Correo', 'pablo.datadev@gmail.com')
txt2('Celular', '6777-8628')
