async function askQuestion() {
  const question = document.getElementById("question").value;

  const res = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();

  document.getElementById("answer").innerText = data.answer;

  const sourcesList = document.getElementById("sources");
  sourcesList.innerHTML = "";

  data.sources.forEach(page => {
    const li = document.createElement("li");
    li.innerText = "Page " + page;
    sourcesList.appendChild(li);
  });
}
