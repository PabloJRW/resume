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

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
        Soy Científico de Datos con experiencia en Python, SQL y Power BI. \n
        Soy muy hábil en la transformación, exploración y visualización de 
        grandes conjuntos de datos. Además tengo conocimientos en técnicas 
        de Machine Learning, lo cual me permite desarrollar modelos predictivos 
        para tareas de clasificación y regresión, como también tareas de segmentación.
        También he experimentado con el análisis de series temporales y la creación de 
        modelos predictivos para las mismas.

        Me apasiona la Inteligencia Artificial y las nuevas tecnologías.
        ''')


############
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #2D4D6D">
  <a class="navbar-brand" target="_blank">Pablo Ramos W</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#educación">Educación</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiencia">Experiencia</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#proyectos">Proyectos</a>
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


#####################
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
'2011-2021')
st.markdown('''
- asasadffergedhdfhdgh
''')
txt('**Supervisor**, Azucarera Nacional, S.A., El Roble, Aguadulce',
'2011-2021')
st.markdown('''
- Supervisé el personal para la extracción de producto terminado (azúcar) del almacén.
- Control de inventario. Análisis de datos en Excel.
''')



#####################
st.markdown('''
## Proyectos
''')
txt4('Despliegue de una Aplicación Web de modelo de Machine Learning', 'https://deploying-ml-app-ght4v3x8j4p.streamlit.app/')
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
txt3('Model deployment', '`streamlit`')

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
