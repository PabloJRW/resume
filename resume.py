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
resume_text = '''Apasionado por la tecnología y con una fuerte inclinación hacia el análisis de datos y la ciencia de datos. 
He desarrollado habilidades en exploración y análisis de datos, creación de visualizaciones, desarrollo de aplicaciones y 
dashboards web interactivos, creación y despliegue de modelos de Machine Learning. Domino Python y sus librerías NumPy, 
Pandas, Flask, Streamlit y scikit-learn. Mi enfoque en la resolución de problemas me permite abordar desafíos técnicos con 
creatividad y eficiencia. Busco unirme a un equipo apasionado por la tecnología y el avance constante en el ámbito del análisis 
de datos y la ciencia de datos, donde mi determinación y entusiasmo sean activos valiosos para contribuir al éxito de la empresa.'''
st.markdown(f'<div style="text-align: justify">{resume_text}</div>', unsafe_allow_html=True)


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

def txt2(a, b, c):
    col1, col2, col3 = st.columns([1,1,4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b, unsafe_allow_html=True)
    with col3:
        st.markdown(c)

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
txt4('Despliegue de Aplicaciones para Predicción de Clases con Modelos de Machine Learning', 'https://subsequent-spectrum-167.notion.site/Despliegue-de-Aplicaciones-para-Predicci-n-de-Clases-con-Modelos-de-Machine-Learning-cbe64e5d079c495097ca90de35d11da3?pvs=4')
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

linkedin_icon = '''<svg width="20" height="20" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg">
    <path fill="#0A66C2" d="M218.123 218.127h-37.931v-59.403c0-14.165-.253-32.4-19.728-32.4c-19.756 0-22.779 15.434-22.779 31.369v60.43h-37.93V95.967h36.413v16.694h.51a39.907 39.907 0 0 1 35.928-19.733c38.445 0 45.533 25.288 45.533 58.186l-.016 67.013ZM56.955 79.27c-12.157.002-22.014-9.852-22.016-22.009c-.002-12.157 9.851-22.014 22.008-22.016c12.157-.003 22.014 9.851 22.016 22.008A22.013 22.013 0 0 1 56.955 79.27m18.966 138.858H37.95V95.967h37.97v122.16ZM237.033.018H18.89C8.58-.098.125 8.161-.001 18.471v219.053c.122 10.315 8.576 18.582 18.89 18.474h218.144c10.336.128 18.823-8.139 18.966-18.474V18.454c-.147-10.33-8.635-18.588-18.966-18.453"/>
</svg>'''

twitter_icon = '''<svg width="20" height="20" viewBox="0 0 256 209" xmlns="http://www.w3.org/2000/svg">
    <path fill="#55acee" d="M256 25.45a105.04 105.04 0 0 1-30.166 8.27c10.845-6.5 19.172-16.793 23.093-29.057a105.183 105.183 0 0 1-33.351 12.745C205.995 7.201 192.346.822 177.239.822c-29.006 0-52.523 23.516-52.523 52.52c0 4.117.465 8.125 1.36 11.97c-43.65-2.191-82.35-23.1-108.255-54.876c-4.52 7.757-7.11 16.78-7.11 26.404c0 18.222 9.273 34.297 23.365 43.716a52.312 52.312 0 0 1-23.79-6.57c-.003.22-.003.44-.003.661c0 25.447 18.104 46.675 42.13 51.5a52.592 52.592 0 0 1-23.718.9c6.683 20.866 26.08 36.05 49.062 36.475c-17.975 14.086-40.622 22.483-65.228 22.483c-4.24 0-8.42-.249-12.529-.734c23.243 14.902 50.85 23.597 80.51 23.597c96.607 0 149.434-80.031 149.434-149.435c0-2.278-.05-4.543-.152-6.795A106.748 106.748 0 0 0 256 25.45"/>
</svg>'''

github_icon = '''<svg width="20" height="20" viewBox="0 0 256 250" xmlns="http://www.w3.org/2000/svg">
    <path fill="#161614" d="M128.001 0C57.317 0 0 57.307 0 128.001c0 56.554 36.676 104.535 87.535 121.46c6.397 1.185 8.746-2.777 8.746-6.158c0-3.052-.12-13.135-.174-23.83c-35.61 7.742-43.124-15.103-43.124-15.103c-5.823-14.795-14.213-18.73-14.213-18.73c-11.613-7.944.876-7.78.876-7.78c12.853.902 19.621 13.19 19.621 13.19c11.417 19.568 29.945 13.911 37.249 10.64c1.149-8.272 4.466-13.92 8.127-17.116c-28.431-3.236-58.318-14.212-58.318-63.258c0-13.975 5-25.394 13.188-34.358c-1.329-3.224-5.71-16.242 1.24-33.874c0 0 10.749-3.44 35.21 13.121c10.21-2.836 21.16-4.258 32.038-4.307c10.878.049 21.837 1.47 32.066 4.307c24.431-16.56 35.165-13.12 35.165-13.12c6.967 17.63 2.584 30.65 1.255 33.873c8.207 8.964 13.173 20.383 13.173 34.358c0 49.163-29.944 59.988-58.447 63.157c4.591 3.972 8.682 11.762 8.682 23.704c0 17.126-.148 30.91-.148 35.126c0 3.407 2.304 7.398 8.792 6.14C219.37 232.5 256 184.537 256 128.002C256 57.307 198.691 0 128.001 0Zm-80.06 182.34c-.282.636-1.283.827-2.194.39c-.929-.417-1.45-1.284-1.15-1.922c.276-.655 1.279-.838 2.205-.399c.93.418 1.46 1.293 1.139 1.931Zm6.296 5.618c-.61.566-1.804.303-2.614-.591c-.837-.892-.994-2.086-.375-2.66c.63-.566 1.787-.301 2.626.591c.838.903 1 2.088.363 2.66Zm4.32 7.188c-.785.545-2.067.034-2.86-1.104c-.784-1.138-.784-2.503.017-3.05c.795-.547 2.058-.055 2.861 1.075c.782 1.157.782 2.522-.019 3.08Zm7.304 8.325c-.701.774-2.196.566-3.29-.49c-1.119-1.032-1.43-2.496-.726-3.27c.71-.776 2.213-.558 3.315.49c1.11 1.03 1.45 2.505.701 3.27Zm9.442 2.81c-.31 1.003-1.75 1.459-3.199 1.033c-1.448-.439-2.395-1.613-2.103-2.626c.301-1.01 1.747-1.484 3.207-1.028c1.446.436 2.396 1.602 2.095 2.622Zm10.744 1.193c.036 1.055-1.193 1.93-2.715 1.95c-1.53.034-2.769-.82-2.786-1.86c0-1.065 1.202-1.932 2.733-1.958c1.522-.03 2.768.818 2.768 1.868Zm10.555-.405c.182 1.03-.875 2.088-2.387 2.37c-1.485.271-2.861-.365-3.05-1.386c-.184-1.056.893-2.114 2.376-2.387c1.514-.263 2.868.356 3.061 1.403Z"/>
</svg>'''

st.markdown('''
## Social Media
''')
txt2('LinkedIn', linkedin_icon, 'https://www.linkedin.com/in/pablo-ramos-w')
txt2('Twitter', twitter_icon, 'https://twitter.com/DataDevPablo')
txt2('GitHub', github_icon, 'https://github.com/PabloJRW')

#####################

gmail_icon = '''<svg width="20" height="20" viewBox="0 0 256 193" xmlns="http://www.w3.org/2000/svg">
    <path fill="#4285F4" d="M58.182 192.05V93.14L27.507 65.077L0 49.504v125.091c0 9.658 7.825 17.455 17.455 17.455h40.727Z"/>
    <path fill="#34A853" d="M197.818 192.05h40.727c9.659 0 17.455-7.826 17.455-17.455V49.505l-31.156 17.837l-27.026 25.798v98.91Z"/>
    <path fill="#EA4335" d="m58.182 93.14l-4.174-38.647l4.174-36.989L128 69.868l69.818-52.364l4.669 34.992l-4.669 40.644L128 145.504z"/>
    <path fill="#FBBC04" d="M197.818 17.504V93.14L256 49.504V26.231c0-21.585-24.64-33.89-41.89-20.945l-16.292 12.218Z"/>
    <path fill="#C5221F" d="m0 49.504l26.759 20.07L58.182 93.14V17.504L41.89 5.286C24.61-7.66 0 4.646 0 26.23v23.273Z"/>
</svg>'''

telephone_icon = '''<svg width="20" height="20" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg">
    <path fill="#31373D" d="m34.06 26.407l-3.496-3.496a4.942 4.942 0 0 0-8.34 2.528c-5.765-1.078-11.372-6.662-11.721-11.653a4.908 4.908 0 0 0 2.586-1.36a4.943 4.943 0 0 0 0-6.99L9.594 1.94a4.943 4.943 0 0 0-6.99 0C-7.882 12.426 23.574 43.882 34.06 33.396a4.944 4.944 0 0 0 0-6.989z"/>
</svg>'''

st.markdown('''
## Contacto
''')
txt2('Correo', gmail_icon, 'pablo.datadev@gmail.com')
txt2('Celular', telephone_icon, '6777-8628')



