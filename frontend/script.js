const API_URL = "http://127.0.0.1:8000/tasks/";

// Listar todas as tarefas
const fetchTasks = async () => {
  const response = await fetch(API_URL);
  const tasks = await response.json();
  const taskList = document.getElementById("task-list");
  taskList.innerHTML = "";

  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <h3>${task.title}</h3>
      <p>${task.description}</p>
      <a href="edit.html?id=${task.id}"><button class="warning">Editar</button></a>
      <button class="danger" onclick="deleteTask(${task.id})">Excluir</button>
    `;
    taskList.appendChild(li);
  });
};

// Criar nova tarefa
document
  .getElementById("create-task-form")
  ?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description }),
    });

    window.location.href = "index.html";
  });

// Excluir tarefa
const deleteTask = async (taskId) => {
  if (confirm("Tem certeza que deseja excluir esta tarefa?")) {
    await fetch(API_URL + taskId, { method: "DELETE" });
    fetchTasks();
  }
};

// Editar tarefa (Carregar dados)
const loadTaskForEditing = async () => {
  const params = new URLSearchParams(window.location.search);
  const taskId = params.get("id");
  if (!taskId) return;

  const response = await fetch(API_URL + taskId);
  const task = await response.json();

  document.getElementById("task-id").value = task.id;
  document.getElementById("title").value = task.title;
  document.getElementById("description").value = task.description;
};

// Salvar edição
document
  .getElementById("edit-task-form")
  ?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const taskId = document.getElementById("task-id").value;
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    await fetch(API_URL + taskId, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, description }),
    });

    window.location.href = "index.html";
  });

// Carregar lista de tarefas automaticamente
if (document.getElementById("task-list")) {
  fetchTasks();
}

// Carregar dados na edição
if (document.getElementById("edit-task-form")) {
  loadTaskForEditing();
}
