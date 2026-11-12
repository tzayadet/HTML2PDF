# HTML, Markdown & Files to PDF

Conversor por lotes basado en navegador para preparar documentos PDF a partir de HTML, Markdown, texto, archivos locales y URLs accesibles.

[![Pages deployment](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml)

**Demo:** [abrir conversor](https://tzayadet.github.io/HTML2PDF/) · **Código:** [repositorio](https://github.com/tzayadet/HTML2PDF)

## Funciones

- Entrada de HTML, texto y Markdown.
- Cola de conversión para varios elementos.
- Incorporación de archivos locales y URLs.
- Vista previa y seguimiento del estado de cada trabajo.
- Reintento de elementos fallidos.
- Configuración de página y salida continua.
- Marcas de agua, combinación y descarga de PDF.

## Tecnologías

HTML5, CSS3, JavaScript, html2canvas, jsPDF, pdfmake, html-to-pdfmake, Marked.js, PDF.js y JSZip. Las bibliotecas se cargan desde CDN, por lo que algunas funciones requieren conexión a Internet.

## Privacidad y limitaciones

La aplicación no incorpora backend propio. La lectura de URLs externas depende de CORS y de las políticas del servidor de origen. El contenido importado se muestra en iframes aislados sin ejecutar sus scripts. No introduzcas documentos confidenciales en páginas externas sin comprobar antes dónde se procesan y qué datos se transmiten.

GitHub Pages publica una interfaz estática; no ejecuta procesos de servidor.

## Licencia

Consulta [LICENSE](LICENSE).
