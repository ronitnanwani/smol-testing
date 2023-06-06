document.addEventListener("DOMContentLoaded", () => {
  const gameboard = document.getElementById("gameboard");
  const gameStatus = document.getElementById("game-status");
  const restartButton = document.getElementById("restart-button");
  const humanScoreElement = document.getElementById("human-score");
  const computerScoreElement = document.getElementById("computer-score");

  let gameBoardState = Array.from({ length: 3 }, () => Array(3).fill(null));
  let currentPlayer = "human";
  let humanScore = 0;
  let computerScore = 0;
  humanScoreElement.textContent = humanScore;
  computerScoreElement.textContent = computerScore;

  function makeMove(row, column, player) {
    if (gameBoardState[row][column] === null) {
      gameBoardState[row][column] = player;
      document.getElementById(`cell-${row}-${column}`).textContent = player === "human" ? "X" : "O";
      return true;
    }
    return false;
  }

  function checkWinner() {
    const lines = [
      [[0, 0], [0, 1], [0, 2]],
      [[1, 0], [1, 1], [1, 2]],
      [[2, 0], [2, 1], [2, 2]],
      [[0, 0], [1, 0], [2, 0]],
      [[0, 1], [1, 1], [2, 1]],
      [[0, 2], [1, 2], [2, 2]],
      [[0, 0], [1, 1], [2, 2]],
      [[0, 2], [1, 1], [2, 0]],
    ];

    for (const line of lines) {
      const [a, b, c] = line;
      if (
        gameBoardState[a[0]][a[1]] &&
        gameBoardState[a[0]][a[1]] === gameBoardState[b[0]][b[1]] &&
        gameBoardState[a[0]][a[1]] === gameBoardState[c[0]][c[1]]
      ) {
        return gameBoardState[a[0]][a[1]];
      }
    }
    return null;
  }

  function checkTie() {
    return gameBoardState.every(row => row.every(cell => cell !== null));
  }

  async function computerMove() {
    var mes={};
    const handlemessage = (msg) => {
      mes=msg;
    }
    await fetch("http://127.0.0.1:5000/computer_move", {
      method: "POST",
      body: JSON.stringify({"gameBoardState":gameBoardState}),
    }).then(response => response.json()).then(message => (
      handlemessage(message)
    ))
    return ({"row":mes["row"],"column":mes["column"]});
  }

  function humanMove(event) {
    const cell = event.target;
    const myArray = cell.id.split("-")
    const row = myArray[1];
    // console.log(row)
    const column = myArray[2];
    // console.log(column)

    if (makeMove(row, column, currentPlayer)) {
      const winner = checkWinner();
      if (winner) {
        gameStatus.textContent = winner === "human" ? "You Won!" : "Computer Won!";
        winner === "human" ? humanScore++ : computerScore++;
        updateLeaderboard();
      } else if (checkTie()) {
        gameStatus.textContent = "Tie Game!";
      } else {
        currentPlayer = "computer";
        gameStatus.textContent = "Computer Turn";
          computerMove().then(({ row, column }) => {
            console.log(row,column);
            makeMove(row, column, currentPlayer);
            const winner = checkWinner();
            if (winner) {
              gameStatus.textContent = winner === "human" ? "You Won!" : "Computer Won!";
              winner === "human" ? humanScore++ : computerScore++;
              updateLeaderboard();
            } else if (checkTie()) {
              gameStatus.textContent = "Tie Game!";
            } else {
              currentPlayer = "human";
              gameStatus.textContent = "Your Turn";
            }
          });
      }
    }
  }

  function updateLeaderboard() {
    humanScoreElement.textContent = humanScore;
    computerScoreElement.textContent = computerScore;
  }

  function restartGame() {
    gameBoardState = Array.from({ length: 3 }, () => Array(3).fill(null));
    currentPlayer = "human";
    gameStatus.textContent = "Your Turn";
    gameboard.querySelectorAll(".cell").forEach(cell => (cell.textContent = ""));
  }

  gameboard.addEventListener("click", humanMove);
  restartButton.addEventListener("click", restartGame);
});