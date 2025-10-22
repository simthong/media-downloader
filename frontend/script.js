const API_BASE = "https://your-backend-url.onrender.com"; // Replace after deploying backend

async function processLink() {
    const url = document.getElementById("urlInput").value.trim();
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Processing...";

    try {
        const res = await fetch(`${API_BASE}/api/process`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        const data = await res.json();

        if (data.error) {
            resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
            return;
        }

        let html = `<h2>${data.title}</h2><img src="${data.thumbnail}" width="300"><br>`;
        data.formats.forEach(f => {
            html += `<a href="${f.download_url}" target="_blank" download><button>${f.quality || 'Unknown'} (${f.ext})</button></a><br>`;
        });

        resultDiv.innerHTML = html;

    } catch (err) {
        resultDiv.innerHTML = `<p style="color:red;">${err.message}</p>`;
    }
}
