<p align="center">
  <img src="https://img.shields.io/badge/WEB_UTILITY-DOCUMENT_CONVERTER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Document converter"/>
  <img src="https://img.shields.io/badge/CLIENT_SIDE-BROWSER_APP-101010?style=for-the-badge&logo=javascript&logoColor=00FF41" alt="Browser app"/>
</p>

# HTML, Markdown & Files to PDF

Conversor por lotes en el navegador para preparar documentos PDF a partir de HTML, Markdown, texto, archivos locales y URLs accesibles.

<p align="center">
  <a href="https://tzayadet.github.io/HTML2PDF/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/HTML2PDF"><strong>SOURCE CODE</strong></a>
</p>

[![Pages deployment](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml)

## Features

- Entrada de HTML, texto y Markdown.
- Cola de conversión para varios elementos.
- Incorporación de archivos locales y URLs accesibles.
- Vista previa y seguimiento del estado de cada trabajo.
- Reintento de elementos fallidos.
- Configuración de página y salida continua.
- Marcas de agua, combinación y descarga de PDF.

## Use it

Abre la [demo web](https://tzayadet.github.io/HTML2PDF/) en un navegador moderno. La aplicación es estática y no necesita backend propio.

## Technology

HTML5, CSS3, JavaScript, html2canvas, jsPDF, pdfmake, html-to-pdfmake, Marked.js, PDF.js y JSZip. Las bibliotecas se cargan desde CDN, por lo que algunas funciones requieren conexión a Internet.

## Privacy & limitations

La aplicación no incorpora backend propio. La lectura de URLs externas depende de CORS y de las políticas del servidor de origen. El contenido importado se muestra en iframes aislados sin ejecutar sus scripts.

No introduzcas documentos confidenciales en páginas externas sin comprobar antes dónde se procesan y qué datos se transmiten. La aplicación está pensada para procesamiento local en el navegador; el comportamiento puede variar según el tamaño del documento y los recursos disponibles.

## Deployment

Sitio estático publicado mediante GitHub Pages. Pages sirve la interfaz; la conversión se ejecuta en el navegador del usuario.

## License

See [LICENSE](LICENSE).
