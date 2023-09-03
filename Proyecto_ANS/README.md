<p align="center"> 
  <img src="image/patients_icon.png" alt="patients.png" width="80px" height="80px">
</p>
<h1 align="center"> Atención hospitalaria de pacientes con COVID-19 </h1>

<h3 align="center"> ¿Se pueden agrupar los pacientes según sus características de ingreso?</h3>
<h5 align="center"> Proyecto Final - Análisis no supervisado</h5>

<p align="center"> 
<img src="image/hospitalgif.gif" alt="Gif hospital" height="300px">
</p>

<h2 align="center"> 
Bienvenidos al Proyecto de Agrupación de Pacientes COVID-19</h2>
<p>Exploraremos los datos de pacientes que han sido hospitalizados por COVID-19 en cuatro clínicas en diferentes ciudades de Colombia Estos datos incluyen detalles demográficos, síntomas al momento del ingreso, variables de examen físico, clasificaciones clínicas y resultados (ingreso a la unidad de cuidados intensivos-UCI y mortalidad).</p>
<p>Anteriormente, nuestro equipo utilizó estos datos para construir modelos supervisados con el objetivo de predecir ingresos a la UCI. En este proyecto, adoptamos un enfoque diferente al aplicar técnicas de aprendizaje no supervisado. </p>

<h2 >Objetivos</h2>
<p>Nuestra meta es reducir la dimensionalidad y descubrir grupos distintos de pacientes basados en sus características al momento de la hospitalización. Esto podría ser valioso para ajustar los tratamientos iniciales según las características de cada grupo.</p>

<h2 >Potenciales Partes Interesadas </h2>
<p>Varios actores podrían encontrar este análisis beneficioso, incluyendo:</p>
  <ul>
      <li>Clínicas y hospitales (públicos y privados)</li>
      <li>Administradores de planes de beneficios de salud</li>
      <li>Consortios de prestadores de servicios de salud</li>
      <li>Profesionales médicos, enfermeras y personal de salud</li>
      <li>Pacientes</li>
      <li>Comunidad en general</li>
  </ul>


<p align="center"> 
<img src="image/hospital2.gif" alt="hospital2" height="300px">
</p>

<p>Muchos de estos actores podrían ser clientes directos interesados en implementar procesamientos y análisis similares en sus instituciones. </p>
  
  
<p> En este proyecto, la fuente de datos consiste en cuatro clínicas privadas en Colombia. La información se obtuvo con la aprobación institucional y la autorización de un comité de ética en investigación.</p>



<h2>Descripción de archivos</h2>

<p>Este proyecto incluye archivos ejecutables, archivos de texto y directorios de la siguiente manera:</p>

<ul type=”A”>
  <li><B>Scripts:</B>  Contiene los notebook de python donde se han procesado o transformado los datos para el modelo</li>
  <li><B>Docs:</B> Documentación del proyecto</li>
  <li><B>Data:</B> Bases de datos que serán utilizadas para la construcción del modelo</li>
  <li><B>Model:</B> Modelo de closterización (Aún no se encuentra elaborado)</li>
  <li><B>image:</B> Imagenes utilizadas para la documentación (Imágenes de apoyo)</li>
</ul>



<h2>Metodología</h2>
<p>La agrupación (clustering) es una técnica de aprendizaje no supervisado en la que los datos se dividen en clústeres basados en similitudes. El objetivo principal es capturar patrones subyacentes en los datos sin necesidad de un labeling previo. En el contexto de nuestro dataset, el clustering puede ayudar a identificar grupos de pacientes con síntomas similares, lo que puede ser valioso para el análisis y la toma de decisiones en los centros de atención médica. </p>
<p align="center"> 
<img src="image/clustering.gif" alt="Formula 1" width="350px" height="350px"></p>
<p>Para este proyecto, consideraremos inicialmente los siguiente algoritmos de clustering para elaborar el modelo:</p>
<ul>
  <li><strong>K-Means</strong></li>
  <li><strong>K-Medoides</strong></li>
  <li><strong>Clustering Jerárquico</strong></li>
  <li><strong>DBSCAN</strong> </li>
</ul>
<p>La elección del algoritmo final dependerá de la naturaleza de los datos y de la evaluación de los resultados para determinar cuál es más adecuado .</p>


<h2> Instrucciones para ejecución del model</h2>
<p>El orden de ejecución de los archivos del programa es el siguiente:</p>

<p><b>1) model.ipynb</b></p>
<p>Se ejecuta para efectuar la creación del archivo evaluation.txt. Al principio de este archivo, se ha importado "BD_Morbimortalidad-COVID-19-2.xlsx" para que las funciones definidas en él puedan ser utilizadas.</p>

<p><b>2) evaluation.txt</b></p>
<p>Finalmente, se debe ejecutar el archivo texto para la comprobación de resultados.</p>




<h2>Bibliografía</h2>
<ul>
  <li><b>Dong E, Du H, Gardner L.</b> An interactive web-based dashboard to track COVID-19 in real time. Lancet Infect Dis. 2020;20(5):533-4.</li>
  <li><b>Collaborators C-CI</b>. Estimating global, regional, and national daily and cumulative infections with SARS-CoV-2 through Nov 14, 2021: a statistical analysis. Lancet. 2022;399(10344):2351-80.</li>
  <li><b>Lin C-T, Bookman K, Sieja A, Markley K, Altman RL, Sippel J, et al. </b>Clinical informatics accelerates health system adaptation to the COVID-19 pandemic: examples from Colorado. Journal of the American Medical Informatics Association. 2020;27(12):1955-63.</li>
  <li><b>Merette K, Awad M, Hamid R.</b> Building resilient hospitals in the Eastern Mediterranean Region: lessons from the COVID-19 pandemic. BMJ Global Health. 2022;7(Suppl 3):e008754.</li>
  <li><b>Staffolani S, Iencinella V, Cimatti M, Tavio M.</b> Long COVID-19 syndrome as a fourth phase of SARS-CoV-2 infection. Infez Med. 2022;30(1):22-9.</li>
  <li><b>Saavedra Trujillo CH</b>. ADENDO: ACTUALIZACIÓN 27/06/2020. Consenso colombiano de atención, diagnóstico y manejo de la infección por SARS-CoV-2/COVID-19 en establecimientos de atención de la salud: Recomendaciones basadas en consenso de expertos e informadas en la evidencia ACIN-IETS. SEGUNDA EDICIÓN. Infectio. 2020;24(3).</li>
  <li><b>Mirfazeli FS, Sarabi-Jamab A, Jahanbakhshi A, Kordi A, Javadnia P, Shariat SV, et al.</b> Neuropsychiatric manifestations of COVID-19 can be clustered in three distinct symptom categories. Scientific Reports. 2020;10(1):20957.</li>
  <li><b>Otake S, Chubachi S, Namkoong H, Nakagawara K, Tanaka H, Lee H, et al.</b> Clinical clustering with prognostic implications in Japanese COVID-19 patients: report from Japan COVID-19 Task Force, a nation-wide consortium to investigate COVID-19 host genetics. BMC Infectious Diseases. 2022;22(1):735.</li>
  <li><b>Fernández-de-las-Peñas C, Martín-Guerrero JD, Florencio LL, Navarro-Pardo E, Rodríguez-Jiménez J, Torres-Macho J, et al.</b> Clustering analysis reveals different profiles associating long-term post-COVID symptoms, COVID-19 symptoms at hospital admission and previous medical co-morbidities in previously hospitalized COVID-19 survivors. Infection. 2023;51(1):61-9.</li>
  <li><b>San-Cristobal R, Martín-Hernández R, Ramos-Lopez O, Martinez-Urbistondo D, Micó V, Colmenarejo G, et al.</b> Longwise Cluster Analysis for the Prediction of COVID-19 Severity within 72 h of Admission: COVID-DATA-SAVE-LIFES Cohort. Journal of Clinical Medicine. 2022;11(12):3327.</li>
  <li><b>Hu F, Huang M, Sun J, Zhang X, Liu J. </b>An analysis model of diagnosis and treatment for COVID-19 pandemic based on medical information fusion. Information Fusion. 2021;73:11-21.</li>
  <li><b>Pezoulas VC, Kourou KD, Mylona E, Papaloukas C, Liontos A, Biros D, et al.</b> ICU admission and mortality classifiers for COVID-19 patients based on subgroups of dynamically associated profiles across multiple timepoints. Computers in Biology and Medicine. 2022;141:105176.</li>
  <li><b>Han L, Shen P, Yan J, Huang Y, Ba X, Lin W, et al.</b> Exploring the Clinical Characteristics of COVID-19 Clusters Identified Using Factor Analysis of Mixed Data-Based Cluster Analysis. Frontiers in Medicine. 2021;8.</li>
  <li><b>Rodríguez A, Ruiz-Botella M,  Martín-Loeches I, Jimenez Herrera M, Solé-Violan J, Gómez J, et al.</b> Deploying unsupervised clustering analysis to derive clinical phenotypes and risk factors associated with mortality risk in 2022 critically ill patients with COVID-19 in Spain. Critical Care. 2021;25(1):63.</li>
</ol>


<h2 id="integrantes">Integrantes</h2>
<p></p>
<ul>
  <li><strong>Andrés Gaviria</strong></li>
  <li><strong>Denisse Trujillo</strong> </li>
  <li><strong>Eniver Pino </strong></li>
  <li><strong>Luis Daza</strong></li>
  
  
</ul>
