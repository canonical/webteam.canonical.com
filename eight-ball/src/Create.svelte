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

<main>
  <h1>CREATE YOUR OWN MAGIC 8 BALL!!!!!!!!!!</h1>
  <h3>Add you own answers</h3>
  <input
    type="text"
    id="answer"
    placeholder="Most likely"
    bind:value={answer}
    bind:this={answerInput}
    on:keypress={onKeyPress}
  />
  <button on:click={addAnswer} disabled={!answer} type="submit">Add</button>
  {#each answerList as answer, i}
    <li>
      {answer}
      <button
        on:click={() => {
          removeItem(i);
        }}>X</button
      >
    </li>
  {/each}
  <Link to="/?answers={answerList.toString()}"><button>GENERATE</button></Link>
</main>
