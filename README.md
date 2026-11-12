# HTML, Markdown & Files to PDF

A browser-based batch converter for preparing PDF documents from HTML, Markdown, text, local files and accessible URLs.

<p align="center">
  <a href="https://tzayadet.github.io/HTML2PDF/"><img src="https://img.shields.io/badge/LIVE_DEMO-OPEN-00a86b?style=flat-square" alt="Live demo"></a>
  <a href="https://github.com/tzayadet/HTML2PDF"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source"></a>
</p>

[![Pages deployment](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/HTML2PDF/actions/workflows/static.yml)

## Features

- HTML, text and Markdown input.
- Batch conversion queue.
- Local file and accessible URL input.
- Preview and per-job status.
- Retry for failed items.
- Page settings and continuous-page layouts.
- Watermarks, PDF merging and download.

## Use it

Open the [live demo](https://tzayadet.github.io/HTML2PDF/) in a modern browser. The application is static and does not require a project backend.

## Technology

HTML5, CSS3 and JavaScript, with html2canvas, jsPDF, pdfmake, html-to-pdfmake, Marked.js, PDF.js and JSZip. Libraries are loaded from CDNs, so some functions require an internet connection.

## Privacy and limitations

The application has no project backend. Access to external URLs depends on CORS and the source server's policies. Imported HTML is rendered in isolated iframes with scripts disabled.

Do not process confidential documents through external pages unless you have checked where the content is handled and whether any data is transmitted. Performance depends on document size and browser resources.

## Deployment

Static browser application published through GitHub Pages. Conversion runs in the user's browser.

## License

See [LICENSE](LICENSE) for the repository's licensing terms.
