# HTML → PDF · Batch Converter

Conversor de documentos basado en navegador para preparar y generar PDF a partir de contenido HTML, Markdown, archivos locales y direcciones web.

**Demo:** https://tzayadet.github.io/HTML2PDF/  
**Código:** https://github.com/tzayadet/HTML2PDF

## Funcionalidades

- Añadir contenido HTML o texto pegado.
- Convertir contenido Markdown.
- Incorporar archivos locales y URLs a una cola de trabajo.
- Procesar varios elementos y revisar el estado de cada conversión.
- Reintentar elementos con errores y consultar el historial de trabajos.
- Configurar anchura de página, formato y opciones avanzadas de salida.
- Generar documentos de página continua cuando el contenido lo requiere.
- Aplicar marcas de agua y combinar documentos.
- Descargar los PDF generados.

## Uso

Abre la [demo web](https://tzayadet.github.io/HTML2PDF/), selecciona el tipo de entrada, añade el contenido a la cola y ejecuta la conversión.

También puedes descargar el repositorio y abrir `index.html` en un navegador moderno.

## Tecnologías

- HTML5, CSS3 y JavaScript
- html2canvas
- jsPDF
- pdfmake
- html-to-pdfmake
- Marked.js
- PDF.js
- JSZip

Las bibliotecas se cargan desde CDN. Para disponer de todas las funciones dependientes de esas bibliotecas se necesita conexión a Internet.

## Privacidad y limitaciones

La interfaz está diseñada para procesar contenido desde el navegador y no incorpora un backend propio. La disponibilidad de una URL externa depende de las restricciones CORS del servidor de origen; una web puede impedir que el navegador lea su contenido.

No introduzcas documentos confidenciales en servicios o páginas externas sin comprobar previamente dónde se procesan y qué información se transmite.

## Despliegue

La demo se publica como contenido estático mediante GitHub Pages. GitHub Pages no ejecuta procesos de servidor.

## Licencia

Consulta [LICENSE](LICENSE).
