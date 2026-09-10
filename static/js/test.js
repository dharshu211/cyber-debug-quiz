let remainingSeconds = Math.max(0, startingTime);
let testTerminated = false;
let submitting = false;
const timerElement = document.getElementById("timer");
const overlay = document.getElementById("antiCheatOverlay");

function updateTimer() {
    const minutes = Math.floor(remainingSeconds / 60);
    const seconds = remainingSeconds % 60;
    timerElement.textContent = String(minutes).padStart(2, "0") + ":" + String(seconds).padStart(2, "0");
    if (remainingSeconds <= 0) { automaticSubmit(); return; }
    remainingSeconds--;
}
updateTimer();
const timerInterval = setInterval(updateTimer, 1000);

function automaticSubmit() {
    if (submitting || testTerminated) return;
    submitting = true;
    clearInterval(timerInterval);
    document.getElementById("testForm").submit();
}

function terminateTest() {
    if (testTerminated || submitting) return;
    testTerminated = true;
    clearInterval(timerInterval);
    if (overlay) overlay.classList.add("show");
    fetch("/terminate", { method: "POST", headers: { "Content-Type": "application/json" }, keepalive: true })
        .finally(function () {
            setTimeout(function () { window.location.href = "/thank-you"; }, 900);
        });
}

// A normal browser cannot identify whether a participant opened ChatGPT,
// Gemini, Claude, etc. We therefore detect leaving this test tab/window.
document.addEventListener("visibilitychange", function () {
    if (document.hidden && !testTerminated && !submitting) terminateTest();
});
window.addEventListener("blur", function () {
    if (!testTerminated && !submitting) terminateTest();
});
document.addEventListener("fullscreenchange", function () {
    if (!document.fullscreenElement && !testTerminated && !submitting) terminateTest();
});

// Copy, cut, paste, selection and the context menu are intentionally allowed.
// This lets participants copy the buggy code from this page and paste/edit it
// in the answer box. Browser security cannot reliably tell where pasted text came from.

// Block shortcuts that deliberately navigate away or open developer tools.
document.addEventListener("keydown", function (e) {
    const key = e.key.toLowerCase();
    if (e.key === "F12" || (e.ctrlKey && e.shiftKey && ["i", "j", "c"].includes(key))) {
        e.preventDefault();
        terminateTest();
    }
});

// Question navigation
const questionCards = Array.from(document.querySelectorAll(".question-card"));
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");
const progress = document.getElementById("questionProgress");
let currentQuestion = 0;

function showQuestion(index) {
    if (!questionCards.length) return;
    currentQuestion = Math.max(0, Math.min(index, questionCards.length - 1));
    questionCards.forEach((card, i) => {
        card.classList.toggle("question-hidden", i !== currentQuestion);
    });
    prevBtn.disabled = currentQuestion === 0;
    const last = currentQuestion === questionCards.length - 1;
    nextBtn.hidden = last;
    submitBtn.hidden = !last;
    progress.textContent = "Question " + (currentQuestion + 1) + " of " + questionCards.length;
    window.scrollTo({ top: 0, behavior: "smooth" });
}

prevBtn.addEventListener("click", function () { showQuestion(currentQuestion - 1); });
nextBtn.addEventListener("click", function () { showQuestion(currentQuestion + 1); });

document.getElementById("testForm").addEventListener("submit", function () {
    submitting = true;
    clearInterval(timerInterval);
});

showQuestion(0);

// Dynamic line numbers for every participant answer editor.
function syncLineNumbers(textarea) {
    const gutter = textarea.parentElement.querySelector('.line-numbers');
    if (!gutter) return;
    const lineCount = Math.max(1, textarea.value.split('\n').length);
    gutter.textContent = Array.from({length: lineCount}, (_, i) => i + 1).join('\n');
    gutter.scrollTop = textarea.scrollTop;
}

document.querySelectorAll('.code-editor textarea').forEach(function(textarea) {
    syncLineNumbers(textarea);
    textarea.addEventListener('input', function() { syncLineNumbers(textarea); });
    textarea.addEventListener('scroll', function() { syncLineNumbers(textarea); });
});
