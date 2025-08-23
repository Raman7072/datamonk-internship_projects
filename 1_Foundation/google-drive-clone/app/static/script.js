async function fetchFiles() {
    let res = await fetch("/api/files");
    let files = await res.json();
    renderFiles(files);

    // Search filter
    document.getElementById("search").addEventListener("input", e => {
        let q = e.target.value.toLowerCase();
        let filtered = files.filter(f => f.name.toLowerCase().includes(q));
        renderFiles(filtered);
    });
}

function renderFiles(files) {
    let grid = document.getElementById("fileList");
    grid.innerHTML = "";
    files.forEach(f => {
        let icon = "📦";
        if (f.name.match(/\.(jpg|jpeg|png|gif)$/i)) icon = "🖼";
        else if (f.name.match(/\.pdf$/i)) icon = "📄";

        let div = document.createElement("div");
        div.className = "file-card";
        div.innerHTML = `
      <div class="file-icon">${icon}</div>
      <div class="file-name">${f.name}</div>
      <div class="actions">
        <button onclick="downloadFile(${f.id})">⬇</button>
        <button onclick="previewFile(${f.id})">👁</button>
        <button onclick="deleteFile(${f.id})">🗑</button>
      </div>`;
        grid.appendChild(div);
    });
}

async function downloadFile(id) {
    let res = await fetch(`/api/files/${id}/download`);
    let data = await res.json();
    window.open(data.url, "_blank");
}
async function previewFile(id) {
    let res = await fetch(`/api/files/${id}/preview`);
    let data = await res.json();
    window.open(data.url, "_blank");
}
async function deleteFile(id) {
    await fetch(`/api/files/${id}/delete`, { method: "DELETE" });
    fetchFiles();
}

document.getElementById("uploadForm").addEventListener("submit", async e => {
    e.preventDefault();
    let file = document.getElementById("fileInput").files[0];
    let formData = new FormData();
    formData.append("file", file);
    await fetch("/api/upload", { method: "POST", body: formData });
    fetchFiles();
});

fetchFiles();
