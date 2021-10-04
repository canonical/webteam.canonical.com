<script>
  import { Link } from "svelte-routing";
  import Ball from "./Ball.svelte";
  let answer = "";

  const urlParams = new URLSearchParams(window.location.search);

  var answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Do not count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
  ];

  if (urlParams.get("answers")) {
    answers = urlParams.get("answers").split(",");
  }

  const initialAnswersList = [...answers];

  let shouldRepeat = true;

  function askQuestion() {
    const index = Math.floor(Math.random() * answers.length);
    answer = answers[index];
    if (!shouldRepeat) {
      answers.splice(index, 1);
    }
  }

  const resetList = () => {
    answers = [...initialAnswersList];
  };
</script>

<main>
  <h1>APP NAME GOES HERE</h1>
  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps.
  </p>
  <input type="text" placeholder="Ask a question to the magic 8 ball" />
  <button on:click={askQuestion}>Ask</button>
  <input type="checkbox" id="repeat" bind:checked={shouldRepeat} />
  <label for="repeat">Repeat</label>
  <Ball {answer} />
  <button on:click={resetList}>Reset list</button>
  <Link to="create">Create</Link>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
