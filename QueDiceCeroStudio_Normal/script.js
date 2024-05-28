let currentQuestionIndex = 0;
let questions;

document.getElementById('fileInput').addEventListener('change', handleFileSelect);

function handleFileSelect(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            questions = JSON.parse(e.target.result);
            currentQuestionIndex = 0;
            displayQuestionAndAnswers(questions[currentQuestionIndex]);
        };

        reader.readAsText(file);
    }
}

function loadPreviousQuestion() {
    currentQuestionIndex--;
    if (currentQuestionIndex < 0) {
        currentQuestionIndex = questions.length - 1;
    }
    displayQuestionAndAnswers(questions[currentQuestionIndex]);
}


function loadNextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex >= questions.length) {
        currentQuestionIndex = 0;
    }
    displayQuestionAndAnswers(questions[currentQuestionIndex]);
}

function displayQuestionAndAnswers(data) {
    const questionElement = document.getElementById('question');
    const answersContainer = document.getElementById('answers');

    questionElement.textContent = data.pregunta;

    answersContainer.innerHTML = '';
    data.respuestas.forEach((respuesta, index) => {
        const gridItem = document.createElement('div');
        gridItem.classList.add('grid-item');
        gridItem.textContent = index + 1; // Mostrar número en lugar de respuesta

        gridItem.addEventListener('click', function () {
            // Al hacer clic, ocultar el número y mostrar la respuesta
            gridItem.textContent = respuesta;
            // gridItem.style.backgroundColor = ''; // Restaurar el color de fondo
            // gridItem.style.color = ''; // Restaurar el color del texto
            // gridItem.classList.remove('grid-item-clickable'); // Eliminar el cursor pointer
            // gridItem.removeEventListener('click', handleClick); // Eliminar el manejador de clic
        });

        answersContainer.appendChild(gridItem);
    });
}


// function showAnswer(index, respuesta) {
//     alert(`Respuesta ${index}: ${respuesta}`);
// }
