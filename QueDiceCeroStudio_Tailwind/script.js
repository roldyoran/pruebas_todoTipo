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
        gridItem.classList.add('grid-item', 'font-medium' , 'p-2', 'border', 'border-gray-300', 'rounded', 'cursor-pointer', 'bg-indigo-900', 'text-white', 'text-3xl', 'hover:bg-blue-500', 'transition', 'ease-in-out', 'duration-300'); // Cambié el color a 'bg-indigo-800' y 'hover:bg-indigo-600'

        gridItem.textContent = index + 1;

        gridItem.addEventListener('click', function () {
            gridItem.textContent = respuesta;
        });

        answersContainer.appendChild(gridItem);
    });
}



// function showAnswer(index, respuesta) {
//     alert(`Respuesta ${index}: ${respuesta}`);
// }
