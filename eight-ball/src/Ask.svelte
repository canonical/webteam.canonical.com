<script>
  import { Link } from "svelte-routing";
  import Ball from "./Ball.svelte";
  let answer = "";
  let isShaking = false;

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

  let question = urlParams.get("q");

  const initialAnswersList = [...answers];

  let shouldRepeat = true;

  function askQuestion() {
    isShaking = true;
    const index = Math.floor(Math.random() * answers.length);

    if (!shouldRepeat) {
      answers.splice(index, 1);
    }
    // wait 1s before showing the answer
    setTimeout(() => {
      answer = answers[index];
      isShaking = false;
    }, 1000);
  }

  const resetList = () => {
    answers = [...initialAnswersList];
  };
</script>

<main>
  <h1>Can🎱niball</h1>
  <div class="form__group field">
    <input
      type="input"
      class="form__field"
      placeholder="Question"
      name="Question"
      id="Question"
      bind:value={question}
    />
    <label for="Question" class="form__label">Question</label>
  </div>
  <div class="button-wrapper">
    <button class="button" on:click={askQuestion}>Ask</button>
    <input type="checkbox" id="repeat" bind:checked={shouldRepeat} />
    <label for="repeat">Repeat</label>
  </div>
  <Ball {answer} {isShaking} {askQuestion}/>
  <button class="button" on:click={resetList}>Reset list</button>
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
    color: #e95420;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }

  .form__group {
    position: relative;
    padding: 15px 0 0;
    margin-top: 10px;
    width: 50%;
  }
  .form__field {
    font-family: inherit;
    width: 100%;
    border: 0;
    border-bottom: 2px solid white;
    outline: 0;
    font-size: 1.3rem;
    color: white;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
  }
  .form__field::placeholder {
    color: transparent;
  }

  .form__field:placeholder-shown ~ .form__label {
    font-size: 1.3rem;
    cursor: text;
    top: 20px;
  }

  .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 1rem;
    color: white;
  }

  .form__field:focus {
    padding-bottom: 6px;
    font-weight: 700;
    border-width: 3px;
    border-image: linear-gradient(to right, white, white);
    border-image-slice: 1;
  }

  .form__field:focus ~ .form__label {
    position: absolute;
    top: 0;
    display: block;
    transition: 0.2s;
    font-size: 1rem;
    color: white;
    font-weight: 700;
  }
  /* reset input */
  .form__field:required,
  .form__field:invalid {
    box-shadow: none;
  }
  .button-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.7rem 2rem;
    font-family: "Poppins", sans-serif;
    font-weight: 700;
    font-size: 18px;
    text-align: center;
    text-decoration: none;
    color: #fff;
    backface-visibility: hidden;
    border: 2px solid transparent;
    border-radius: 3rem;
    background: transparent;
    cursor: pointer;
  }

  .button {
    border-color: #fff;
    transition: transform 0.2s cubic-bezier(0.235, 0, 0.05, 0.95);
  }

  .button:hover {
    transform: perspective(1px) scale3d(1.044, 1.044, 1) translateZ(0) !important;
  }
</style>
