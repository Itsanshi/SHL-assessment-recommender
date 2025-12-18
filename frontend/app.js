async function getRecommendations() {
  const query = document.getElementById("query").value;
  const output = document.getElementById("output");

  if (!query.trim()) {
    alert("Please enter a query or JD");
    return;
  }

  output.innerHTML = "Loading...";

  try {
    const response = await fetch("http://localhost:8000/recommend", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query })
    });

    const data = await response.json();
    renderResults(data.recommended_assessments);
  } catch (err) {
    output.innerHTML = "Error connecting to API";
  }
}

function renderResults(assessments) {
  const output = document.getElementById("output");
  output.innerHTML = "";

  assessments.forEach(a => {
    const div = document.createElement("div");
    div.className = "card";

    div.innerHTML = `
      <h3>${a.name}</h3>
      <p>${a.description}</p>
      <p><b>Duration:</b> ${a.duration} mins</p>
      <p><b>Test Type:</b> ${a.test_type.join(", ")}</p>
      <a href="${a.url}" target="_blank">View Assessment</a>
    `;

    output.appendChild(div);
  });
}
