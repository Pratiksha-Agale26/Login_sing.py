var readlineSync = require("readline-sync");

var score = 0;
var userName = readlineSync.question("WELCOME");

console.log("Hi Dear "+ userName);

function play(question,answer) {
  var userAnswer = readlineSync.question(question);

  if (userAnswer == answer) {
    console.log("Right Answer");
    score = score + 1;
} else {
    console.log("Wrong Answer")
    // score = score - 1
    console.log(".................")
  }
  console.log("Current score",score);
}

var questions = [{
  question: "who is my favorite person",
  answer: "my mother"
}, {
  question: "my favorite color",
  answer: "black"
}, {
  question: "what is my favorite dish",
  answer: "puran poli"
}, {
  question: "what is my birth date",
  answer: "26 nov"
}, {
  question: "what is my favorite hobby",
  answer: "cooking"


}]

for (var i=0; i<questions.length; i++){
  var currentQuestion = questions[i];
  play(currentQuestion.question,currentQuestion.answer)
}

console.log("Final score", score)