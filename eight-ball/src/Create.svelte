<script>
  import { Link } from "svelte-routing";
  let answerList = [];
  let answer = "";
  let answerInput;

  const addAnswer = () => {
    const answers = answer.split(";");
    answerList = [...answerList, ...answers];
    answer = "";
    answerInput.focus();
  };
  const onKeyPress = (e) => {
    if (e.key === "Enter") addAnswer();
  };

  const removeItem = (index) => {
    answerList = answerList.slice(0, index).concat(answerList.slice(index + 1));
  };
</script>

<main class="container">
  <header>
    <h1>CREATE YOUR OWN MAGIC 8 BALL!!!!!!!!!!</h1>
    <p>Add your own answers</p>
  </header>
  <input
    type="text"
    id="answer"
    placeholder="Most likely"
    bind:value={answer}
    bind:this={answerInput}
    on:keypress={onKeyPress}
  />
  <button on:click={addAnswer} disabled={!answer} type="submit" class="btn"
    >Add</button
  >

  <ul class="list">
    {#each answerList as answer, i}
      <li class="list__item">
        <span>{answer}</span>
        <button
          on:click={() => {
            removeItem(i);
          }}
          ><svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="#000000"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            ><line x1="18" y1="6" x2="6" y2="18" /><line
              x1="6"
              y1="6"
              x2="18"
              y2="18"
            /></svg
          ></button
        >
      </li>
    {/each}
  </ul>
  <Link to="/?answers={answerList.toString()}"
    ><button class="btn btn--success">Generate</button></Link
  >
</main>

<style>
  header {
    padding: 2rem 0rem;
  }
  .container {
    width: 90%;
    max-width: 900px;
    margin: 0 auto;
  }

  .btn {
    padding: 0.25em 0.75em;
    min-width: 10ch;
    min-height: 44px;
    border-radius: 0.5rem;
    font-size: 1.2rem;
  }

  .btn:disabled {
    background: #f1f1f1;
    color: black;
  }

  .btn--success {
    background-color: #ffdc7d;
    color: #000;
  }

  input {
    font-size: 16px;
    padding: 0.25em 0.75em;
    border-radius: 0.5rem;
    transition: 180ms box-shadow ease-in-out;
    min-height: 44px;
    width: 90%;
    max-width: 600px;
    margin-right: 1rem;
  }

  input:focus {
    outline: 3px solid transparent;
    box-shadow: 0 0 3px orange;
  }

  .list__item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: white;
    color: black;
    font-size: 1.5rem;
    padding: 0.5rem 1.2rem;
  }

  .list__item > span {
    width: 90%;
  }

  .list__item > button {
    min-height: 44px;
    font-size: 1.2rem;
    padding: 0.25em 0.75em;
  }
</style>
