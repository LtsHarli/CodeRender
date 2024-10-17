document.addEventListener('DOMContentLoaded', () => {
    const htmlInput = document.getElementById('html-input');
    const cssInput = document.getElementById('css-input');
    const jsInput = document.getElementById('js-input');
    const runButton = document.getElementById('run-button');
    const outputDisplay = document.getElementById('output-display');
    const codeEditors = document.querySelectorAll('.code-editor');

    // Make code editors resizable
    codeEditors.forEach(editor => {
        editor.style.resize = 'vertical';
        editor.style.overflow = 'auto';
    });

    // Make output display resizable
    outputDisplay.style.resize = 'vertical';
    outputDisplay.style.overflow = 'auto';

    runButton.addEventListener('click', () => {
        const html = htmlInput.value;
        const css = cssInput.value;
        const js = jsInput.value;

        const combinedCode = `
            <html>
                <head>
                    <style>${css}</style>
                </head>
                <body>
                    ${html}
                    <script>${js}</script>
                </body>
            </html>
        `;

        outputDisplay.innerHTML = '';
        const iframe = document.createElement('iframe');
        iframe.style.width = '100%';
        iframe.style.height = '100%';
        iframe.style.border = 'none';
        iframe.style.flexGrow = '1';
        outputDisplay.appendChild(iframe);

        iframe.contentDocument.open();
        iframe.contentDocument.write(combinedCode);
        iframe.contentDocument.close();

        // Add default styles to ensure text visibility
        const defaultStyles = iframe.contentDocument.createElement('style');
        defaultStyles.textContent = 'body { color: black; background-color: white; }';
        iframe.contentDocument.head.appendChild(defaultStyles);

        // Apply user-provided CSS styles to the iframe content
        const styleElement = iframe.contentDocument.createElement('style');
        styleElement.textContent = css;
        iframe.contentDocument.head.appendChild(styleElement);
    });
});