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
  <button
    on:click={addAnswer}
    disabled={!answer}
    type="submit"
    class="btn btn--success">Add</button
  >
  <Link to="/?answers={answerList.toString()}"
    ><button class="btn">Generate</button></Link
  >
  <ul class="list">
    {#each answerList as answer, i}
      <li class="list__item">
        {answer}
        <button
          on:click={() => {
            removeItem(i);
          }}>X</button
        >
      </li>
    {/each}
  </ul>
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

  .btn--success {
    background-color: green;
    color: #fff;
  }

  input {
    font-size: 16px;
    font-family: inherit;
    padding: 0.25em 0.5em;
    border-radius: 0.5rem;
    transition: 180ms box-shadow ease-in-out;
    min-height: 44px;
    width: 50%;
  }

  input:focus {
    outline: 3px solid transparent;
    box-shadow: 0 0 3px orange;
  }

  .list__item {
    display: flex;
    justify-content: space-between;
    background: white;
    color: black;
    font-size: 2rem;
    padding: 0.5rem 1.2rem;
  }
</style>
