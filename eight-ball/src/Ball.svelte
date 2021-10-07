<script>
  export let answer;
  export let isShaking;
  export let askQuestion;
  let hasHadAnAnswer = false;

  $: if (isShaking) {
    hasHadAnAnswer = true;
  }
  import { fade } from "svelte/transition";

  let disableHover = false;
  let m = { x: 0, y: 0 };

  function handleMousemove(event) {
    m.x = event.clientX;
    m.y = event.clientY;
  }

  function handleClick(event) {
    setTimeout(askQuestion, 1000);
    disableHover = !disableHover;
    setTimeout(() => (disableHover = !disableHover), 7000);
  }
</script>

<div
  class="ball-wrapper {disableHover ? 'nohover shake' : ''}"
  on:mousemove={handleMousemove}
  style="top:{m.y}px; left:{m.x}px"
  on:click={handleClick}
>
  <div class="ball" class:zooming={hasHadAnAnswer && !isShaking}>
    <div class="window">
      <div class="triangle">
        <p class="text">
          {answer}
        </p>
      </div>
      <div class="shadow" />
      {#if !answer || isShaking}
        <div transition:fade class="overlay" />
      {/if}
    </div>
  </div>
</div>

<style>
  .ball-wrapper {
    z-index: 1000;
    width: 50vh;
    height: 50vh;
    margin: 15vh auto;
    animation: 10s ease-in-out infinite;
  }
  .ball {
    width: 50vh;
    height: 50vh;
    border-radius: 50%;
    margin: 0 auto;
    background: radial-gradient(
      circle at 65% 15%,
      white 1px,
      rgb(39, 39, 39) 3%,
      rgb(12, 12, 12) 60%,
      rgb(39, 39, 39) 100%
    );
    display: flex;
    justify-content: center;
    align-items: center;
    animation: hover 10s ease-in-out infinite;
    pointer-events: none;
  }

  .window {
    width: 20vh;
    height: 20vh;
    z-index: 5;
    border-radius: 50%;
    background-color: black;
    position: relative;
  }

  .triangle {
    width: 0;
    height: 0;
    border-left: 7vh solid transparent;
    border-right: 7vh solid transparent;
    border-top: 10vh solid blue;
    position: absolute;
    top: 5vh;
    left: 3vh;
    font-family: sans-serif;
    font-variant: small-caps;
    animation: floating 6s linear infinite;
  }

  .shadow {
    z-index: 1;
    position: absolute;
    border-radius: 50%;
    width: 20vh;
    height: 20vh;
    background: linear-gradient(to left, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0));
    animation: rotating 6s infinite linear;
  }
  .overlay {
    z-index: 10;
    position: absolute;
    border-radius: 50%;
    width: 20vh;
    height: 20vh;
    background-color: black;
  }
  .text {
    position: absolute;
    top: -10vh;
    left: -2.8vh;
    font-size: 1.2vh;
    width: 6vh;
    text-align: center;
    font-family: sans-serif;
    font-variant: small-caps;
    color: white;
  }

  .zooming {
    animation: zoom 6s forwards ease-in-out;
  }

  @keyframes shake {
    0% {
      transform: rotate(1deg) translate(3px, 4px);
    }
    5% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    10% {
      transform: rotate(0deg) translate(vh, -5px);
    }
    15% {
      transform: rotate(2deg) translate(4px, vh);
    }
    20% {
      transform: rotate(1deg) translate(-3px, 3px);
    }
    25% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    30% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    35% {
      transform: rotate(-2deg) translate(3px, 4px);
    }
    40% {
      transform: rotate(0deg) translate(-3px, -3px);
    }
    45% {
      transform: rotate(-1deg) translate(4px, 4px);
    }
    50% {
      transform: rotate(1deg) translate(-4px, 3px);
    }
    55% {
      transform: rotate(2deg) translate(-4px, -1px);
    }
    60% {
      transform: rotate(0deg) translate(0, -5px);
    }
    65% {
      transform: rotate(2deg) translate(4px, 0);
    }
    70% {
      transform: rotate(1deg) trans0px 0pxlate (-3px, 3px);
    }
    75% {
      transform: rotate(4deg) translate(4px, -3px);
    }
    80% {
      transform: rotate(1deg) translate(3px, -5px);
    }
    85% {
      transform: rotate(1deg) translate(1px, -2px);
    }
    100% {
      transform: rotate(0deg) translate(0, 0px);
    }
  }
  .shake {
    animation: shake 1.2s ease-out 2;
  }

  /* Triangle gently floating around */
  @keyframes floating {
    from {
      transform: rotateZ(0) rotateY(15deg) translateZ(5vh) rotateZ(0);
    }
    to {
      transform: rotateZ(1turn) rotateY(15deg) translateZ(5vh) rotateZ(-1turn);
    }
  }

  @keyframes hover {
    0% {
      transform: translatey(0px);
    }
    50% {
      transform: translatey(-2vh);
    }
    100% {
      transform: translatey(0px);
    }
  }

  /* Roatating shadow */
  @keyframes rotating {
    to {
      transform: rotate(1turn);
    }
  }
  @keyframes zoom {
    0% {
      transform: scale(1);
    }
    20% {
      transform: scale(3);
    }
    80% {
      transform: scale(3);
    }
    100% {
      transform: scale(1);
    }
  }
  .nohover {
    pointer-events: none;
  }
  .ball-wrapper:hover {
    position: absolute;
    top: 0;
    left: 0;
    cursor: pointer;
    transform: translate(-50%, -50%);
  }
</style>
