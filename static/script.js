async function analisarOpinion() {
    const opinion = document.getElementById('opinion').value;
    const response = await fetch('/analisar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ opinion })
    });
    const data = await response.json();
    document.getElementById('resultado').innerText = `Classificação: ${data.label}`;
}